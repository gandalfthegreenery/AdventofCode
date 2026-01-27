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
                if i not in new_connections:
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


def count(list):
    i = 0
    for j in list:
        if j:
            i+=1
    return i



f= open("AdventofCodeDay8.txt","r") 
all_points = []
i = 0
for row in f:
    x,y,z = row.split(",")[0],row.split(",")[1],row.split(",")[2]
    all_points.append(Point(int(x),int(y),int(z),i))
    i+=1

top_n_connections = []
current_row = 0
for i in all_points:
    for j in all_points[current_row:]:
        if i==j:
            pass
        else:
            if len(top_n_connections)<10000:
                top_n_connections.append(Circuit([i,j]))
                top_n_connections.sort()
            else:
                if i.distance(j)>top_n_connections[-1].get_distance():
                    pass
                else:
                    top_n_connections.append((Circuit([i,j])))
                    top_n_connections.sort()
                    top_n_connections = top_n_connections[0:10000]
    current_row+=1


searched = dict.fromkeys(all_points)
j=0
for i in searched:
    searched[i]=j
    j+=1

i=0
print(searched)

while(i<len(top_n_connections)):
    
    if all(value ==0 for value in searched.values()):
        print(a)
        print(b)
        break
    else:
        print(count(value==0 for value in searched.values()))
    a = top_n_connections[i].a()
    b = top_n_connections[i].b()

    if searched[a]==searched[b]:
        pass
    else:
        temp = max(searched[a],searched[b])
        min_g = min(searched[a],searched[b])
        searched[a]=min_g
        searched[b]=min_g
        for j in searched:
            if searched[j] == temp:
                searched[j]= min_g
    i+=1
    print(i)



f.close()
        
