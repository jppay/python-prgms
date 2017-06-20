'''
Created on Jun 17, 2017

@author: Coalesce
'''
tScores=[[6,7,9],[8,9,5],[9,7,5]]
langSkills=["C","Python","Java"]
trainees=["T1","T2","T3"]

print("\t%s" %(langSkills))
i=0
for iScore in tScores:
    eachScore=list(iScore)
    print("%s\t%s" %(trainees[i], eachScore))
    i+=1