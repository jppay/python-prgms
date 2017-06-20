'''
Created on Jun 16, 2017

@author: Coalesce
'''

finalList = ["http://10.10.10.10:8080", 1, 4.15, "True"]
stringList = []

for theValue in finalList:
    #theValue = raw_input()
    #if((theValue).isdigit()): # This works but also prints boolean value
    if(type(theValue) == str): # List filtering by data type
        stringList.append(theValue)

print(stringList)

portNos = stringList[0].split(':') # 
print(portNos[2])

corp1 = ['Google', 'IBM', 'FB']
corp2 = ['Wells Fargo', 'Mercedes', 'ANZ']

mergedList = []

for temp in range(len(corp1)): 
    mergedList.append(corp1[temp]) 
    mergedList.append(corp2[temp])
    
    
print(mergedList)

print(mergedList[-1:-5]) # 