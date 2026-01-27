import io
import numpy as np


def locations_of_splitters(input_row,start,end):
    beam_splitters = []
    while end-start>0:
        try:
            i = input_row.index('^',start,end)
            start = i+1
            beam_splitters.append(i)
        except ValueError:
            end = start

    return beam_splitters
    
def create_new_beams(beams, beam_splitters):
    global total_splits
    b2 = []
    for i in beams:
        if i in beam_splitters:
            total_splits+=1
            if i-1 not in b2:
                b2.append(i-1)
            if i+1 not in b2:
                b2.append(i+1)
        else:
            b2.append(i)

    b3 = []
    for j in b2:
        if j not in b3:
            b3.append(j)
    return b3


f= open("AdventofCodeDay7.txt","r") 
current_splits = []
beams = []
current_row = 0
middle = 0
total_splits = 0
for row in f:
    if current_row ==0:
        beams.append(row.index("S"))
        middle = row.index("S")
        print("lenrow:",len(row.strip("\n")))
    else: 
        beam_splitters = locations_of_splitters(row,0,len(row))
        beams = create_new_beams(beams,beam_splitters)
    current_row+=1


print(total_splits)
f.close()
        
