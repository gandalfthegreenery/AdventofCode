import csv

def checking_halves(start,end):
    total_sum=0
    if len(start)!=len(end):
        if len(end)%2 ==1:
            end = "9"*len(start)
        else:
            start = "1"
            i=0
            while i<len(end)-1:
                start+="0"
                i+=1              
    if(len(start)%2==1):
        print("length not divisible by 2")
    else:
        print("divisible by 2")
        st1 = int(start[:(int(len(start)/2))])
        en1 = int(end[:int(len(start)/2)])
        while st1<en1:
            if int(start)<=int(str(st1)*2):
                total_sum+=int(str(st1)*2)
            st1+=1
        if st1==en1:
            if int(end)>=int(str(st1)+str(st1))>=int(start):
                total_sum+=int(str(st1)*2)
    return total_sum

s1 = 0
with open("AdventofCodeDay2.txt","r") as f:
    reader= csv.reader(f)
    for row in reader:
        for ranges in row:
            print()
            edges = ranges.split('-')
            start =edges[0]
            end = edges[1]
            print("start:",start)
            print("end:",end)
            s1+=checking_halves(start,end)
print(s1)
f.close()
        
