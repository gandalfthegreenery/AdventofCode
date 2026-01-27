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
    
def create_new_beams(beams,beam_splitters):
    new_beams = [0]*len(beams)
    i = 0
    splitter_set = set(beam_splitters)
    while i < len(beams):
        if i in splitter_set:
            if len(beams)-1>i >0:
                new_beams[i-1]+=beams[i]
                new_beams[i+1]+=beams[i]
            elif i ==0:
                new_beams[i+1]+=beams[i]
            elif i >0:
                new_beams[i-1]+=beams[i]
        else:
            new_beams[i]+=beams[i]
        i+=1
    return new_beams
        

f= open("AdventofCodeDay7.txt","r") 
current_splits = []
beams = []
current_row = 0
middle = 0
total_splits = 0
for row in f:
    row = row.strip("\n")
    if current_row ==0:
        print(row.index("S"))
        beams = [0]*len(row)
        beams[row.index("S")]=1
    elif current_row<10:
        beam_splitters = locations_of_splitters(row,0,len(row))
        beams = create_new_beams(beams,beam_splitters)
        print("beam_splitters:",beam_splitters)

        print("beams:",beams)
    
    else: 
        beam_splitters = locations_of_splitters(row,0,len(row))
        beams = create_new_beams(beams,beam_splitters)
    current_row+=1


print(sum(beams))
f.close()
        
