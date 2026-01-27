current_dial = 50
count = 0
with open("AdventofCodeDay1.txt","r") as f:
    for line in f:
        num =  int(line[1:])
        direction = line[0]
        if direction == "R":
            current_dial+=num
        else:
           current_dial-=num
        if current_dial%100==0:
            count+=1
print(count)
f.close()
        
