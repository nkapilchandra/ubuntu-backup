import random
from scipy.optimize import rosen as rf
import numpy as np

def rosenbrock(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

def sim_anneal(f,x0,tol,alpha):
    T = 1.0
    ran_x = x0[0]
    ran_y = x0[1]
    cost = f([ran_x,ran_y])
    count = 0
    new_cost = 2000000
    #abs(new_cost-cost)>tol
    while (count < 10):
        print('new cost = ',new_cost,'old cost = ',cost)
        del_x = random.uniform(-2,2)
        del_y = random.uniform(-2,2)
        cost = f([ran_x,ran_y])
        ran_x_new = ran_x + del_x
        ran_y_new = ran_y + del_y
        new_cost = f([ran_x_new,ran_y_new])
        if new_cost < cost:
            ran_x, ran_y = ran_x_new,ran_y_new
        else:
            P = np.exp(-(new_cost-cost)/(alpha*T))
            r = random.random()
            if (P>r):
                ran_x,ran_y = ran_x_new,ran_y_new
            else:
                pass
        if (count%1 == 0):
            T = alpha*T
            print(count)

        count += 1

    print([ran_x,ran_y])

sim_anneal(rosenbrock,[0,0],0.0001,0.8)
