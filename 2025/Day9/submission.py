import io
import numpy as np
import math

class Point:
    def __init__(self,x,y,id):
        self.id = id
        self.x = x
        self.y = y
    
    def area(self,other):
        return abs(self.x-other.x+1)*abs(self.y-other.y+1)



f= open("AdventofCodeDay9.txt","r") 
all_points = []
i = 0
for row in f:
    x,y = row.split(",")[0],row.split(",")[1]
    all_points.append(Point(int(x),int(y),i))
    i+=1

sorted_x = sorted(all_points, key = lambda Point:Point.x)
sorted_y = sorted(all_points,key=lambda Point:Point.y)

upper_left_quad =[]
upper_right_quad = []
lower_left_quad = []
lower_right_quad = []

min_y = sorted_x[0].y
max_y = sorted_x[0].y


for i in sorted_x:
    if i.y >= max_y:
        upper_left_quad.append(i)
        max_y = i.y
    if i.y <= min_y:
        lower_left_quad.append(i)
        min_y = i.y

min_y = sorted_x[-1].y
max_y = sorted_x[-1].y
for j in reversed(sorted_x):
    if j.y>=max_y:
        upper_right_quad.append(j)
        max_y = j.y
    if j.y<= min_y:
        lower_right_quad.append(j)
        min_y = j.y

print("lenur,ul,ll,lr",len(upper_right_quad))
print(len(upper_left_quad))
print(len(lower_left_quad))
print(len(lower_right_quad))
max_area = upper_left_quad[0].area(lower_right_quad[0])

for i in upper_left_quad:
    for j in lower_right_quad:
        if i.area(j)>max_area:
            max_area = i.area(j)

for i in upper_right_quad:
    for j in lower_left_quad:
        if i.area(j)>max_area:
            max_area=i.area(j)
print(max_area)
f.close()
        
