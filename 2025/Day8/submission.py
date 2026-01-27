import io
import numpy as np
import math

class Point:
    def __init__(self,x,y,z,id):
        self.id = id
        self.x = x
        self.y = y
        self.z = z


    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def distance(self, other):
        if type(other) is Point:
            return (self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2
        else:
            raise TypeError
        
    def __eq__(self, value):
        return (self.x==value.x and self.y==value.y and self.z ==value.z)
        
class Circuit:
    def __init__(self,input):
        if len(input)==2:
            self.nodes = input
            self.distance = input[0].distance(input[1])
        else:
            self.nodes = input
            self.distance = -1
    
    def size_eq(self,other):
        if type(other) is Circuit:
            return len(self.nodes)==len(other.nodes)
        else:
            raise TypeError
        
    def merge_circuits(self,other):
        if type(other) is Circuit:
            new_connections=[]
            for i in other.current_nodes():
                new_connections.append(i)
            for j in self.nodes:
                if j not in new_connections:
                    new_connections.append(j)
            return Circuit(new_connections)

    def __eq__(self, value):
        return (self.nodes==value.nodes and self.distance==value.distance)
    
    def get_distance(self):
        return self.distance
    
    def __lt__(self,other):
        return self.distance < other.distance
    
    def a(self):
        return self.nodes[0]
    
    def b(self):
        return self.nodes[1]

f= open("AdventofCodeDay8.txt","r") 
all_points = []
i = 0
for row in f:
    x,y,z = row.split(",")[0],row.split(",")[1],row.split(",")[2]
    all_points.append(Point(int(x),int(y),int(z),i))
    i+=1

top_thousand_connections = []

current_row = 0
for i in all_points:
    for j in all_points[current_row:]:
        if i==j:
            pass
        else:
            if len(top_thousand_connections)<1000:
                top_thousand_connections.append(Circuit([i,j]))
                top_thousand_connections.sort()
            else:
                if i.distance(j)>top_thousand_connections[-1].get_distance():
                    pass
                else:
                    top_thousand_connections.append((Circuit([i,j])))
                    top_thousand_connections.sort()
                    top_thousand_connections = top_thousand_connections[0:1000]
    current_row+=1


def search_and_add(neighbors_list, current_point,root_point,checked_points):
    if current_point == root_point:
        print("broke loop")
        return neighbors_list,checked_points
    if len(neighbors_list[current_point])==1:
        checked_points[current_point] = True
        return neighbors_list,checked_points
    else:
        for i in neighbors_list[current_point]:
            if i not in neighbors_list[root_point]:
                neighbors_list[root_point].append(i)
                neighbors_list,checked_points = search_and_add(neighbors_list,i,root_point,checked_points)
        checked_points[current_point]=True
        return neighbors_list,checked_points
    
current_row = 0
merging_connections = []
merged = True
i = 0
j = 0

neighbors_list = {}
searched = dict.fromkeys(all_points,False)
i = 0
for i in all_points:
    neighbors_list[i]=[]

for i in top_thousand_connections:
    neighbors_list[i.a()].append(i.b())
    neighbors_list[i.b()].append(i.a())

total_connections = 0
for i in all_points:
    if i in neighbors_list:
        total_connections+=len(neighbors_list[i])

i = 0
for i in all_points:
    if searched[i]:
        pass
    else:
        for j in neighbors_list[i]:
            neighbors_list,searched = search_and_add(neighbors_list,j,i,searched)
    
j = []
for i in neighbors_list:
    j.append(len(neighbors_list[i]))
j = sorted(j)
print(j)
    
print("lets see how long this takes")
'''

i=0


while i < len(top_thousand_connections[:-1]):
    first_list = top_thousand_connections[i].current_nodes()
    merged = False
    while j < len(top_thousand_connections[i+1:]):
        second_list = top_thousand_connections[j].current_nodes()
        if not any(item in first_list for item in second_list):
            pass
        else:
            merging_connections.append(top_thousand_connections[i].merge_circuits(top_thousand_connections[j]))
            merged = True
        j+=1
    if not merged:
        merging_connections.append(top_thousand_connections[i])
    i+=1

any_merged = True


i=0
j=0
while any_merged:
    any_merged=False
    temp = []
    i=0
    j=0
    merging_len = len(merging_connections)
    while i < merging_len-1:
        first_list = merging_connections[i].current_nodes()
        j=i+1
        merged = False
        while j < merging_len:
            second_list = merging_connections[j].current_nodes()
            if not any(item in first_list for item in second_list):
                pass
            else:
                temp.append(merging_connections[i].merge_circuits(merging_connections[j]))
                any_merged = True
                merged = True
            j+=1
        if not merged:
            temp.append(merging_connections[i])
        i+=1

    print(merging_len)

    merging_connections = temp


for i in merging_connections:
    print(len(i.current_nodes()))
'''




f.close()
        
