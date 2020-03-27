import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def vertice_init(vertex_0, step_length):
    '''
    initialize vertice of the simplex
    using the following formula:
    $xi=x0+step_length*ei$
    '''

    emat = np.eye(vertex_0.size) * step_length
    vertice = [vertex_0]
    for ii in range(vertex_0.size):
        vertice.append(vertex_0 + emat[:, ii])
    return vertice


# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math
def ellipsoid(x):
    sum = 0
    for i,num in enumerate(x):
        temp = (i+1)*num
        sum += temp
    return sum
def rosenBrock(x):
    sum = 0
    for i,num in enumerate(x):
        if(i<x.size-1):
            
            temp = 100*(x[i+1]-num*num)*(x[i+1]-num*num) + (1-num)*(1-num)
            sum += temp

    return sum

def ackley(x):
    sum1 = 0
    sum2 = 0
    for i,num in enumerate(x):
        temp1 = num*num
        temp2 = math.cos(2*num*math.pi)

        sum1 += temp1
        sum2 += temp2
    sum1 = sum1/len(x)
    sum2 = sum2/len(x)
    return math.exp(math.sqrt(sum1)*(-0.2))*(-20) - math.exp(sum2)
def griewank(x):
    sum1 = 0
    sum2 = 1
    for i,num in enumerate(x):
        temp1 = num*num/4000
        sum2 = sum2*math.cos(num/math.sqrt((i+1)))
        sum1 += temp1
    return 1 + sum1 - sum2

#dim = int(input("dim="))
#while True:
#x = [random.uniform(-5.12,5.12) for i in range(dim)]
#print(x)
#y1 = ellipsoid(x)
#print(y1)
#$#x = [random.uniform(-2.048,2.048) for i in range(dim)]
#y2 = rosenBrock(x)
#time.sleep(10)



def f(v):
    '''
    Evaluation of Function $f$
    '''
    dim = v.size
    v0 = np.ones(dim) * 5
    v1 = np.ones(dim) * 3
    return 0.5 * np.dot(v - v0, v - v1)


def line(t, v1, v2):
    return (1 - t) * v1 + t * v2
def simplex(f, vertice, maxit=1000, step_length=100, tol=1e-3):
    vertice_max_list = []  # store the max vertex during each iteration
    vertice_min_list = []  # store the min vertex during each iteration
    for jj in range(maxit):
        y = []
        for ii in vertice:
            y.append(f(ii))
        y = np.array(y)
        #  only the highest (worst), next-highest, and lowest (best) vertice
        # are neeed
        idx = np.argsort(y)
        vertice_max_list.append(vertice[idx[-1]])
        vertice_min_list.append(vertice[idx[0]])
        
        # centroid of the best n vertice
        # NOTE: the worst vertex should be excluded, but for simplicity we don't do this
        v_mean = np.mean(vertice)

        # compute the candidate vertex and corresponding function vaule
        v_ref = line(-1, v_mean, vertice[idx[-1]])
        y_ref = f(v_ref)
        if y_ref >= y[idx[0]] and y_ref < y[idx[-2]]:
            # y_0<=y_ref<y_n, reflection (replace v_n+1 with v_ref)
            vertice[idx[-1]] = v_ref
            # print('reflection1')
        elif y_ref < y[idx[0]]:
            # y_ref<y_0, expand
            v_ref_e = line(-2, v_mean, vertice[idx[-1]])
            y_ref_e = f(v_ref_e)
            if y_ref_e < y_ref:
                vertice[idx[-1]] = v_ref_e
                # print('expand')
            else:
                vertice[idx[-1]] = v_ref
                # print('reflection2')
        elif y_ref >= y[idx[-2]]:
            if y_ref < y[idx[-1]]:
                # y_ref<y_{n+1}, outside contraction
                v_ref_c = line(-0.5, v_mean, vertice[idx[-1]])
                y_ref_c = f(v_ref_c)
                if y_ref_c < y_ref:
                    vertice[idx[-1]] = v_ref_c
                # print('outside contraction')
            else:
                # y_ref>=y_{n+1} inside contraction
                v_ref_c = line(0.5, v_mean, vertice[idx[-1]])
                y_ref_c = f(v_ref_c)
                if y_ref_c < y_ref:
                    vertice[idx[-1]] = v_ref_c
                    # print('inside contraction')
                    continue
            # shrinkage
                for ii in range(1, len(vertice)):
                    vertice[ii] = 0.5 * (vertice[0] + vertice[ii])
                    #print('shrinkage')
                vertice = vertice_init(vertice[idx[0]], step_length)
        # restart
        # restarting is very important during iteration, for the simpex
        # can easily stucked into a nonoptimal point
        rtol = 2.0 * abs(y[idx[0]] - y[idx[-1]]) / (
            abs(y[idx[0]]) + abs(y[idx[-1]]) + 1e-9)
        if rtol <= tol:
            vertice = vertice_init(vertice[idx[0]], step_length)
    return vertice_max_list, vertice_min_list

dim = 5
step_length = 5
v = np.random.randn(dim)
vertice = vertice_init(v, step_length)  # the chioce of step length is cruical

vertice_max_list, vertice_min_list = simplex(
    rosenBrock, vertice, maxit=2000, step_length=step_length, tol=1e-5)
print('min value is %s' % f(vertice_min_list[-1]))