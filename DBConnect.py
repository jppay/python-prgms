'''
Created on Jun 19, 2017

@author: Coalesce
'''
#
import pymysql
from Banking.PcClass import PcClass 
from Banking.RouterSwitch import RouterSwitch
 
# Connection object
db = pymysql.connect(host="localhost", user="root", passwd="root", db="networkdb")

# -------- PcClass Objects from DB -------- 
# Cursor object
cursor = db.cursor()
customSql = "select * from PC"
cursor.execute(customSql) # execute and send data to RAM
resultSet = cursor.fetchall() # fetchall() gets its data from RAM
#print(resultSet)

# Alternative way to execute
#cursor.execute("select * from PC")
#resultSet = cursor.fetchall()
pcObj = []
obList = []
for i in resultSet:
    obList = []
    for c in i:
        obList.append(c)
    obList[0] = PcClass(obList[1],obList[2],obList[3])   
    pcObj.append(obList[0]) 

print('\nPC Details -')
for j in pcObj:
    print('IP: '+j.ipAddrpc+'\tMac: '+j.macAddrpc+'\tLink Status: '+j.lnkpc)    

# -------- RouterSwitch Objects from DB --------  
swObj = []
customSql = "select * from SWITCH"
swCursor = db.cursor()
swCursor.execute(customSql) 
swResultSet = swCursor.fetchall()  
print(swResultSet)
for j in swResultSet:
    obList = []
    for c in j:
        obList.append(c)
    obList[0] = RouterSwitch(obList[1],obList[2],obList[3],obList[0])   
    swObj.append(obList[0]) 

print('\nSWITCH Details -')
for z in swObj:
    print('Host: '+z.hNameswitch+'\tIP: '+z.ipAddrswitch+'\tMac: '+z.macAddrswitch+'\tLink Status: '+str(z.vLanswitch))   
