"""
.. module:: CNNS2SCrazyIvan2HArchitecture

CNNS2SCrazyIvanArchitecture
*************

:Description: CNNS2SCrazyIvanArchitecture

    Imaginative versions of CNN

      - First try "a la inception" with multiple heads using different kernel sizes 2 Heads

:Authors: HPAI-BSC
    

:Version: 

:Created on: 25/03/2019 16:31 

"""

__author__ = 'HPAI-BSC'


from Wind.Architectures.NNS2SArchitecture import NNS2SArchitecture
from keras.models import Sequential, load_model, Model
from keras.layers import Dense, Dropout, Conv1D, Flatten, Concatenate, Input
from sklearn.metrics import r2_score
from Wind.Train.Activations import generate_activation

from keras.regularizers import l1, l2

__author__ = 'HPAI-BSC'


class CNNS2SCrazyIvan4HArchitecture(NNS2SArchitecture):
    """
    Class for Multiple head convolutional sequence to sequence architecture

    """
    modfile = None
    modname = 'CNNCI3HS2S'
    data_mode = ('3D', '2D') #'cnn'

    def generate_model(self):
        """
        Model for CNN with Encoder Decoder for S2S

        json config:

        "arch": {
            "filters": 32,
            "strides": 1,
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
        # 1st head
        drop = self.config['arch']['drop']
        filters = self.config['arch']['filters']
        kernel_size = self.config['arch']['kernel_size']
        if type(kernel_size) != list:
            raise NameError('kernel size must be a list')

        strides = self.config['arch']['strides']

        # 2nd head
        drop2 = self.config['arch']['drop2']
        filters2 = self.config['arch']['filters2']
        kernel_size2 = self.config['arch']['kernel_size2']
        if type(kernel_size2) != list:
            raise NameError('kernel size must be a list')

        strides2 = self.config['arch']['strides2']

        # 3rd head
        drop3 = self.config['arch']['drop3']
        filters3 = self.config['arch']['filters3']
        kernel_size3 = self.config['arch']['kernel_size3']
        if type(kernel_size3) != list:
            raise NameError('kernel size must be a list')
            
        strides3 = self.config['arch']['strides3']
            
        # 4th  head
        drop4 = self.config['arch']['drop4']
        filters4 = self.config['arch']['filters4']
        kernel_size4 = self.config['arch']['kernel_size4']
        if type(kernel_size4) != list:
            raise NameError('kernel size must be a list')
        strides4 = self.config['arch']['strides4']


        activation = self.config['arch']['activation']

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

        lconv = []

        # 1st head
        convomodel = Conv1D(filters[0], input_shape=(idimensions), kernel_size=kernel_size, strides=strides[0],
                          padding='causal', kernel_regularizer=k_regularizer)(input)
        convomodel = generate_activation(activation)(convomodel)

        if drop != 0:
            convomodel = Dropout(rate=drop)(convomodel)
        lconv.append(Flatten()(convomodel))

        # 2nd head
        convomodel = Conv1D(filters2[0], input_shape=(idimensions), kernel_size=kernel_size2, strides=strides2[0],
                          padding='causal', kernel_regularizer=k_regularizer)(input)
        convomodel = generate_activation(activation)(convomodel)

        if drop2 != 0:
            convomodel = Dropout(rate=drop2)(convomodel)
        lconv.append(Flatten()(convomodel))

        # 3rd head
        convomodel = Conv1D(filters3[0], input_shape=(idimensions), kernel_size=kernel_size3, strides=strides3[0],
                          padding='causal', kernel_regularizer=k_regularizer)(input)
        convomodel = generate_activation(activation)(convomodel)
        
        if drop3 != 0:
            convomodel = Dropout(rate=drop3)(convomodel)
        lconv.append(Flatten()(convomodel))


        # 4th head
        convomodel = Conv1D(filters4[0], input_shape=(idimensions), kernel_size=kernel_size4, strides=strides4[0],
                          padding='causal', kernel_regularizer=k_regularizer)(input)
        convomodel = generate_activation(activation)(convomodel)

        if drop4 != 0:
            convomodel = Dropout(rate=drop4)(convomodel)
        lconv.append(Flatten()(convomodel))

        convoout = Concatenate()(lconv)
        fullout = Dense(full_layers[0])(convoout)
        fullout = generate_activation(activationfl)(fullout)
        fullout = Dropout(rate=fulldrop)(fullout)

        for l in full_layers[1:]:
            fullout = Dense(l)(fullout)
            fullout = generate_activation(activationfl)(fullout)
            fullout = Dropout(rate=fulldrop)(fullout)

        #fullout = Flatten()(fullout)

        output = Dense(odimensions, activation='linear')(fullout)

        self.model = Model(inputs=input, outputs=output)
