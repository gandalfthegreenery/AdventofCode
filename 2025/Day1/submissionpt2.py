current_dial = 50 #dial starts at position 50
count = 0
zero = False 
with open("AdventofCodeDay1.txt","r") as f: 
    for line in f:
        num =  int(line[1:])    
        direction = line[0]  
        if num==0:
            pass
        cycles = int(num/100)
        remainder = num%100
        count+=cycles
        if current_dial ==0:
            zero = True
        else:
            zero = False
        if direction == "R":
            current_dial+=remainder
        else:
            current_dial-=remainder
        if current_dial>=100:
            current_dial-=100
            count+=1
        elif current_dial<0 and not zero:
            current_dial+=100
            count+=1
        elif current_dial<0 and zero:
            current_dial+=100
        elif current_dial==0 and not zero:
            count+=1
        assert(current_dial<100 and current_dial>=0)
print(count)
f.close()
        
