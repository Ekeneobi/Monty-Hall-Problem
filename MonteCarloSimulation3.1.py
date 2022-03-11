# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:01:10 2020
@author: Ekene Obi
Student Id: 31-03-030-20-2
Email: ekene.obi.2020@student.ism.de
"""


'''
Question 3.1.
Script a Monte Carlo Simulation that allows the user to estimate the area under any given
function between any two points over a positive area. Compare your simulation results with the
actual area under the standard normal density, as a test function. Show the development of the
error rate over the number of simulations (n = 100, 200, …, 10.000). Solve this task by using
object orientated programming (OOP). Therefore, define a class object MonteCarloSim() which
suffices the following UML diagram.
'''

import numpy as np   
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
a = 0  # select base and height interval
b = 5   # select base and height interval


def myFun(x):   #define your own standard normal density function
    return ((1/np.sqrt(2*np.pi) ) * np.exp(-0.5*((x)**2)))

def rand_num(a,b):  #Creates a random number between two float variables
    range = b - a
    choice = random.uniform(0,1)
    return a + range*choice

def MonteCarloSim(nTrials):
    #create a monte Carlo simulation with default values 

    total_samples = 0
    for i in range(nTrials):
        x = rand_num(a, b)
        total_samples += myFun(x) 
    return ((b - a) * float(total_samples/nTrials))

def MonteCarloSim1(nTrials):
    #create a monte Carlo simulation with default values 

    total_samples = 0
    for i in range(nTrials):
        x = rand_num(a, b)
        total_samples += testFun(x)
    return ((b - a) * float(total_samples/nTrials))

def testFun(x):
    return stats.norm.pdf(x) #Use the standard normal density as test function

def testArea(x):   #Use the cumulative standard normal distribution values as test area
    return stats.norm.cdf(x)

def main():
    h = 1
    print (testFun(h), "Here is Standard distribution function")
    print (myFun(h),"here is My test function")
    print (MonteCarloSim (1000),"Here is MCS using my test function for 1000 trials")
    print (MonteCarloSim (10),"Here is MCS using testfun for 10 trials")
    print (MonteCarloSim1 (10000),"Here is MCS using my test function for 1000 trials")
    print (MonteCarloSim1 (10),"Here is MCS using testFun for 10 trials")
    
    #create a comprehensive list containing simulation
    list = [] #empty list
    n = 100  #count from 100
    for n in range (100,10001,100): #range 100,200 ...1000 step  100
        list.append(MonteCarloSim(n))
        n += 100     #add continously to the list in 100 increament
    print (list, "here is the MCS results appened to list")
    G =   np.mean(list)   # store the mean of list in a variable
    print (G, "is the mean")
    
    #deviation is absolute value of (X - mean) for each element of the list
    np.array(list)
    list2 = abs(list  - G)
    print (list2 ,"this is the error list")
   
    # x axis values 
    x = range(100,10001,100) 
    # corresponding y axis values 
    y = list2
  
    # plotting the points  
    plt.plot(x, y) 
    
    plt.ylim(-0.05,0.05) 
    plt.xlim(100,10000)
  
    # naming the x axis 
    plt.xlabel('no. of simulations') 
    # naming the y axis 
    plt.ylabel('deviations') 
  
    # giving a title to my graph 
    plt.title('Error analysis') 
  
    # function to show the plot 
    plt.show() 
    
main()
    
