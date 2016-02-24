'''
This file contains all of your original functions for making unigrams
    with minor corrections so that the functions actually work
'''

import random
import sys
import pandas as pd
from dict_gen import *


'''
pre: sentLst is a list of lists of strings
post: returns a dictionary: ngram as key, ngram probability as value
'''
def makeUnigramDict(sentLst, ngramSize):
    freqDict = {}
    probDict = {}
    numWords = 0

    #compute the frequencies for each word
    for sent in sentLst:
        freqDict, numWords = unigramDict(sent, freqDict, numWords)
            
    #compute the probabilities for each word 
    for word in freqDict:
        probDict[word] = float(freqDict[word])/float(numWords)
    
    return probDict


def unigramDict(sent, freqDict, numWords):
    for word in sent:
        numWords = numWords + 1
        if word in freqDict:
            freqDict[word] = freqDict[word] + 1
        else:
            freqDict[word] = 1
    return freqDict, numWords

def genUnigrams(numLines, wordsPerLine, probDict):  #correction here for 3rd param

    print ("---------------------UNIGRAMS----------------------")
    probLst = list(probDict.items())
    file = open('data.txt','w')
    for i in range(numLines):
        if wordsPerLine == 1:
            file.write(genUnigramsLine(probLst, wordsPerLine)+'\n')
        else:
            for j in range(wordsPerLine):
                file.write(genUnigramsLine(probLst, wordsPerLine))
    
def genUnigramsLine(probLst, wordsPerLine):
    startEnd = ['<s>', '</s>']
    line = ''
    for numWords in range(wordsPerLine):
        num = random.random()
        probMass = 0.0
        for item in probLst:
            probMass = probMass + item[1]
            if probMass > num and item[0] not in startEnd:
                line = line + ' ' + item[0]
                break
    line = nicer(line)
    return line

def nicer(line):
    line = line + '.'
    line = line.lstrip()
    if line[0].isalpha():
        line = line[0].capitalize() + line[1:]
    return line

def freqTable():
    fileIn = open('data.txt', 'r')
    fileOut = open('dataOut.txt', 'w')
    lines = [line.strip() for line in fileIn if line.strip() and not line.startswith('com')]
    lineSer = pd.Series(lines)
    freq =lineSer.value_counts()
    freq.to_csv('dataOut.txt')
    with pd.option_context('display.max_rows',999):
        print freq
    
