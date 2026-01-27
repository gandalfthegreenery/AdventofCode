import io
import csv

s1 = 0
total_joltage =0
f= open("AdventofCodeDay3.txt","r") 
length_of_string = 12
length_of_row = 101


for row in f:
        locations = [i for i in range(-1-length_of_string+length_of_row,-1+length_of_row)]
        k=0
        end = -1
        for i in locations:
            j = i
            max_ind = i
            print("row:",row)
            print("j:",j)
            print("k:",k)
            print("i:",i)
            print("end:",end)
            while j > end:
                print('row[j]',row[j])
                print("max_ind",max_ind)
                print("max_val",row[max_ind])
                if row[j]>=row[max_ind]:
                        max_ind=j
                        locations[k] = max_ind
                        
                j-=1
            k+=1
            end = max_ind
        print(locations)
        fin = ""
        for i in locations:
              fin+=row[i]
        total_joltage+=int(fin)

print(total_joltage)
f.close()
        
