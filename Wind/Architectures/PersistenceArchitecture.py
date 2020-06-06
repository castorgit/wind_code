""""
.. module:: PersistenceArchitecture
PersistenceArchitecture
******
:Description: PersistenceArchitecture
    Class for persistence model
:Authors:
    HPAI-BSC
:Version: 
:Date:  13/07/2018
"""

from Wind.Architectures.Architecture import Architecture
from Wind.ErrorMeasure import ErrorMeasure
import h5py
import numpy as np


__author__ = 'HPAI-BSC'


class PersistenceArchitecture(Architecture):
    """Class for persistence model
    """
    ## Data mode default for input, 1 dimensional output
    data_mode = ('2D', '2D')
    modname = 'Persistence'
    def generate_model(self):
        """
        Generates the model
        :return:
        """
        pass

    def train(self, train_x, train_y, val_x, val_y):
        """
        Trains the model
        :return:
        """
        pass

    def summary(self):
        """Model summary
        prints all the fields stored in the configuration for the experiment
        :return:
        """
        print("--------- Architecture parameters -------")
        print(f"{self.modname}")
        for c in self.config['arch']:
            print(f"# {c} = {self.config['arch'][c]}")
        print("--------- Data parameters -------")
        for c in self.config['data']:
            print(f"# {c} = {self.config['data'][c]}")
        if 'training' in self.config:
            print("--------- Training parameters -------")
            for c in self.config['training']:
                print(f"# {c} = {self.config['training'][c]}")
            print("---------------------------------------")

    def evaluate(self, val_x, val_y, test_x, test_y, scaler=None, save_errors=None):
        """
        Evaluates the training
        :param save_errors:
        :return:
        """
        if type(self.config['data']['ahead']) == list:
            ahead = self.config['data']['ahead'][1]
        else:
            ahead = self.config['data']['ahead']
        print('shapes', val_x.shape, val_y.shape, test_x.shape, test_y.shape)
        val_yp = np.tile(val_x[:,17],(12,1)).transpose()
        test_yp = np.tile(test_x[:,17],(12,1)).transpose()

        lresults = []
        for i in range(1, ahead + 1):
            lresults.append([i]  + ErrorMeasure().compute_errors(val_x[:, -1],
                                                                 val_y[:, i - 1],
                                                                 test_x[:, -1],
                                                                 test_y[:, i - 1]))
        if save_errors is not None:
            f = h5py.File(f'errors{self.modname}-S{self.config["data"]["datanames"][0]}{save_errors}.hdf5', 'w')
            dgroup = f.create_group('errors')
            dgroup.create_dataset('val_y', val_y.shape, dtype='f', data=val_y, compression='gzip')
            dgroup.create_dataset('val_yp', val_yp.shape, dtype='f', data=val_yp, compression='gzip')
            dgroup.create_dataset('test_y', test_y.shape, dtype='f', data=test_y, compression='gzip')
            dgroup.create_dataset('test_yp', test_yp.shape, dtype='f', data=test_y, compression='gzip')
            if scaler is not None:
                # Unidimensional vectors
                dgroup.create_dataset('val_yu', val_y.shape, dtype='f', data=scaler.inverse_transform(val_y.reshape(-1, 1)), compression='gzip')
                dgroup.create_dataset('val_ypu', val_yp.shape, dtype='f', data=scaler.inverse_transform(val_yp.reshape(-1, 1)), compression='gzip')
                dgroup.create_dataset('test_yu', test_y.shape, dtype='f', data=scaler.inverse_transform(test_y.reshape(-1, 1)), compression='gzip')
                dgroup.create_dataset('test_ypu', test_yp.shape, dtype='f', data=scaler.inverse_transform(test_yp.reshape(-1, 1)), compression='gzip')

        return lresults

