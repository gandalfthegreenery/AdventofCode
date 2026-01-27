import io
import numpy as np


def clear_buff():
    global eq_buf
    global current_func
    global total_sum
    temp_val =0
    if current_func =="+":
        temp_val =0
        for i in eq_buf:

            temp_val+=int(i)
    elif current_func =="*":
        temp_val =1
        for i in eq_buf:
            temp_val*=int(i)
    else:
        print("error")
    print(eq_buf)
    print("current_func",current_func)
    print("temp_val",temp_val)

    total_sum+=temp_val
    eq_buf =[]

f= open("AdventofCodeDay6.txt","r") 
values = []
i=0
total_sum = 0

for row in f:
    values.append(row)

eq_buf = []
current_func = "+"


while i < len(values[0]):
    j=0
    col = ""
    while j < len(values):
        col+= str(values[j][i])
        j+=1
    
    if col[-1]=="+":
        clear_buff()
        current_func="+"
        eq_buf.append(int(col[:-1]))
    elif col[-1]=="*":
        clear_buff()
        current_func="*"
        eq_buf.append(int(col[:-1]))
    elif col.strip()=="":
        pass
    else:
        eq_buf.append(int(col))
    i+=1

clear_buff()
print(total_sum)


f.close()
        
