#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 22:03:12 2019

@author: admin
"""

#AlbumDetails Using Functions
#Shakira

def Artist():
    name = "Shakira, Wyclef Jean "
    return name

def Album():
    name = "Hip's Dont Lie"
    return name

def Genre():
    name = "Latin Pop, Salsa"
    return name

def Lyricist():
    name = "Shakira"
    return name

def Duration():
    name = 3.38
    return name

def Boolean(name2):
    name1 = "Shakira"
    Bool = (name1 == name2)
    return Bool


#Calling each function and storing it in a Variable
ArtistName = Artist()
AlbumName = Album()
GenreName = Genre()
LyricistName = Lyricist()
DurationM = Duration()
BooleanV = Boolean("Wyclef Jean")

#Printing the data wich we get using "return" in function
print(ArtistName)
print(AlbumName)
print(GenreName)
print(LyricistName)
print(DurationM)
print(BooleanV)