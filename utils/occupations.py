#!/usr/bin/python

import random

def convertDict(x):
    d = {}
    f = open(x)
    f.readline()
    m = f.readline()
    while m!='':
        valueHolder = []
        if m[0]=='"':
            m = m[1:]
            indexOfEndQuote = m.find('"')
            currentJob = m[:indexOfEndQuote]
            indexOfSecondComma = m.find(',', indexOfEndQuote + 2)
            valueHolder.append(float(m[indexOfEndQuote + 2: indexOfSecondComma]))
            valueHolder.append(m[indexOfSecondComma + 1:])
            d[currentJob] = valueHolder
        else:
            if m[0:5] != 'Total':
                indexOfComma = m.find(',')
                currentJob = m[:indexOfComma]
                indexOfSecondComma = m.find(',', indexOfComma + 1)
                valueHolder.append(float(m[indexOfComma + 1: indexOfSecondComma]))
                valueHolder.append(m[indexOfSecondComma + 1:])
                d[currentJob] = valueHolder
        m = f.readline()
    return d
def picker(dict):
    percentage = random.random() * 99.8
    counter = 0
    for item in dict:
        if percentage > dict[item][0] + counter:
            counter += dict[item][0]
        else:
            return item
        
def occupations():
    dict = convertDict("data/occupations.csv")
    return picker(dict)

print occupations()
