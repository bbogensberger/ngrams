'''
This file contains all of your original functions for making unigrams
    with minor corrections so that the functions actually work
'''

import random
import sys
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
    for i in range(numLines):
        print (genUnigramsLine(probLst, wordsPerLine))
    
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

