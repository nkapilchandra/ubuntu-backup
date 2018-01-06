import numpy as np
import matplotlib.pyplot as plt
import scipy
import h5py

def initialize_helper(layer_dims):
    np.random.seed(1)
    parameters = {}
    l = len(layer_dims)

    for i in range(1,l):
        parameters['W' + str(i)] = np.random.randn(layer_dims[i],layer_dims[i-1])/np.sqrt(layer_dims[i-1]) #*0.01
        parameters['b' + str(i)] = np.zeros((layer_dims[i],1))

        assert(parameters['W' + str(i)].shape == (layer_dims[i],layer_dims[i-1]))
        assert(parameters['b' + str(i)].shape == (layer_dims[i],1))

    return parameters

def sigmoid(z):
    return (1/(1+np.exp(-z)))

def relu(z):
    return (z + np.absolute(z))/2

def forward_prop_helper(A_prev, W, b, activation):
    Z = np.dot(W,A_prev) + b

    if activation == 'sigmoid':
        A = sigmoid(Z)
    elif activation == 'relu':
        A = relu(Z)
    elif activation == 'tanh':
        A = np.tanh(Z)

    assert(A.shape == (W.shape[0],A_prev.shape[1]))

    cache = (Z,A_prev,W,b)

    return A,cache

def model_forward(X,parameters):

    L = len(parameters)//2
    A = X
    caches = []

    for l in range(1,L):
        A_prev = A
        A,cache = forward_prop_helper(A_prev,parameters['W'+str(l)],parameters['b' + str(l)],'relu')
        caches.append(cache)

    AL, cache = forward_prop_helper(A,parameters['W' + str(L)],parameters['b' + str(L)],'sigmoid')
    caches.append(cache)

    assert(AL.shape == (1,X.shape[1]))

    return AL, caches

def cost_helper(AL,Y):
    m = Y.shape[1]

    cost = -1/m*np.sum((np.multiply(Y,np.log(AL)) + np.multiply(1-Y,np.log(1-AL))))

    cost = np.squeeze(cost)
    assert(cost.shape == ())

    return cost

def relu_backward(dA,Z):

    def relu_der(x):
        k = np.copy(x)
        np.putmask(k,k>=0,1)
        np.putmask(k,k<0,0)
        return k

    return np.multiply(dA,relu_der(Z))

def sigmoid_backward(dA,Z):

    def sigmoid_der(x):
        der = np.exp(-x)/(1+np.exp(-x))**2
        return der

    return np.multiply(dA,sigmoid_der(Z))

def linear_backward(dZ,cache):
    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = 1/m*(np.dot(dZ,A_prev.T))
    db = 1/m*np.sum(dZ,axis=1,keepdims=True)
    dA_prev = np.dot(W.T,dZ)

    assert (dA_prev.shape == A_prev.shape)
    assert (dW.shape == W.shape)
    assert (db.shape == b.shape)

    return dA_prev, dW, db

def backward_prop_helper(dA, cache, activation):

    Z, A_prev, W, b = cache
    small_cache = (A_prev,W,b)

    if activation == 'relu':
        dZ = relu_backward(dA,Z)
        dA_prev, dW, db = linear_backward(dZ,small_cache)
    elif activation == 'sigmoid':
        dZ = sigmoid_backward(dA,Z)
        dA_prev, dW, db = linear_backward(dZ,small_cache)

    return dA_prev, dW, db

def model_backward(AL, y, caches):

    grads = {}
    L = len(caches)
    m = AL.shape[1]
    y = y.reshape(AL.shape)

    dAL = -(np.divide(y,AL) - np.divide(1-y,1-AL))

    current_cache = caches[L-1]
    grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = backward_prop_helper(dAL, current_cache,'sigmoid')

    for l in reversed(range(L-1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = backward_prop_helper(grads['dA'+str(l+2)],current_cache,'relu')
        grads["dA" + str(l + 1)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp

    return grads

def update_parameters(parameters,grads,learning_rate):

    L = len(parameters)//2

    for l in range(L):
        parameters['W'+str(l+1)] -= learning_rate*grads['dW'+str(l+1)]
        parameters['b'+str(l+1)] -= learning_rate*grads['db'+str(l+1)]

    return parameters

def master_model(X,y,layer_dims,learning_rate=0.0075,iterations=3000,print_cost=False):
    np.random.seed(1)
    costs = []

    parameters = initialize_helper(layer_dims)

    for i in range(iterations):

        # Forward propagation step
        AL, caches = model_forward(X,parameters)

        # Cost computation step
        cost = cost_helper(AL,y)

        # Back propagation step
        grads = model_backward(AL,y,caches)

        # Updating parameters
        parameters = update_parameters(parameters,grads,learning_rate)

        if print_cost and i%100 == 0:
            print("Cost after %d iteration = %f"%(i,cost))
        if i%100 == 0:
            costs.append(cost)

    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()

    return parameters

def load_data():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

def predict(X,y,parameters):
    m = X.shape[1]
    n = len(parameters) // 2
    p = np.zeros((1,m))

    probas, caches = model_forward(X, parameters)

    for i in range(0, probas.shape[1]):
        if probas[0,i] > 0.5:
            p[0,i] = 1
        else:
            p[0,i] = 0
    print("Accuracy: "  + str(np.sum((p == y)/m)))

    return np.sum((p == y)/m)
