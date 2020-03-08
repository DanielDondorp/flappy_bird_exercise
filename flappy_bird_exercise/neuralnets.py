#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:25:45 2020

@author: daniel
"""

import tensorflow as tf
from tensorflow import keras

class NeuralNet:
    def __init__(self, model = None):
        if model == None:
            self.model = self.make_cnn()    
        
    def make_cnn(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(4, input_dim = 5, kernel_initializer = "random_uniform", activation = "relu"))
        model.add(keras.layers.Dense(1, kernel_initializer = "random_uniform", activation = "sigmoid"))      
        return model
    
    
