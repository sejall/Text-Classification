#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:01:42 2019

@author: sejal
"""
import os
import codecs
from sklearn import *

import pickle as p #Pickling is a standard, built-in way of serializing and storing Python objects

def load(clf_file): #define load method #this load method will get mdl file which just saved into memory 
     fp = open(clf_file, 'rb')
     clf = p.load(fp)
     return clf

     
def make_dict():
    direc = "emails/"  #set directory as emails 
    files = os.listdir(direc)  #take all the mails in the directory

    emails = [direc + email for email in files]   #append directory names to the files name #list comprehension


    words= [] #to keep track of all words this list is made

    c = len(emails) #counter initialise to length of all the emails



    for email in emails :
        f= codecs.open(email, "r",encoding='utf-8', errors='ignore') #to open the email
        blob = f.read() #to read the email   
        words += blob.split(" ")#append blob to the list
        print ( c)
        c-= 1
    
    
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""                               #eliminate all alphanumeric words like numbers,hyphens or any symbols   
            dictionary = Counter(words)    #dictionary is an object of class counter having attribute most_common
            del dictionary [""]
            return (dictionary.most_common(3000))   #this print 3000 most common words in our list words[]
clf = load("text-classifier.sav")


d = make_dict()

while True:
    
    
    features = []
    inp = input(">")  #input from the user
    if (inp=="exit"):
        break
    

    for word in d : #make feature vector again
        features.append(inp.count(word[0])) #for every word in dictionary count how many times word occur in input string and append that in features
    
    res = clf.predict([features])

    print(["Not Spam", "Spam!"][res[0]]) #if result is spam it will print 1 otherwise 0 if not spam








