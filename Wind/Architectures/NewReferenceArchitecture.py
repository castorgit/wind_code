"""
.. module:: NewReferenceModel

New Reference Model
******

:Description: NewReferenceModel

    Class for New Reference model

:Authors:
    jm

:Version: 

:Date:  25/01/2019
"""

from Wind.Architectures.Architecture import Architecture
from sklearn.metrics import r2_score
import numpy as np

__author__ = 'HPAI-BSC'


class NewReferenceArchitecture(Architecture):
    """Class for NewReferenceArchitecture

    """
    ## Data mode default for input, 1 dimensional output
    data_mode = (False, '1D')

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
        """
        Model summary
        :return:
        """
        print("New Reference Model")

    def evaluate(self, val_x, val_y, test_x, test_y):
        """
        Evaluates the training
        :return:
        """
        print("2",val_x[1,-1])
        r2val = r2_score(val_x[:, -1], val_y[:, 0])
        r2test = r2_score(test_x[:, -1], test_y[:, 0])

        return r2val, r2test


