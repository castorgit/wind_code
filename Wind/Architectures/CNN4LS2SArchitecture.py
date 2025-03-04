"""
.. module:: CNN4LS2SArchitecture

CNNS2SArchitecture
*************


:Description: CNN4LS2SArchitecture

    Class for convolutional sequence to sequence architecture with exactly 4 layers


:Authors: HPAI-BSC
    

:Version: 

:Created on: 24/10/2018 8:10 

"""

from Wind.Architectures.NNS2SArchitecture import NNS2SArchitecture
from keras.models import Sequential, load_model, Model
from keras.layers import Dense, Dropout, Conv1D, Flatten, Input
from sklearn.metrics import r2_score
from Wind.Train.Activations import generate_activation

from keras.regularizers import l1, l2

__author__ = 'HPAI-BSC'


class CNN4LS2SArchitecture(NNS2SArchitecture):
    """
    Class for convolutional sequence to sequence architecture

    """
    modfile = None
    modname = 'CNN4LS2S'
    data_mode = ('3D', '2D') #'cnn'

    def generate_model(self):
        """
        Model for CNN  for S2S

        json config:

        "arch": {
            "filters": [32],
            "strides": [1],
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
            strides = [1] * len(dilation)
        else:
            strides = self.config['arch']['strides']
            dilation = [1] * len(strides)

        # 2nd Layer
        drop2 = self.config['arch']['drop2']
        filters2 = self.config['arch']['filters2']
        kernel_size2 = self.config['arch']['kernel_size2']
        # If there is a dilation field and it is true the strides field is the dilation rates
        # and the strides are all 1's
        if 'dilation' in self.config['arch'] and self.config['arch']['dilation']:
            dilation2 = self.config['arch']['strides2']
            strides2 = [1] * len(dilation2)
        else:
            strides2 = self.config['arch']['strides2']
            dilation2 = [1] * len(strides2)

        # 3rd Layer
        drop3 = self.config['arch']['drop3']
        filters3 = self.config['arch']['filters3']
        kernel_size3 = self.config['arch']['kernel_size3']
        # If there is a dilation field and it is true the strides field is the dilation rates
        # and the strides are all 1's
        if 'dilation' in self.config['arch'] and self.config['arch']['dilation']:
            dilation3 = self.config['arch']['strides3']
            strides3 = [1] * len(dilation3)
        else:
            strides3 = self.config['arch']['strides3']
            dilation3 = [1] * len(strides3)

        # 4th Layer
        drop4 = self.config['arch']['drop4']
        filters4 = self.config['arch']['filters4']
        kernel_size4 = self.config['arch']['kernel_size4']
        # If there is a dilation field and it is true the strides field is the dilation rates
        # and the strides are all 1's
        if 'dilation' in self.config['arch'] and self.config['arch']['dilation']:
            dilation4 = self.config['arch']['strides4']
            strides4 = [1] * len(dilation4)
        else:
            strides4 = self.config['arch']['strides4']
            dilation4 = [1] * len(strides4)

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
        model = Conv1D(filters[0], input_shape=(idimensions), kernel_size=kernel_size[0], strides=strides[0],
                              padding='causal', dilation_rate=dilation,
                              kernel_regularizer=k_regularizer)(input)
        model = generate_activation(activation)(model)

        if drop != 0:
            model = Dropout(rate=drop)(model)

        # 2nd Layer
        model = Conv1D(filters2[0], kernel_size=kernel_size2[0], strides=strides2[0],
                          padding='causal', dilation_rate=dilation2,
                          kernel_regularizer=k_regularizer)(model)
        model = generate_activation(activation)(model)

        if drop2 != 0:
            model = Dropout(rate=drop2)(model)

        # 3rd Layer
        model = Conv1D(filters3[0], kernel_size=kernel_size3[0], strides=strides3[0],
                          padding='causal', dilation_rate=dilation3,
                          kernel_regularizer=k_regularizer)(model)
        model = generate_activation(activation)(model)

        if drop3 != 0:
            model = Dropout(rate=drop3)(model)

        # 4th Layer
        model = Conv1D(filters4[0], kernel_size=kernel_size4[0], strides=strides4[0],
                          padding='causal', dilation_rate=dilation4,
                          kernel_regularizer=k_regularizer)(model)
        model = generate_activation(activation)(model)

        if drop4 != 0:
            model = Dropout(rate=drop4)(model)

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

