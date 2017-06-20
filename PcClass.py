'''
Created on Jun 19, 2017

@author: Coalesce
'''

class PcClass: 
    
    operating_sys = 'Windows XP'
    
    def __init__(self, _ipAddress, _macAddress, _link):
        self.ipAddrpc = _ipAddress
        self.macAddrpc = _macAddress
        self.lnkpc = _link
        
    def set_phyLoc(self, _physicalLoc):
        self.phyLocpc = _physicalLoc
        
    def get_phyLoc(self):
        return self.phyLocpc
    
    def get_Pc_Instance(self):
        return pcList
    
homePc = PcClass('10.0.0.13', '00D0.BD10.5C67', 'Up')
homePc.set_phyLoc('Home Office')

laptopPc = PcClass('10.0.0.129', '00A1.ZX98.A549', 'Up')
laptopPc.set_phyLoc('Home Laptop')

pcList = [homePc, laptopPc]
    