"""
.. module:: CNN2DS2SArchitecture

CNNS2SArchitecture
*************


:Description: CNN2DS2SSArchitecture

    Class for convolutional sequence to sequence architecture with 2D convolutions


:Authors: HPAI-BSC
    

:Version: 

:Created on: 24/10/2018 8:10 

"""

from Wind.Architectures.NNS2SArchitecture import NNS2SArchitecture
from keras.models import Sequential, load_model, Model
from keras.layers import Dense, Dropout, Conv2D, Flatten, Input
from sklearn.metrics import r2_score
from Wind.Train.Activations import generate_activation

from keras.regularizers import l1, l2

__author__ = 'HPAI-BSC'


class CNNS2S2DArchitecture(NNS2SArchitecture):
    """
    Class for convolutional sequence to sequence architecture with 2D convolutions

    """
    modfile = None
    modname = 'CNNS2S2D'
    data_mode = ('4D', '2D')

    def generate_model(self):
        """
        Model for CNN with 2D convolutions for S2S

        json config:

        "arch": {
            "filters": [32],
            "strides": [1,1],
            "dilation": false,
            "kernel_size": [3],
            "k_reg": "None",
            "k_regw": 0.1,
            "rec_reg": "None",
            "rec_regw": 0.1,
            "drop": 0,
            "activation": "relu",
            "activation_full": "linear",
            "full": [16,8],
            "fulldrop": 0,
            "mode":"CNN_s2s"
        }

        :return:
        """
        drop = self.config['arch']['drop']
        filters = self.config['arch']['filters']

        kernel_size = self.config['arch']['kernel_size']
        # If there is a dilation field and it is true the strides field is the dilation rates
        # and the strides are all 1's
        if 'dilation' in self.config['arch'] and self.config['arch']['dilation']:
            dilation = self.config['arch']['strides']
            strides = [[1,1]] * len(dilation)
        else:
            strides = self.config['arch']['strides']
            dilation = [[1,1]] * len(strides)
        activationfl = self.config['arch']['activation_full']
        fulldrop = self.config['arch']['fulldrop']
        full_layers = self.config['arch']['full']

        activation = self.config['arch']['activation']

        k_reg = self.config['arch']['k_reg']
        k_regw = self.config['arch']['k_regw']

        # Extra added from training function
        idimensions = self.config['idimensions']
        odimensions = self.config['odimensions']

        if k_reg == 'l1':
            k_regularizer = l1(k_regw)
        elif k_reg == 'l2':
            k_regularizer = l2(k_regw)
        else:
            k_regularizer = None

        input = Input(shape=(idimensions))
        # We assume that the kernel size for the dimension corresponding to the variables is always the number of variables
        model = Conv2D(filters[0], input_shape=(idimensions), kernel_size=[kernel_size[0],idimensions[1]], strides=[1,strides[0]],
                              padding='same', dilation_rate=dilation[0],
                              kernel_regularizer=k_regularizer)(input)
        model = generate_activation(activation)(model)

        if drop != 0:
            model = Dropout(rate=drop)(model)

        for i in range(1, len(filters)):
            model = Conv2D(filters[i], kernel_size=[kernel_size[i], idimensions[0]], strides=[1,strides[i]],
                              padding='same', dilation_rate=dilation[i],
                              kernel_regularizer=k_regularizer)(model)
            model = generate_activation(activation)(model)

            if drop != 0:
                model = Dropout(rate=drop)(model)

        model = Flatten()(model)
        for l in full_layers:
            model= Dense(l)(model)
            model = generate_activation(activationfl)(model)
            if fulldrop != 0:
                model = Dropout(rate=fulldrop)(model)

        output = Dense(odimensions, activation='linear')(model)

        self.model = Model(inputs=input, outputs=output)

    # def evaluate(self, val_x, val_y, test_x, test_y):
    #     batch_size = self.config['training']['batch']
    #
    #     if self.runconfig.best:
    #         self.model = load_model(self.modfile)
    #     val_yp = self.model.predict(val_x, batch_size=batch_size, verbose=0)
    #     test_yp = self.model.predict(test_x, batch_size=batch_size, verbose=0)
    #
    #     # Maintained to be compatible with old configuration files
    #     if type(self.config['data']['ahead'])==list:
    #         ahead = self.config['data']['ahead'][1]
    #     else:
    #         ahead = self.config['data']['ahead']
    #
    #     lresults = []
    #     for i in range(1, ahead + 1):
    #         lresults.append((i,
    #                          r2_score(val_y[:, i - 1], val_yp[:, i - 1]),
    #                          r2_score(test_y[:, i - 1], test_yp[:, i - 1])
    #                          ))
    #     return lresults

