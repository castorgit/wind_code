"""
.. module:: __init__.py

__init__.py
*************

:Description: __init__.py

    

:Authors: HPAI-BSC
    

:Version: 

:Created on: 06/07/2018 7:53 

"""

from .TrainDispatch import TrainDispatch
from Wind.Train.TrainingProcess import train_dirregression, train_persistence, train_sequence2sequence, train_sckit_dirregression
from .RunConfig import RunConfig

__author__ = 'HPAI-BSC'


__all__ = ['TrainDispatch',
           'RunConfig',
           'train_persistence', 'train_dirregression', 'train_sequence2sequence', 'train_sckit_dirregression']
