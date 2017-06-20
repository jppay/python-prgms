'''
Created on Jun 19, 2017

@author: Coalesce
'''
import pymysql
# Connection object
db = pymysql.connect(host="localhost", user="root", passwd="root", db="networkdb")

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
    
    def get_Pc_Instance(self, _):
        return pcList
    
'''homePc = PcClass('10.0.0.13', '00D0.BD10.5C67', 'Up')
homePc.set_phyLoc('Home Office')

laptopPc = PcClass('10.0.0.129', '00A1.ZX98.A549', 'Up')
laptopPc.set_phyLoc('Home Laptop')

pcList = [homePc, laptopPc]'''

# Show the connection between PC and Switch
cursorPcSw = db.cursor()
for k in swObj:
    print(k.hNameswitch)
    cursorPcSw.execute("""select * from PC where switch_host = '%s'""" %(k.hNameswitch)) 
    resultSet = cursorPcSw.fetchall()
    for m in resultSet:
        obList = []
        for n in m:
            obList.append(n)
        print(obList)
        obList[0] = PcClass(obList[1],obList[2],obList[3])   
        setPcs = PcClass.get_Pc_Instance(obList)
        for eachPc in setPcs:
            print('Switch \''+k.hNameswitch+'\' set up with PC having IP '+eachPc.ipAddrpc+', Mac Address '+eachPc.macAddrpc+
              ' and Link status is '+eachPc.lnkpc)   
    