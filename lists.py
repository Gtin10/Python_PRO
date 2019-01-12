#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:19:12 2019

@author: admin
"""
#creating two empty list
myUniqueList =[]
myLeftovers =[]

#creating function and passing values into the list using num
def func(num):
    #global variables
   global myUniqueList
   global myLeftovers
   """
   if num in the list is unique it should be added in the unique list and should  return true 
   or else should be added in leftover list and return false
   """
   if num in myUniqueList:
       myLeftovers.append(num)
       return False
   else:
       myUniqueList.append(num)
       return True
   
      
    
    
    
    
    

ab= func(20)              #passng value 20 from func into the list #Unique Value
print(myUniqueList)
print(myLeftovers)
print(ab)

ab = func(40)            #Unique Value
print(myUniqueList)
print(myLeftovers)
print(ab)

ab = func(10)             #Unique Value
print(myUniqueList)
print(myLeftovers)
print(ab)

ab = func(20)             #Unique Value
print(myUniqueList)
print(myLeftovers)
print(ab)
    