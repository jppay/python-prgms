'''
Created on Jun 19, 2017

@author: Coalesce
'''
# Class definition - file name and class name CAN BE DIFFERENT
from Banking.RouterSwitch import RouterSwitch, switchList
class Router: 
    
    # Default Constructor (used to initialize variables)
    def __init__(self, _hostTempName, _link, _ipAddress):
        self.localHostName = _hostTempName
        self.link = _link
        self.ipAddr = _ipAddress
        
    # Setters and getters are alternative to default constructor variable initialization    
    def set_passwd(self, _pwd):
        self.password = _pwd
        
    def get_passwd(self):
        return self.password
        
    def connect_switch(self, switchList):
        print('\n'+self.localHostName+' connecting to SWITCH...')
        localSwitchList = switchList
        for i in localSwitchList:
            print('\nROUTER connected to SWITCH: \n'+i.ipAddrswitch)
            
    def filter(self):
        print('\nROUTER is filtering IP Addresses: \n\t', self.localHostName, self.link, self.ipAddr)
        connectedSwitch = RouterSwitch.get_switch_details(switchList)
        for i in connectedSwitch:
            print('\nINFO: Switch connected: \n'+i.ipAddrswitch)
        
# Objects created
router1841 = Router('Tomcat Host', 'Up', '10.0.0.1')
router1841.set_passwd('abc123') # Setter
router1841.connect_switch(switchList)
#
router2811 = Router('WebSphere Host', 'Down', '172.16.0.1')
router2811.set_passwd('xyz098') # Setter
router2811.filter()

# Getters with object variables
print('\nPassword for %s is %s' %(router1841.localHostName, router1841.get_passwd()))
print('Password for %s is %s' %(router2811.localHostName, router2811.get_passwd()))
