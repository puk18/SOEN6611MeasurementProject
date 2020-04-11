#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:10:56 2020

@author: pulkitwadhwa
"""
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import pandas as pd
import os

file1=input("Enter file path for 1,2&6 .csv")
file2=input("Enter file path for 5&6.csv")


Metrics1 = pd.read_csv(file1)
Metrics2=pd.read_csv(file2)


path, filename = os.path.split(file1)
currentDirectory=os.path.dirname(path)
path1=os.path.dirname(currentDirectory)
finalPath=os.path.dirname(path1)
print(Metrics1.head(3))



statementCoverageList=Metrics1["LINE_COVERED"]
branchCoverageList=Metrics1["BRANCH_COVERED"]
codeSmellList=Metrics1["Code_Smell"]


print(path)
print(currentDirectory)


dict1={}

print("Metrics 1&6")
correlation1and6,p1and6=spearmanr(codeSmellList,statementCoverageList)
dict1["Metrics 1&6"]=correlation1and6
print("correlation="+str(correlation1and6))
print("p="+str(p1and6))





plt.scatter(codeSmellList,statementCoverageList)
plt.xlabel("codeSmellList")
plt.ylabel("statementCoverageList")
plt.title("Statement coverage vs Code Smells")
plt.show()



print("Metrics 2&6")

correlation2and6,p2and6=spearmanr(branchCoverageList, codeSmellList)
dict1["Metrics 2&6"]=correlation2and6

print("correlation="+str(correlation2and6))
print("p="+str(p2and6))

plt.scatter(codeSmellList,branchCoverageList)
plt.xlabel("codeSmellList")
plt.ylabel("Branch coverage results")
plt.title("Branch coverage vs codeSmellList ")
plt.show()




codeChurnList=Metrics2["Code_Churn"]
codeSmellDiff=Metrics2["Code_SmellDiff"]


print("Metrics 5&6")
correlation5and6,p5and6=spearmanr(codeChurnList, codeSmellDiff)
dict1["Metrics 5&6"]=correlation5and6


print("correlation="+str(correlation5and6))
print("p="+str(p5and6))
plt.scatter(codeChurnList,codeSmellDiff)
plt.xlabel("codeChurnList")
plt.ylabel("codeSmellDiff ")
plt.title("Code Churn vs codeSmellList ")
plt.show()




df=pd.DataFrame(dict1.items(),columns=['Metrics', 'Correlation'])
df.to_csv(os.path.join(path,r'Correlation.csv'),mode='a', header=False,index=False)


