'''
Created on Jun 19, 2017

@author: Coalesce
'''
import math

def calculateMaskBits(nodes=9000):
    return math.log2(float(nodes))

print(calculateMaskBits(8000))