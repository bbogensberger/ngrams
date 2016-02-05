'''
Bethany
this file is just the main function with parameters:
x: char for getData funtion
grS: gramSize cannot be >4
ngrS: ngramSize which is actually the ngrams/line
numL: number of lines to display

-Uses python 2.7
-Generates random unigrams, bigrams, trigrams, or quadgrams from
 the editorials found in the brown corpus.
-Requires nltk
-Other parameters that may be set are found in main().
-Some additional tokenizing could be done.
-Could be easily adapted to any other text, though it crucially depends
 on the representation generated by sents in nltk, i.e., a list of sentences,
each of which is a list of words.
'''
from ngrams import *
from unigram import *
from dict_gen import *
def main(x, grS, ngrS,numL):
    #r = real data
    #t = test data from small files in the home directory
    gramSize = grS        #1, 2, 3, 4
    numLines = numL       #number of lines to display
    rawDataSize = 100   #lines of data from corpus to use
    unigramSize = 1     #unigrams per line
    gramsPerLine = ngrS       #ngrams per line
    
    sentLst = getData(x, rawDataSize)
    #these lines I added for clerification of what you enter
    print ("gram size: ", gramSize)
    print ("Ngrams per line: ", gramsPerLine)
    
    if gramSize == 1:
        gramsPerLine = unigramSize
        #make a probability dictionary of words
        unigramDict = makeUnigramDict(sentLst, gramSize)
        printDict(unigramDict)
        genUnigrams(numLines,gramsPerLine,unigramDict)
    else:
        #gramsPerLine = int(ngramSize / gramSize)
        #make a frequency dictionary of ngrams
        ngramFreqDict = makeFreqNgramDict(sentLst,gramSize)
        printDict(ngramFreqDict)
        #make a nested probability dictionary of ngrams
        ngramNestedDict = makeNestedNgramDict(ngramFreqDict,gramSize)
        printDict(ngramNestedDict)

        genNgrams(numLines, gramsPerLine, gramSize, ngramNestedDict, ngramFreqDict)
           

