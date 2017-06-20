'''
Created on Jun 16, 2017

@author: Coalesce
'''

empData = open("C:/Users/Coalesce.Coalesce-PC/Documents/EmpData.csv", 'r')
empList = list(empData)

for eachRow in empList:
    #print(eachRow)
    eachField = list(eachRow.split(','))
    for oneField in range(len(eachField)):
        print("%d\t%s" %(oneField[0], oneField[1]))
empDataNew = open("C:/Users/Coalesce.Coalesce-PC/Documents/Python Scripts/EmpData.csv", 'r')
empListNew = list(empDataNew)

print (empList==empListNew)

