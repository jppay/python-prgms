'''
Created on Jun 17, 2017

@author: Coalesce
'''
pwdStr = "STAR"
i = 0
pwdStrList = []

print("Encrypted pwd: ")
for x in pwdStr:
    pwdStrList.append(bin(ord(x) & (16)))

for j in pwdStrList:
    print(j)

decryptPwd = []
for m in pwdStrList: 
    binElement = bin(ord(m))
    decryptPwd.append(binElement & 0b10000)
       
print("Decrypted pwd: ")
print(decryptPwd)        