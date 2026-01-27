import io
import csv
import numpy as np




accessible_rolls =0
f= open("AdventofCodeDay4.txt","r") 
length_of_row = 136
number_of_rolls = 136
neighbors = np.zeros([138,138])
rolls = [["" for _ in range(136)] for _ in range(136)]
i = 0
j = 0
cols = 0
rows = 0

for row in f:
    j=0
    for col in row:
        if col == "@":
            neighbors[i:i+3,j:j+3]+=1
            neighbors[i+1,j+1]-=1
            rolls[i][j]="@"
        elif col==".":
            rolls[i][j]="."
        j+=1
        cols = j
    i+=1
    rows = i
i = 0
j=0
f.close()
removable_rolls = True
num_rounds = 0
print(neighbors[0:5])
while removable_rolls:
    removable_rolls=False 
    i =0
    j = 0
    while i < 136:
        j=0
        #print(i)
        while j < 136:
            if rolls[i][j] =="@":

                if neighbors[i+1][j+1]<4:
                    accessible_rolls+=1
                    removable_rolls=True
                    neighbors[i:i+3,j:j+3]-=1
                    neighbors[i+1][j+1]+=1
                    rolls[i][j]="."
            j+=1
            #print('J:',j)
        i+=1
    num_rounds+=1
    #print(num_rounds)
            
print(accessible_rolls)
f.close()
        
