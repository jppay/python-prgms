'''
Created on Jun 19, 2017

@author: Coalesce
'''
from Banking.PcClass import PcClass, pcList

class RouterSwitch:
    
    def __init__(self, _ipAddress, _macAddress, _vLan, _hostName):
        self.ipAddrswitch = _ipAddress
        self.macAddrswitch = _macAddress
        self.vLanswitch = _vLan
        self.hNameswitch = _hostName
        
    def set_portNo(self, _portNo):
        self.portNoswitch = _portNo
        
    def get_portNo(self):
        return self.portNoswitch
    
    def get_switch_details(self):
        return switchList
    
    
rSwtch1 = RouterSwitch('172.16.0.58', '01DA.CC22.H901', True, 'DTHSwitch')
rSwtch1.set_portNo(8980)  

connectedPcs = PcClass.get_Pc_Instance(pcList)
print('\nSWITCH DETAILS - \n\tIP: '+rSwtch1.ipAddrswitch+', \n\tMac Addr: '+rSwtch1.macAddrswitch+
      ', \n\tVLan connection: '+str(rSwtch1.vLanswitch)+
      ', \n\tPort No: '+str(rSwtch1.portNoswitch)+
      ' and \n\tHost Name: '+rSwtch1.hNameswitch+', \nfollowing PCs are connected -')

for i in connectedPcs:
    if (i.ipAddrpc == '10.0.0.13'):
        print('\nFollowing PC is blocked from routing in SWITCH:')
        print('\nHome office PC (OS: %s) blocked ' %(i.operating_sys))
    else:
        print('\nSuccessfully set up to route in SWITCH: ')
        print(i.ipAddrpc+', '+i.macAddrpc+', '+i.lnkpc+', '+i.phyLocpc)

#print(connectedPcs)
switchList = [rSwtch1]

# Inheritance in action : RouterSwitch -> Layer3Switch 
class Layer3Switch(RouterSwitch):
    
    # Additional attributes (variables) in constructor
    def __init__(self, _ipAddress, _macAddress, _vLan, _hostName, _link, _user): 
        RouterSwitch.__init__(self, _ipAddress, _macAddress, _vLan, _hostName) # Super() sort-of command
        self.link = _link
        self.userName = _user
    
    # Method to retrieve PC details for Layer3 Switch    
    def get_PCdetails_layer3(self): 
        layer3ConnectedPcs = PcClass.get_Pc_Instance(pcList)
        print('\nLayer 3 SWITCH connected to PCs')
        for i in layer3ConnectedPcs:
            print(i.ipAddrpc)
            
l3SwitchObj = Layer3Switch('192.168.0.1', '44D1.23QW.NMF6', True, 'WebLogic Host', 'Up', 'wladmin')    
l3SwitchObj.get_PCdetails_layer3()       
print(l3SwitchObj.get_switch_details())