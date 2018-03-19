# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 09:58:02 2018

This is a simple program to predict the species of the iris flowers using K-nearest neighbour

@author: Sylvia Achach
"""
import random
from math import sqrt 
from collections import Counter
#retrieve the file and put in a list
irisPath=("C:/Users/SA/Desktop/comp improvement/data science/Iris.csv")
irisFile = open(irisPath,"r")
iris = []
for r in irisFile:
    r = r.split(',')
    iris.append(r)
#remove the first row which is the title
del iris[0]    

#splitting it into training and testing data using the ratio of 4:1
irisShuffle = iris
random.shuffle(irisShuffle)

for s in range (0,len (irisShuffle)):
    irisShuffle[s][0]=int(irisShuffle[s][0])
    irisShuffle[s][1]=float(irisShuffle[s][1])
    irisShuffle[s][2]=float(irisShuffle[s][2])
    irisShuffle[s][3]=float(irisShuffle[s][3])
    irisShuffle[s][4]=float(irisShuffle[s][4])
        
train = []
test = []
for i in range(0,len (irisShuffle)):
    if i <= ((len (irisShuffle))//5)*4:
        train.append(irisShuffle[i])
    else:
        test.append(irisShuffle[i])
    
#get neighbours
def getNeighbours (testinstance,train,k):
    def foreachinstance(traininstance):
            return sqrt(sum((a-b)**2 for a,b in zip(traininstance[1:5],testinstance[1:5])))
    return sorted(train,key = foreachinstance)[:k]
 
#vote on neighbours
def predict(neighbours_species):
    countNeighbours = Counter(neighbours_species)
    return max(countNeighbours, key = countNeighbours.get) 
    #incase of a tie max returns the first one
    
#let's start our classifier
for k in range (1,7):   
    correct_predictions = 0
    for testinstance in test:
        #first get the neighbours
        _,_,_,_,_,neighbours_species = zip(*(getNeighbours(testinstance,train,k)))
        #predict the neighbours
        prediction = predict(neighbours_species)
        if (prediction == testinstance[5]):
            correct_predictions += 1
        
    print("accuracy for ",k,"-nearest neighbours is: ",(correct_predictions/len(test)))




