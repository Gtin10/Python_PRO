#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:21:05 2019

@author: admin
"""

#Function FizzBuzz is created
def fizzbuzz():
    
  #For loop is used for iterating the sequence
  for i in range(1,101):
 
  #if condition to check whether i is divisible by 3 as well as 5 , if yes then print "i" as well as "fizzbuzz"
      if i % 3==0 and i % 5==0:
        print(i)
        print ("FizzBuzz")
        continue

 # number divisible by 3, print "i" as well as "Fizz'
      elif i % 3 == 0:
        print(i)
        print ("Fizz")
        continue

 # number divisible by 5, print "i" as well as "Buzz"
      elif i % 5 == 0:
        print(i)
        print ("Buzz")
        continue
 
 # if number divisible by itself as well as 1 print "i" as well as "Prime"    
      elif i % i ==0 and i % 1 ==0:
        print(i)
        print("Prime")
        continue
      
 # print numbers       
      else:
        print(i)
        break
        
ab = fizzbuzz()
    