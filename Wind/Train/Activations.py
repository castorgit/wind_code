"""
.. module:: Activations

Activations
*************

:Description: Activations

    

:Authors: HPAI-BSC
    

:Version: 

:Created on: 07/03/2019 12:21 

"""

from keras.layers import Activation
from keras.layers import LeakyReLU, PReLU, ELU

__author__ = 'HPAI-BSC'


def generate_activation(act_par):
    """
    Uses the value in the configuration to generate the activation layer

    :param act_par:
    :return:
    """

    if type(act_par) == list:
        if len(act_par) == 2:
            atype, par = act_par
            if atype == 'elu':
                return ELU(alpha=par)
            elif atype == 'leaky':
                return LeakyReLU(alpha=par)
            elif atype == 'prelu':
                return PReLU()
            else:
                raise NameError("No such Activation layer")
        elif len(act_par) == 1:
            return Activation(act_par[0])
        else:
            raise NameError("No such Activation layer")
    elif type(act_par) == str:
        return Activation(act_par)
    else:
        raise NameError("Wrong parameters for activation layer")

