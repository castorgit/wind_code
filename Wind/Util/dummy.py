"""
.. module:: SelfAttention

SelfAttention
*************

:Description: SelfAttention

    

:Authors: Borrowed from Marc Nuth Github https://github.com/Marcnuth/keras-attention
    

:Version: 

:Created on: 17/06/2019 13:46 

"""

__author__ = 'HPAI-BSC'


from keras.layers import Layer
from keras import initializers
from keras import backend as K


class SelfAttention(Layer):
    def __init__(self, regularizer=None, attention_width=12, **kwargs):
        super(SelfAttention, self).__init__(**kwargs)
        self.regularizer = regularizer
        self.attention_width = attention_width
        self.supports_masking = True

    def build(self, input_shape):
        feature_dim = int(input_shape[2])
        self.Wa = self.add_weight(name='Wa',
                                       shape=(input_shape[-1], 1),
                                       initializer=initializers.RandomNormal(mean=0.0, stddev=0.05, seed=None),
                                       regularizer=self.regularizer,
                                       trainable=True)
        
        super(SelfAttention, self).build(input_shape)

    def call(self, x, mask=None):
                 
        # e_{t, t'} = x_t^T W_a x_{t'} + b_a
        e = K.batch_dot(K.dot(x, self.Wa), K.permute_dimensions(inputs, (0, 2, 1)))
        
        lower = K.arange(0, input_len) - (self.attention_width - 1)
        lower = K.expand_dims(lower, axis=-1)
        upper = lower + self.attention_width
        indices = K.expand_dims(K.arange(0, input_len), axis=0)
        e = e * K.cast(lower <= indices, K.floatx()) * K.cast(indices < upper, K.floatx())      
        
        # a_{t} = \text{softmax}(e_t)
        s = K.sum(e, axis=-1, keepdims=True)
        a = e / (s + K.epsilon())

        # l_t = \sum_{t'} a_{t, t'} x_{t'}
        v = K.batch_dot(a, x)

        return v


      
        attention_flat = K.exp( K.squeeze(K.dot(x,self.context), axis=-1) )
        attention2 = attention_flat /K.expand_dims(K.sum(attention_flat, axis=-1), -1)

        print('--- shapes: ', K.shape(x), K.shape(self.context))
        print('... shape k.dot', K.shape(K.dot(x, self.context)))
        print('... shape k.squezze', K.shape(K.squeeze(K.dot(x, self.context), axis=-1)))
        print('... shape k.exp', K.shape(K.exp(K.squeeze(K.dot(x, self.context), axis=-1))))

        if mask is not None:
            attention = attention * K.cast(mask, 'float32')

#        weighted_sum = K.batch_dot(K.permute_dimensions(x, [0, 2, 1]), attention)
        
        # multiplicative
        
        weighted_sum = K.batch_dot(K.permute_dimensions(x, [0, 2, 1]), attention2)
#       
        return weighted_sum

    def compute_output_shape(self, input_shape):
        return (input_shape[0], input_shape[-1])

    def compute_mask(self, input, input_mask=None):
        return None
    
    @staticmethod
    def get_custom_objects():
        return {'SelfAttention': SelfAttention}

