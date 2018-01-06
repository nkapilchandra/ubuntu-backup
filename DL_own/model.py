import numpy as np
import matplotlib.pyplot as plt
import scipy
import h5py
from helper_functions import *

np.random.seed(1)

train_x_orig, train_y, test_x_orig, test_y, classes = load_data()

m_train = train_x_orig.shape[0]
num_px = train_x_orig.shape[1]
m_test = test_x_orig.shape[0]

train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T
test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

train_x = train_x_flatten/255.
test_x = test_x_flatten/255.

layers_dims = [12288, 20, 7, 5, 1]

parameters = master_model(train_x, train_y, layer_dims = layers_dims, iterations = 3000, print_cost = True)

train_pred = predict(train_x,train_y,parameters)

test_pred = predict(test_x,test_y,parameters)

print("Train Accuracy : " + str(train_pred))
print("Test Accuracy : " + str(test_pred))
