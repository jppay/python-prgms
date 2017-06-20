'''
Created on Jun 17, 2017

@author: Coalesce
'''

import sys
sys.path.append('C:/')

from pip._vendor.distlib.compat import raw_input
from network_cust_lib.SubnetCalc import calculate
from pytrial.TrialCmdFile import justPrintPort 
from pyremotetrial.anothertrial import anothertrialmethod

subnetClass = raw_input('Enter Subnet Class: ')
nosOfHosts = raw_input('Number of hosts: ')
startingIP = raw_input('Starting IP Address: ')

# Define dictionary to hold all values
subnetDict={'Class':subnetClass, 'NosOfHosts':nosOfHosts, 'Starting IP': startingIP}

# Calling function 
# Mod 1: with Dictionary instead of values
calculate(subnetDict)

# Calling function created from non-IDE route
justPrintPort(9000)

# Calling function from remote location
anothertrialmethod(12345)

# Trial to define a GLOBAL var and access it in another module
global portNos
def accessPort(): 
    portNos = 8000
    
