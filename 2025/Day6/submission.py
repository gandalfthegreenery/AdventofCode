import io
import numpy as np


f= open("AdventofCodeDay6.txt","r") 
equations = [[0 for _ in range(4)] for _ in range(1000)]

functions =["" for _ in range(1000)]
ids_fresh = 0
i=0
j =0
print(len(equations[0]))
print(len(functions))
for row in f:
    if j ==4:
        for col in row.split():
            functions[i]=col
            i+=1
    else:
        for col in row.split():
            equations[i][j]=int(col)
            i+=1

            
    i=0
    j+=1

tot_sum = 0
i=0
while i < len(functions):
    temp = 0
    if functions[i]=="*":
        temp = equations[i][0]*equations[i][1]*equations[i][2]*equations[i][3]
    elif functions[i]=="+":
        temp = equations[i][0]+equations[i][1]+equations[i][2]+equations[i][0]
    else:
        print("error")
    tot_sum+=temp
    i+=1
print(tot_sum)
f.close()
        
