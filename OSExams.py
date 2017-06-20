'''
Created on Jun 20, 2017

@author: Coalesce
'''
import os, glob

# Current Working Dir
print(os.getcwd())
# Change Working Dir
os.chdir('C:/')
print(os.getcwd())
os.chdir('C:/Users/Coalesce.Coalesce-PC/python-workspace/Python_Day1/network_cust_lib')
print(os.getcwd())
#List all files in CWD
print(glob.glob('/*.*'))
# Navigate the dir and list dirs-and-files
for dirloc, dirName, fileName in os.walk('C:/Users/Coalesce.Coalesce-PC/python-workspace/Python_Day1/network_cust_lib'):
    os.chdir(dirloc)
    print('Current Dir: ', os.getcwd())
    allFiles = glob.glob('/*.*')
    for i in allFiles:
        print(i)
# Check logged in user        
print(os.getlogin())  