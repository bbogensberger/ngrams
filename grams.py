'''
trying to impliment jut a ngram gnerator
'''
import random
import re
import sys
import pandas as pd
from nltk.corpus import brown


def getData():
    outLst = [] 
    fileIn = open("s0205b.txt") 
    sent = fileIn.read()
    sent = re.sub(r'<[^>]+','',sent)
    sent = re.sub(r'>','',sent)
    #sentences = brown.words(categories='news')
    #print sentences
    lst= tokenize(sent)
    #print lst
    return lst

def tokenize(sent):
    punctLst = [',', ';', ':',')', '(', '?', '!', '.', '""', "''","``", '"', "'",'\n', '  ']
    words=''
    for word in sent:
        newSent = filter(lambda token: token not in punctLst, word)
        newSent = newSent.lower()
        words = words+newSent
    
    return words

def word_gen(words):
    letters = ''
    wo=[]
    for i in words:
        if(i!= ' '):
            letters = letters+i
        else:
            wo.append(letters)
            letters = ''
    return wo

def tok_words(grams):
    lis=[]
    for i in grams:
        if(i!=''):
            lis.append(i)
    print lis
    return lis

def gram_gen(words, gramSize):
    gram=[]
    if gramSize == 1:
        return words
    if gramSize ==2:
        for i in range(len(words)-1):
            gram.append((words[i], words[i+1]))
        return gram
    if gramSize ==3:
        for i in range(len(words)-2):
            gram.append((words[i], words[i+1], words[i+2]))
        return gram
    if gramSize ==4:
        for i in range(len(words)-3):
            gram.append((words[i], words[i+1], words[i+2], words[i+3]))
        return gram

def gram_dict(grams):
    d = {}
    for i in grams:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
    return d

def freqTable(grams):
    dataOut=open('dataOut.txt','w')
    #lines = [line.strip() for line in grams if line.strip() and not line.startswith('com')]
    lineSer = pd.Series(grams)
    freq =lineSer.value_counts()
    freq.to_csv('dataOut.txt')
    with pd.option_context('display.max_rows',999):
        print freq
    
        
