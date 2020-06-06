"""
.. module:: CNNS2SDreamTimeArchitecture

CNNS2SCrazyIvanArchitecture
*************

:Description: CNNS2SDreamTimeArchitecture

    Loosely resemblant to CrazyIvan

      - Based on arXiv:1909.04939 / GiHub: https://github.com/hfawaz/DreamTime

:Version: 

:Created on: 14/09/2019

"""

__author__ = 'HPAI-BSC'


from Wind.Architectures.NNS2SArchitecture import NNS2SArchitecture
from keras.models import Sequential, load_model, Model
from keras.layers import Dense, Dropout, Conv1D, Flatten, Concatenate, Input, MaxPool1D,GlobalAveragePooling1D,SeparableConv1D
                        
from sklearn.metrics import r2_score
from Wind.Train.Activations import generate_activation

from keras.regularizers import l1, l2

__author__ = 'HPAI-BSC'


class CNNS2SDreamTimeArchitecture(NNS2SArchitecture):
    """
    Class for Multiple head convolutional sequence to sequence architecture

    """
    modfile = None
    modname = 'CNNCIS2S'
    data_mode = ('3D', '2D') #'cnn'

    def generate_model(self):
        """
        Model for CNN with Encoder Decoder for S2S

        json config:

        "arch": {
            "bottleneck_filters": [256,256,0],
            "bottleneck_activation": [["elu",0.2], ["elu",0.2],["elu",0.2]],
            "inception_filters: [20,20,20]
            "inception_kernels":[[3,5,7],[3,3,3],[5,7,9]],
            "inception_activation":[["elu",0.2], ["elu",0.2],["elu",0.2]],
            "shortcut":[True,True,True]
            "inception_drop": [0.3,0.3,0.3]
            "dilation": false,
            "kernel_size": 3,   
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
        kernel_size = self.config['arch']['kernel_size']
        if type(kernel_size) != list:
            raise NameError('kernel size must be a list')
        elif len(kernel_size) < 1:
            raise NameError('kernel size list must have more than one element')

#        strides = self.config['arch']['strides']

        activationfl = self.config['arch']['activation_full']
        fulldrop = self.config['arch']['fulldrop']
        full_layers = self.config['arch']['full']

        activation = self.config['arch']['activation']

        k_reg = self.config['arch']['k_reg']
        k_regw = self.config['arch']['k_regw']
        
        #inception architecture parameters
        bottleneck_filters = self.config['arch']['bottleneck_filters']
        bottleneck_activation = self.config['arch']['bottleneck_activation']
        inc_filters = self.config['arch']['inception_filters']
        inc_kernels = self.config['arch']['inception_kernels']
        inc_act = self.config['arch']['inception_activation']
        inc_shortcut = self.config['arch']['shortcut']
        inc_drop = self.config['arch']['inception_drop']

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
        inc_tensor = input
        r = 0
        i = 0
        for k in inc_filters:                   # len(inc_filters)=number 
           print("-->k ",k)
           if bottleneck_filters[i] !=0:      #Create Bottleneck?
              print("conv1d bottleneck -->",r," filters, activation ", bottleneck_filters[i], bottleneck_activation[i])
              r = r + 1
              bottleneck_tensor = SeparableConv1D(filters=bottleneck_filters[i], kernel_size=1,
                               padding='same', use_bias=False)(inc_tensor)
              bottleneck_tensor = generate_activation(bottleneck_activation[i])(bottleneck_tensor)
              bottleneck_tensor = Dropout(rate=0.0)(bottleneck_tensor)
           else:
              bottleneck_tensor = inc_tensor
           lconv = [] 
           
           for j in range(0,3):
              print("conv1d -->",r, k, inc_kernels[i][j], )
              r = r+1
        
              inc_layer = SeparableConv1D(k, kernel_size=inc_kernels[i][j], strides=1,
                              padding='same', kernel_regularizer=k_regularizer)(bottleneck_tensor)
              inc_layer = generate_activation(activation)(inc_layer)
              print('drouput:',inc_drop[i])
              if inc_drop[i] != 0:
                 print('drouput:',inc_drop[i])
                 inc_layer = Dropout(rate=inc_drop[i])(inc_layer)
              lconv.append(inc_layer)
              
           max_pool1 = MaxPool1D(pool_size=3, strides=1, padding='same')(bottleneck_tensor)
           max_pool1 = SeparableConv1D(filters=32, kernel_size=1,
                                     padding='same', use_bias=False)(max_pool1)     
           max_pool1 = generate_activation(activation)(max_pool1)
           lconv.append(max_pool1)
        
           inc_tensor = Concatenate(axis=2)(lconv)
           i = i + 1
#        x = BatchNormalization()(x)
#        x = generate_activation(["elu",0.2])(x)
#        gap_layer = GlobalAveragePooling1D()(inc_tensor)
#        gap_layer = tensor
#      convoout = Concatenate()(x)

        fullout = Dense(full_layers[0])(inc_tensor)
        fullout = generate_activation(activationfl)(fullout)
        fullout = Dropout(rate=fulldrop)(fullout)

        for l in full_layers[1:]:
            fullout = Dense(l)(fullout)
            fullout = generate_activation(activationfl)(fullout)
            fullout = Dropout(rate=fulldrop)(fullout)

        fullout = Flatten()(fullout)

        output = Dense(odimensions, activation='linear')(fullout)

        self.model = Model(inputs=input, outputs=output)
