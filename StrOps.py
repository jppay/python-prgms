'''
Created on Jun 17, 2017

@author: Coalesce
'''
# String types: single line, multi-line
strMessage='''This is a multiline
            string statement
            which needs \''' to 
            display it correctly. 
            it needs QUOTES to work. '''

#strMessage='this is a multiline\
#            string statement. \
#                        which needs \''' to \n\
#            display it correctly'

# Use \ for using " or ' multi-line strings

print("With capitalize():")
print(strMessage.capitalize())    
print("With title():")        
print(strMessage.title())            
# # # # # # # 

# String functions
centeredStr="Jiggy"
print("Centered: ")
print(centeredStr.center(11, '*'))

print("Justification: left, right")
print(centeredStr.ljust(20, '^'))
print(centeredStr.rjust(20, '^'))

print("Case-related functions: islower(), isupper()")
print(centeredStr.islower())
print(centeredStr.isupper())
