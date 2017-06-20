'''
Created on Jun 20, 2017

@author: Coalesce
'''
import os
from pip._vendor.distlib.compat import raw_input

# File handling
filepath = raw_input('Enter a file name to open/create: ')

if(os.path.exists(filepath)):
    print("File exists!")
    contents = open(filepath, mode = 'r') # 'a','w','r' append, write, read
    for i in contents:
        print(i)
else:
    (dirName, fileName) = os.path.split(filepath)
    if not(os.path.exists(dirName)):
        os.mkdir(dirName, mode=0o777, dir_fd=None)
        print('Dir not found; dir created...')
        print("File not found; creating it...")
        newFile = open(filepath, mode = 'w') # No explicit file create method - just use open()
        newFile.write('''
            # Alter PC table to add SWITCH table referential dependency (Foreign Key)
            ALTER TABLE PC ADD SWITCH_HOST varchar(25) NOT NULL;
            alter table PC modify SWITCH_HOST varchar(25) NULL DEFAULT NULL;
            update PC set switch_host = null where 1=1;
            alter table PC add constraint fk_switch_host FOREIGN KEY (SWITCH_HOST) REFERENCES SWITCH(HOST);
            
            # Insert data in Switch and update FK in PC table
            insert into switch(HOST, IPADDRESS, MACADDRESS, VLAN) values ('DTHSwitch', '172.16.0.58', '01DA.CC22.H901', 1); 
            update PC set switch_host = 'DTHSwitch' where PCNO = 'PC-1';'''
        )
        print("File created now!")
        newFile.close()  
    elif(os.path.exists(dirName)) and not (os.path.exists(filepath)):
        print('Dir exists; file not found. Creating it...')
        newFile = open(filepath, mode = 'w') # No explicit file create method - just use open()
        newFile.write('''
            # Alter PC table to add SWITCH table referential dependency (Foreign Key)
            ALTER TABLE PC ADD SWITCH_HOST varchar(25) NOT NULL;
            alter table PC modify SWITCH_HOST varchar(25) NULL DEFAULT NULL;
            update PC set switch_host = null where 1=1;
            alter table PC add constraint fk_switch_host FOREIGN KEY (SWITCH_HOST) REFERENCES SWITCH(HOST);
            
            # Insert data in Switch and update FK in PC table
            insert into switch(HOST, IPADDRESS, MACADDRESS, VLAN) values ('DTHSwitch', '172.16.0.58', '01DA.CC22.H901', 1); 
            update PC set switch_host = 'DTHSwitch' where PCNO = 'PC-1';'''
        )
        print("File created now!")
        newFile.close()
        
        
    
    