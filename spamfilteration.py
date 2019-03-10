#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:33:56 2019

@author: sejal
"""




# STEP1 making a dictionary
 

"""to convert text data format to numbers format"""
"""step1 is to make a dictionary to process the emails
read all the mails and put all the words that are encountered into the list
 """ 


import os
import codecs   #to open the email

from collections import Counter  #counter does what exactly we want that is remove duplicates   #To delete duplicate words and to extract most common words
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

import pickle as p

def save(clf,name):
   # with open(name, 'wb') as fp:
   fp = open(name,'wb') #encoding="utf8", errors='ignore'
   p.dump(clf, fp)
   print ("saved")    

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
 
 

    #print (dict)

     
    
 # STEP2 Prepare the dataset


"""feature vectorization used"""

# conversion of email to feature vector


def make_dataset(dictionary):
    direc = "emails/" 
    files = os.listdir(direc)  

    emails = [direc + email for email in files]

    
    feature_set = []
    labels = []
    c = len(emails) 
    for email in emails :
        data = []
        f= codecs.open(email, "r",encoding='utf-8', errors='ignore') 
        words = f.read().split(' ')
        for entry in dictionary :
            data.append(words.count(entry[0]))   #count how many times words occur in the email
        feature_set.append(data)
        if "ham" in email :
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(c)   #printing the tracking variable
        c = c-1
    return feature_set, labels

d = make_dict()
features, labels = make_dataset(d)

#print(len(features), len(labels))

x_train, x_test, y_train, y_test = tts (features, labels, test_size = 0.2) #this function is splitting the dataset into two parts training part and testing part #x_train denotes the features for training,  x_train denotes the features of testing, y_train denotes the corresponding labels for training , y_test denotes the corresponding labels for testing, 20 percent data is used for testing and remaining for training  

clf = MultinomialNB() #make a classifier
clf.fit(x_train, y_train) #fit the classifier with corresponding training features and training labels

preds = clf.predict(x_test) #start making predicitions with the features that kept aside            
        
print(accuracy_score(y_test, preds))  #accuracy score takes two parameters that is true and predictions            
save(clf, "text-classifier.sav",)  
#with this , classifier is trained ,now real life implementation of filtering of spam messages will be done 

















   

    


    






    

    
    
    
    

