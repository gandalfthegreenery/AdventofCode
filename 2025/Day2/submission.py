import io
import csv


def checking_sevenths(start,end):
    total_sum = 0
    if len(start)!=len(end):
        if len(end)%7 !=0:
            end = "9"*len(start)
        else:
            start = "1"
            i=0
            while i<len(end)-1:
                start+="0"
                i+=1
    if(len(start)!=7):
        print("length not divisible by 7")
    else:
        print("divisible by 7")
        st1 = int(start[0])
        en1 = int(end[0])
        while st1 < en1:
            if int(start)<=int(str(st1)*7):
                total_sum+=int(str(st1)*7)
            st1+=1
        if st1==en1:
            if int(end)>=int(str(st1)*7)>=int(start):
                total_sum+=int(str(st1)*7)
    return total_sum

def checking_fifths(start,end):
    total_sum = 0
    if len(start)!=len(end):
        if len(end)%5 !=0:
            end = "9"*len(start)
        else:
            start = "1"
            i=0
            while i<len(end)-1:
                start+="0"
                i+=1
    if(len(start)%5!=0):
        print("length not divisible by 5")
    else:
        print("divisible by 5")
        if len(start)==5:
            st1 = int(start[0])
            en1 = int(end[0])
            while st1 < en1:
                if int(start)<=int(str(st1)*5):
                    total_sum+=int(str(st1)*5)
                st1+=1
            if st1==en1:
                if int(end)>=int(str(st1)*5)>=int(start):
                    total_sum+=int(str(st1)*5)
        else:
            assert(len(start)==10)
            st1 = int(start[:2])
            en1 = int(end[:2])
            while st1 < en1:
                if int(start)<=int(str(st1)*5) and start[0]!=start[1]:
                    total_sum+=int(str(st1)*5)
                st1+=1
            if st1==en1:
                if int(end)>=int(str(st1)*5)>=int(start) and start[0]!=start[1]:
                    total_sum+=int(str(st1)*5)
    return total_sum

def checking_thirds(start,end):
    total_sum = 0
    if len(start)!=len(end):
        if len(end)%3 !=0:
            end = "9"*len(start)
        else:
            start = "1"
            i=0
            while i<len(end)-1:
                start+="0"
                i+=1
    if(len(start)%3!=0):
        print("length not divisible by 3")
    else:
        print("divisible by 3")
        if len(start)==3:
            st1 = int(start[0])
            en1 = int(end[0])
            while st1 < en1:
                if int(start)<=int(str(st1)*3):
                    total_sum+=int(str(st1)*3)
                st1+=1
            if st1==en1:
                if int(end)>=int(str(st1)*3)>=int(start):
                    total_sum+=int(str(st1)*3)

        elif len(start)==6:
            st1 = int(start[:2])
            en1 = int(end[:2])
            while st1 <en1:
                if int(start)<=int(str(st1)*3) and str(st1)[0]!=str(st1)[1]:
                    total_sum+=int(str(st1)*3)
                st1+=1
            if st1==en1:
                if int(end)>=int(str(st1)*3)>=int(start) and str(st1)[0]!=str(st1)[1]:
                    total_sum+=int(str(st1)*3)
        else:
            assert(len(start)==9)
            st1 = int(start[:3])
            en1 = int(end[:3])
            while st1 < en1:
                if int(start)<=int(str(st1)*3):
                    total_sum+=int(str(st1)*3)
                st1+=1

            if st1==en1:
                if int(end)>=int(str(st1)*3)>=int(start):
                    total_sum+=int(str(st1)*3)

    return total_sum

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
            s1+=checking_thirds(start,end)
            s1+=checking_fifths(start,end)
            s1+=checking_sevenths(start,end)
print(s1)
f.close()
        
