'''
Created on Jun 17, 2017

@author: Coalesce
'''
import math

# GLOBAL array to store default values (global var is useful only in same 
ipArray={'A':'10.0.0.1','B':'172.16.0.1','C':'192.168.0.1'}
def calculate(subnetDictionary):
    
    # Retrieving values
    subnetClass = subnetDictionary.get('Class')
    nosOfHosts = subnetDictionary.get('NosOfHosts')
    startingIP = subnetDictionary.get('Starting IP')
    maskBit = math.ceil(math.log(float(nosOfHosts), 2))
    
    if(ipArray.get(subnetClass) == startingIP): # Check if subnet and class is correct
        print("Mask Bit %d" %(maskBit))
        print("Borrowed Network Bits %d" %(32-maskBit))
    return None