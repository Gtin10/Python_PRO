#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:17:12 2019

@author: admin
"""
# function is created
def funccmp(val1, val2, val3): 
# string type values are converted into int type values
    val1 = int(val1)         
    val2 = int(val2)
    val3 = int(val3)
#if-else function is used
    if val1 == val2 or val1 == val3 or val2 == val3: 
        return True
    else:
        return False


    
#passing values to the function which includes integer as well as string as a parameter
ab = funccmp(6,6,"5") 
print(ab)