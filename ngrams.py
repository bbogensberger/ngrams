'''
This file contains the funtions to generate and display the ngrams
    some changes were made
'''
import nltk
from nltk.corpus import brown
import random
import re
import sys
from dict_gen import *
from unigram import *

'''
post: returns a list of sentences, each of which is a list of words
'''
def getData(data, rawDataSize):
    if data == 't': #test data 
        outLst = []
        #simple file in home directory.  N-grams are easily calculated
        #fileIn = open("dataIn.dat") 
        fileIn = open("dataIn1.dat") 
        sentences = fileIn.readlines()
        for sentence in sentences:
            sentence = sentence.rstrip()
            sentence = '<s> ' + sentence + ' </s>'
            sentLst = sentence.split()
            outLst.append(sentLst)    
        return (tokenize(outLst))       #need to tokenize test date so all lower
    else:
        #Real data
        #Editorials tokenized through nltk from the Brown corpus and represented
        #as a list of sentences, each of which is a list of words
        sentLst = brown.sents(categories='editorial')
        newSentLst = []
        for i in range(rawDataSize):
            newSentLst.append(sentLst[i])
        return (tokenize(newSentLst))

def genNgrams(numLines,gramsPerLine, ngramSize,ngramNestedDict, ngramFreqDict):
    if ngramSize == 2:
        print ("---------------------BIGRAMS----------------------")
    if ngramSize == 3:
        print ("---------------------TRIGRAMS----------------------")
    if ngramSize == 4:
        print ("---------------------QUADGRAMS----------------------")

    
    #first line    
    prefix = findFirstPrefix('<s>', ngramFreqDict)
    line = prefix
    if(gramsPerLine == 2):      #for some reason it generates ngramSize+1 if
        gramsPerLine = gramsPerLine-1   #this correction isn't made
    for i in range (numLines):
        for j in range (gramsPerLine): 
            print(prefix)
            prefix, word = findNextPrefix(prefix, ngramNestedDict)
            if word != 'no ngram':
                line = line + ' ' + word
            else:
                break
            print (line)
        #subsequent lines
        #first text on each line must be taken from an ngram that begins
        #with <s>
        prefix = findFirstPrefix('<s>', ngramFreqDict)
        line = prefix
        
    
def findFirstPrefix(initToken, ngramFreqDict):
    ngramLst = ngramFreqDict.keys()
    
    while True:
        num = random.randint(0, len(ngramLst)- 1)
        startGram = ngramLst[num]
        startGramLst = startGram.split()
        if startGramLst[0] == initToken:
            return getPrefix(startGram)


def getPrefix(ngram):
    ngramLst = ngram.split()
    prefix = ' '.join(ngramLst[i] for i in range(1, len(ngramLst), 1))
    return prefix

def findNextPrefix(prefix, ngramNestedDict):
    probMass = 0.0
    num = random.random()

    #trap for ngram size > number of remaining words
    try:
        innerDict = ngramNestedDict[prefix]
    except KeyError:
        return prefix, 'no ngram'

    #trap for ngram with conditioned character equals end of line marker
    keyInnerDict = innerDict.keys()
    if '</s>' in keyInnerDict:
        return prefix, 'no ngram'
    
    words = innerDict.keys()
    for word in words:
        probMass = innerDict[word] + probMass
        if probMass > num:
            ngram = prefix + ' ' + word
            prefixNxt = getPrefix(ngram)
            return prefixNxt, word

#supplemental code to print the contents of a dictionary
def printDict(dict):
    stuff = dict.items()
    for elt in stuff:
        print (elt[0] + ' ' + str(elt[1]))


