'''
Created on Jun 17, 2017

@author: Coalesce
'''
import random
import base64

# Tuple examples
sampleTuple = ('asdf','asdf')
tupList = ([1,2,3],[4,5,6])

# Dictionary examples and parsing
dictEx = {'Name':'Jiggy', 'Class': 'Tenth', 'Roll no': '1234', 'Subjects':['English','Mathematics','Physics']}

for i in dictEx.keys():
    print("%s: %s" %(i,dictEx.get(i)))

listOfDictEx = [{'Name':'Miggy', 'Class': 'Tenth', 'Roll no': '1234', 'Subjects':['English','Mathematics','Physics']}, 
                {'Name':'Ciggy', 'Class': 'Ninth', 'Roll no': '456431', 'Subjects':['English','Mathematics','Social Sciences']}]

print("*************************")
#--------------------------------


# Printing List of Dictionary (with List in it)
i=0
for key in listOfDictEx:
    for (a,b) in key.items():
        print(a, ":\t", key[a])
        print("Length of key dict: %d" %(len(key)))
    if i >= len(key):
        break
    else:
        i+=1
#--------------------------------

# UNION, INTERSECTION operations for Set            
ports = {8080,123,111,151}
idAddr = {192,154,111,564}

allPorts = ports.union(idAddr)
print(allPorts)
commonPorts = ports.intersection(idAddr)
print(commonPorts)
remainingPorts = ports - idAddr
print(remainingPorts)
#--------------------------------


# Using RANDOM module to generate random nos, encode-decode to-from Base64
idSet = {0}
for i in range(100):
    idSet.add(random.randrange(100000))
print (idSet)            

b64 = []
for i in idSet:
    encoded = base64.b64encode(str(i).encode(encoding='utf_8', errors='strict'))
    b64.append(encoded)
    
print(b64)   

backFromB64 = []
for j in b64:
    decoded = base64.b64decode(j, None, True)
    strDecoded = str(decoded)
    backFromB64.append(strDecoded.replace("b'", ""))
print(backFromB64)
#-------------------------------- 