'''
Created on Jun 20, 2017

@author: Coalesce
'''
from openpyxl import Workbook
from pip._vendor.distlib.compat import raw_input
import os, calendar

workBookFile = raw_input("Enter workbook (excel) name: ")
directName = 'C:/Users/Coalesce.Coalesce-PC/Documents/Temp'
finalFile = directName+"/"+workBookFile+".xlsx"

if(os.path.exists(directName)):
    print('Navigating to dir...')
    workBk = Workbook()
    monthList = calendar.month_name 
    #['January','February','March','April','May','June',
    #             'July','August','September','October']
    j = 0
    for i in monthList:
        if not(len(i)) == 0:
            #print(i)
            tempSheet = workBk.create_sheet(i, j)
            j+=1
        workBk.save(finalFile)   
    print('File created!')
