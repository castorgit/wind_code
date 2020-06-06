"""
.. module:: NNS2SArchitecture
NNS2SArchitecture
*************
:Description: SCKS2SArchitecture
    
:Authors: HPAI-BSC
    
:Version: 
:Created on: 19/10/2018 10:32 
"""

from Wind.Architectures.SCKArchitecture import SCKArchitecture
from Wind.ErrorMeasure import ErrorMeasure
import h5py

__author__ = 'HPAI-BSC'


class SCKS2SArchitecture(SCKArchitecture):
    """
    Class for all the neural networks models based on sequence to sequence
    """
    def evaluate(self, val_x, val_y, test_x, test_y, scaler=None, save_errors=None):
        """
        Evaluates the trained model with validation and test
        Overrides parent function
        :param save_errors:
        :param val_x:
        :param val_y:
        :param test_x:
        :param test_y:
        :return:
        """

        val_yp = self.model.predict(val_x)
        test_yp = self.model.predict(test_x)

        # Maintained to be compatible with old configuration files
        if type(self.config['data']['ahead'])==list:
            iahead = self.config['data']['ahead'][0]
            ahead = (self.config['data']['ahead'][1] - self.config['data']['ahead'][0]) + 1
        else:
            iahead = 1
            ahead = self.config['data']['ahead']
        
        print('ahi vamos',save_errors)

        if save_errors is not None:
            print("crear fichero",f'errors{self.modname}-S{self.config["data"]["datanames"][0]}{save_errors}.hdf5')
#            f = h5py.File(f'errors{self.modname}-S{self.config["data"]["datanames"][0]}{save_errors}.hdf5', 'w')
            f = h5py.File(f'errors{self.modname}-S{self.config["data"]["datanames"][0]}{save_errors}.hdf5', 'w')
            dgroup = f.create_group('errors')
            dgroup.create_dataset('val_y', val_y.shape, dtype='f', data=val_y, compression='gzip')
            dgroup.create_dataset('val_yp', val_yp.shape, dtype='f', data=val_yp, compression='gzip')
            dgroup.create_dataset('test_y', test_y.shape, dtype='f', data=test_y, compression='gzip')
            dgroup.create_dataset('test_yp', test_yp.shape, dtype='f', data=test_y, compression='gzip')
            if scaler is not None:
                # n-dimensional vectors
                dgroup.create_dataset('val_yu', val_y.shape, dtype='f', data=scaler.inverse_transform(val_y), compression='gzip')
                dgroup.create_dataset('val_ypu', val_yp.shape, dtype='f', data=scaler.inverse_transform(val_yp), compression='gzip')
                dgroup.create_dataset('test_yu', test_y.shape, dtype='f', data=scaler.inverse_transform(test_y), compression='gzip')
                dgroup.create_dataset('test_ypu', test_yp.shape, dtype='f', data=scaler.inverse_transform(test_yp), compression='gzip')

        lresults = []
        for i, p in zip(range(1, ahead + 1), range(iahead, self.config['data']['ahead'][1]+1)):
            lresults.append([p] + ErrorMeasure().compute_errors(val_y[:, i - 1],
                                                               val_yp[:, i - 1],
                                                               test_y[:, i - 1],
                                                               test_yp[:, i - 1], scaler))

        return lresults