import numpy as np
from sklearn import linear_model

with open('bcc_large.xyz') as data:
    lines = [line[2:].strip() for line in data.readlines() if line[0]=='A']

lines = [line.replace('  13  ','') for line in lines]
m = len(lines)
X_coord = [line.split()[0] for line in lines]
Y_coord = [line.split()[1] for line in lines]
Z_coord = [line.split()[2] for line in lines]

X_matrix = np.array([X_coord*m],dtype='float')
Y_matrix = np.array([Y_coord*m],dtype='float')
Z_matrix = np.array([Z_coord*m],dtype='float')

X_dist = X_matrix.T - X_matrix
