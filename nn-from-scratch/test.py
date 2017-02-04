#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:24:28 2017

@author: anvesha
"""
import numpy as np
from nn import neural_net, LossHistory
import os.path
import timeit
import random
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

def generate_data():
    np.random.seed(0)
    X, y = datasets.make_moons(200, noise=0.20)
    return X, y


def train_net(model, params,X,y):    
     history = LossHistory()
     batchSize = params['batchSize']
     buffer = params['buffer']
     model.fit(
                X, y, batch_size=batchSize,
                nb_epoch=1, verbose=0, callbacks=[history]
              )
     loss_log.append(history.losses)
            
            
            










def main():
    X, y = generate_data()
    [a,b]=np.shape(X)
    print(a)
    print('\n')
    print(b)
    nn_param = [50, 50]
    params = {
            "batchSize": 100,
            "buffer": 50000,
            "nn": nn_param
        }
    model = neural_net(a, nn_param)
    train_net(model, params, X,y)


if __name__ == "__main__":
    main()
            