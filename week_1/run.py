
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
        temp = i*num
        sum += temp
    return sum
def rosenBrock(x):
    sum = 0
    for i,num in enumerate(x):
        temp = 100*(x[i+1]-num*num)*(x[i+1]-num*num) + (1-num)*(1-num)
        sum += temp
    return sum

def ackley(x):
    sum1 = 0
    sum2 = 0
    for i,num in enumerate(x):
        tem1 = num*num
        temp2 = math.cos(2*x*math.pi)

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
        sum2 = sum2*math.cos(num/math.sqrt(i))
        sum1 += temp1
    return 1 + sum1 - sum2

dim = int(input("dim="))
while True:
    x = [random.uniform(-5.12,5.12) for i in range(dim)]
    print(x)
    y1 = ellipsoid(x)
    print(y1)
    x = [random.uniform(-2.048,2.048) for i in range(dim)]
    y2 = rosenBrock(x)
    time.sleep(10)
    

