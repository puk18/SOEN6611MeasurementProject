#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:43:46 2020

@author: pulkitwadhwa
"""

from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import pandas as pd
import os

file1=input("Enter file path for jacoco.csv")
file2=input("Enter file path for extractedpit.csv")


path, filename = os.path.split(file1)
currentDirectory=os.path.dirname(path)
path1=os.path.dirname(currentDirectory)
finalPath=os.path.dirname(path1)





Metrics1 = pd.read_csv(file1)
Metrics2=pd.read_csv(file2)

metrics = pd.merge(left=Metrics1, right=Metrics2, left_on='CLASS', right_on='CLASS')
#metrics.to_csv(currentDirectory+'out.csv', index=False)

metrics['Complexity'] =  metrics['COMPLEXITY_MISSED']+metrics['COMPLEXITY_COVERED']

complexityList = metrics["Complexity"]/100




#Statement coverage results 
statementCoverageScore = (metrics["LINE_COVERED"]/(metrics["LINE_COVERED"]+metrics["LINE_MISSED"]))


#branch coverage Results

metrics['branchCoverageList'] = (metrics["BRANCH_COVERED"]/(metrics["BRANCH_COVERED"]+metrics["BRANCH_MISSED"]))

metrics['branchCoverageList']=metrics['branchCoverageList'].fillna(0)
branchCoverageScore=metrics['branchCoverageList'].tolist()


#mutation score
mutationScoreList = metrics["Mutation Score"]/100




dict1={}



#metrics 1&3

print("Metrics 1&3")
correlation1and3,p1and3=spearmanr(statementCoverageScore, mutationScoreList)

dict1["Metrics 1&3"]=correlation1and3

print("correlation="+str(correlation1and3))
print("p="+str(p1and3))


plt.scatter(mutationScoreList, statementCoverageScore)
plt.ylabel("Statement coverage results")
plt.xlabel("Mutation Score")
plt.title("Statement coverage vs Mutation Score")
plt.show()





#metrics 2&3
print("Metrics 2&3")

correlation2and3,p2and3=spearmanr(branchCoverageScore, mutationScoreList)

dict1["Metrics 2&3"]=correlation2and3

print("correlation="+str(correlation2and3))
print("p="+str(p2and3))

plt.scatter(mutationScoreList, branchCoverageScore)
plt.ylabel("Branch coverage results")
plt.xlabel("Mutation Score")
plt.title("Branch coverage vs Mutation Score")
plt.show()





#Correlation between 1 and 4


print("Metrics 1&4")

correlation1and4,p1and4=spearmanr(statementCoverageScore, complexityList)

dict1["Metrics 1&4"]=correlation1and4


print("correlation="+str(correlation1and4))
print("p="+str(p1and4))


plt.scatter(complexityList, statementCoverageScore)
plt.ylabel("Statement coverage results")
plt.xlabel("complexity Score")
plt.title("Statement coverage vs Complexity")
plt.show()





#Correlation between 2 and 4


print("Metrics 2&4")

correlation2and4,p2and4=spearmanr(branchCoverageScore, complexityList)


dict1["Metrics 2&4"]=correlation2and4

print("correlation="+str(correlation2and4))
print("p="+str(p2and4))



plt.scatter(complexityList , branchCoverageScore)
plt.ylabel("Branch coverage results")
plt.xlabel("complexity Score")
plt.title("Branch coverage vs Complexity")
plt.show()






#Output to file
fieldNames=["metrics","Correlation"]

df=pd.DataFrame(dict1.items(),columns=['Metrics', 'Correlation'])
df.to_csv(os.path.join(finalPath,r'Correlation.csv'), header=True,index=False)
