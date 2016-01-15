'''
This file contains the functions for generating the dictionaries
    no correctons were needed here
'''

import random
import re
import sys

#make the dictionaries
'''
pre: sentLst is a list of lists of strings
     e.g., [ ['Assembly', 'session', 'brought', 'much', 'good'],
             ['The', 'General Assembly', ',' 'which', '.'] ]
post: <s> and </s> tokens have been inserted.
      All punctuation has been removed.
      All alphabetic characters are lower case
'''
def tokenize(sentLst):
    punctLst = [',', ';', ':',')', '(', '?', '!', '.', '""', "''","``", '"', "'"]
    sentLstTok = []
    for sent in sentLst:
        #insert start & end of sentence symbols
        sent.insert(0,'<s>')
        sent.append('</s>')
        #lambda function to remove punctuation
        newSent = filter(lambda token: token not in punctLst, sent)
        newSent = toLower(newSent)
        sentLstTok.append(newSent)
    
    return sentLstTok

'''
pre: newSent is a list of strings
post: all characters in newSent are lower case
'''
def toLower(newSent):
    lst = []
    for word in newSent:
        lst.append(word.lower())
    return lst

'''    
pre: sentLst is a list of lists of strings
post: returns a dictionary:ngram as key, freq as value
'''
def makeFreqNgramDict(sentLst, gramSize):
    freqDict = {}

    for sent in sentLst:
        freqDict = freqNgramDict(sent, freqDict, gramSize)
        
    return freqDict

def freqNgramDict(sent, freqDict, gramSize):
        for prefix in range(len(sent) - (gramSize - 1)):
            gram = ''
            gram = sent[prefix]
            for suffix in range(prefix + 1, prefix + gramSize, 1):
                gram = gram + ' ' + sent[suffix]
            if gram in freqDict:
                freqDict[gram] = freqDict[gram] + 1
            else:
                freqDict[gram] = 1
        return freqDict
'''
pre: freqDict is a dictionary: ngram as key, freq as value
post: returns a nested dictionary where:
        Key = conditioning part of n gram
        Value = dictionary where:
             Key1 = conditioned part of n gram
             value: ngram probability
      Example: if data contains trigrams:The bad cat, The bad cat, The bad dog, The bad bird, The bird
      The dictionary would contain this entry:
      {'The bad' : {'cat' : .5, 'dog' : .25, 'bird': .25} } 
'''
def makeNestedNgramDict(freqDict, gramSize):
    
    nestedDict = {}
    prefixDict = {}
    ngramLst = list(freqDict.keys())
    
    for ngram in ngramLst:
        eltLst = ngram.split()
        prefixLst = [eltLst[i] for i in range(0, len(eltLst) - 1, 1)]
        prefix = ' '.join(prefixLst)
        if prefix in prefixDict:
            prefixDict[prefix] = prefixDict[prefix] + freqDict[ngram]
        else:
            prefixDict[prefix] = freqDict[ngram]
    
    
    prefixes = list(prefixDict.keys())

    for prefix in prefixes:
        innerDict = makeInner(prefix, prefixDict, ngramLst, freqDict)
        nestedDict[prefix] = innerDict

    return  nestedDict


def makeInner(prefix, prefixDict, ngramLst, freqDict):
    innerDict = {}
    numPrefixes = 0
    for ngram in ngramLst:
        eltLst = ngram.split()
        prefixCandLst = [eltLst[i] for i in range(0, len(eltLst) - 1, 1)]
        prefixCand = ' '.join(prefixCandLst)
        wordCand = eltLst[len(eltLst) - 1]
        if prefixCand == prefix:
            innerDict[wordCand] = float(freqDict[ngram]) / float(prefixDict[prefix])
    return innerDict

