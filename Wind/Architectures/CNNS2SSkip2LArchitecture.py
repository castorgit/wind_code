"""
.. module:: CNNS2SArchitecture

CNNS2SArchitecture
*************


:Description: CNNS2SArchitecture

    Class for convolutional sequence to sequence architecture


:Authors: HPAI-BSC
: modified jaume for second layer
    

:Version: 

:Created on: 24/10/2018 8:10 

"""
from keras import backend as K
from keras.layers import merge,Reshape, Add

from Wind.Architectures.NNS2SArchitecture import NNS2SArchitecture
from keras.models import Sequential, load_model, Model
from keras.layers import Dense, Dropout, Conv1D, Flatten, Input, Concatenate, MaxPooling1D, SeparableConv1D
from sklearn.metrics import r2_score
from Wind.Train.Activations import generate_activation

from keras.regularizers import l1, l2

__author__ = 'HPAI-BSC'


class CNNS2SSkip2LArchitecture(NNS2SArchitecture):
    """
    Class for convolutional sequence to sequence architecture

    """
    modfile = None
    modname = 'CNNS2SSKIP'
    data_mode = ('3D', '2D') #'cnn'

    def generate_model(self):
        """
        Model for CNN with Encoder Decoder for S2S

        json config:

        "arch": {
                 "filters": [1024],
                 "strides": [2],
                 "kernel_size": [9],
                 "depth_multiplier": 8,
                 "activation": ["elu",0.3],
                 "drop": 0.6,
                 "filters2": [1024],
                 "strides2": [4],
                 "kernel_size2": [1],
                 "depth_multiplier2": 7,
                 "activation2": ["elu",0.3],
                 "drop2": 0.6,
                 "dilation": false,
                 "k_reg": "None",
                 "k_regw": 0.1,
                 "rec_reg": "None",
                 "rec_regw": 0.1,
                 "activation_full": ["elu",0.4],
                 "fulldrop": 0.10,
                 "full": [1024],
        }

        :return:
        """
        tipus = self.config['arch']['tipus'] # 1 = res, 2, 2 residual, 3 skip 4 residual + skip, 5 residual + skip+max pooling
        # 1st Layer
        print('--->CNNS2SkipArchitecture')
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

        depth_multiplier = self.config['arch']['depth_multiplier']
        activation = self.config['arch']['activation']


        # 2nd Layer
        drop2 = self.config['arch']['drop2']
        filters2 = self.config['arch']['filters2']
        kernel_size2 = self.config['arch']['kernel_size2']
        # If there is a dilation field and it is true the strides field is the dilation rates
        # and the strides are all 1's
        if 'dilation' in self.config['arch'] and self.config['arch']['dilation']:
            dilation2 = self.config['arch']['strides2']
            strides2 = [1] * len(dilation)
        else:
            strides2 = self.config['arch']['strides2']
            dilation2 = [1] * len(strides2)

        depth_multiplier2 = self.config['arch']['depth_multiplier2']
        activation2 = self.config['arch']['activation2']


        activationfl = self.config['arch']['activation_full']
        fulldrop = self.config['arch']['fulldrop']
        full_layers = self.config['arch']['full']

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
        model = SeparableConv1D(filters[0], input_shape=(idimensions), kernel_size=kernel_size[0], strides=strides[0],
                              padding='same', dilation_rate=dilation[0],depth_multiplier=depth_multiplier,
                              kernel_regularizer=k_regularizer)(input)
        model = generate_activation(activation)(model)
        
        if (tipus != 1) or (tipus != 2):
           residual1 = Conv1D(filters2[0], 1, strides=2, padding= 'valid')(input)
           model = Add()([model, residual1])
        
        if drop != 0:
            model = Dropout(rate=drop)(model)


        model = SeparableConv1D(filters2[0], kernel_size=kernel_size2[0], strides=strides2[0],
                          padding='same', dilation_rate=dilation2[0],depth_multiplier=depth_multiplier2,
                          kernel_regularizer=k_regularizer)(model)
        model = generate_activation(activation2)(model)

        if drop != 0:
            model = Dropout(rate=drop2)(model)
            
        input_pooled = input
        if (tipus == 5):
           input_pooled = MaxPooling1D(pool_size=(2), strides=None, padding='same')(input)
        if (tipus == 1) or (tipus == 3):
           model = Flatten()(model)
        else:
           model = Concatenate()([Flatten()(model), Flatten()(input_pooled)] )
           
        for l in full_layers:
            model= Dense(l)(model)
            model = generate_activation(activationfl)(model)
            if fulldrop != 0:
                model = Dropout(rate=fulldrop)(model)

        output = Dense(odimensions, activation='linear')(model)

        self.model = Model(inputs=input, outputs=output)
          
####  Chollet technique
#        
#        residual = Conv1D(filters[0], 1, strides=2, padding= 'same')(input)#        model = Add()([model, residual])
#        model = Add()([model, residual])
###   fin Chollet technique
#        model = Conv1D(filters2[0], kernel_size=kernel_size2[0], strides=strides2[0],
#                          padding='same', dilation_rate=dilation2[0],
#                          kernel_regularizer=k_regularizer)(model)
#        model = generate_activation(activation2)(model)       
####  Chollet technique
#       residual1 = Conv1D(filters2[0], 1, strides=2, padding= 'same')(input)
#        model = Add()([model, residual1])
#        model = Flatten()(model)
###   find Chollet technique
#        input_pooled = MaxPooling1D(pool_size=(2), strides=None, padding='valid')(input)
#        model = Concatenate()([Flatten()(model), Flatten()(input_pooled)] )


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

