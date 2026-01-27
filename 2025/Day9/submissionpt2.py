import io
import numpy as np
import math

class Point:
    def __init__(self,x,y,id):
        self.id = id
        self.x = x
        self.y = y
        self.convex_concave = -1 #-1 refers to uninitialized 0 convex, 1 concave
        self.next = None
        self.prev = None
        self.direction = None
        self.possible = []  #Whether this point can be an upper right, upper left, lower right or lower left

    def area(self,other):
        return (abs(self.x-other.x)+1)*(abs(self.y-other.y)+1)
    def __eq__(self, value):
        return self.x==value.x and self.y==value.y
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def validate_bl(self, sorted_x,sorted_y):
        min_x = self.x
        min_y = self.y
        traveling_y = 0
        x_i = sorted_x.index(self)
        valid_points = []
        max_a =0
        while sorted_x[x_i].x == min_x:
            x_i+=1

        y_i = sorted_y.index(self)
        while sorted_y[y_i].y ==min_y:
            y_i-=1
        while y_i >=0:
            temp_x = sorted_y[y_i].x
            if temp_x<=min_x:
                if sorted_y[y_i].next.x > min_x:
                    traveling_y = sorted_y[y_i].y
                    break
            y_i-=1


        while x_i < len(sorted_x):
            temp_y = sorted_x[x_i].y
            if temp_y <min_y:
                if temp_y >= traveling_y:
                    valid_points.append(sorted_x[x_i])
                    traveling_y = temp_y
                if sorted_x[x_i].next.y >=min_y:
                    break
                x_i+=1
            else:
                x_i+=1
        if len(valid_points)>0:
            max_a = max(i.area(self) for i in valid_points)
        return max_a
    
    def validate_br(self,sorted_x,sorted_y):
        max_x = self.x
        min_y = self.y
        traveling_y = 0
        x_i = sorted_x.index(self)
        valid_points = []
        max_a = 0

        y_i = sorted_y.index(self)
        while sorted_y[y_i].y ==min_y:
            y_i-=1

        while y_i >=0:
            temp_x = sorted_y[y_i].x
            if temp_x<max_x:
                if sorted_y[y_i].next.x >= max_x:
                    traveling_y = sorted_y[y_i].y
                    break
            y_i-=1



        while sorted_x[x_i].x == max_x:
            x_i-=1
        while x_i >0:
            temp_y = sorted_x[x_i].y
            if temp_y <min_y:
                if temp_y >= traveling_y:
                    valid_points.append(sorted_x[x_i])
                    traveling_y = temp_y               
                if sorted_x[x_i].prev.y >=min_y:
                    break
                x_i-=1
            else:
                x_i-=1       
        if len(valid_points)>0:
            max_a = max(i.area(self) for i in valid_points)

        return max_a
    
    def validate_tl(self,sorted_x,sorted_y):
        min_x = self.x
        max_y = self.y
        traveling_y = math.inf
        valid_points = []
        max_a = 0

        y_i = sorted_y.index(self)
        while sorted_y[y_i].y ==max_y:
            y_i+=1
        while y_i <len(sorted_y):
            temp_x = sorted_y[y_i].x
            if temp_x<=min_x:
                if sorted_y[y_i].prev.x > min_x:
                    traveling_y = sorted_y[y_i].y
                    break
            y_i+=1
        
        x_i = sorted_x.index(self)
        while sorted_x[x_i].x ==min_x:
            x_i+=1
        
        while x_i < len(sorted_x):
            temp_y = sorted_x[x_i].y
            if temp_y >max_y:
                if temp_y <= traveling_y:
                    valid_points.append(sorted_x[x_i])
                    traveling_y = temp_y
                if sorted_x[x_i].prev.y <=max_y:
                    break
                x_i+=1
            else:
                x_i+=1
        if len(valid_points)>0:
            max_a = max(i.area(self) for i in valid_points)
        return max_a
    
    def validate_tr(self,sorted_x,sorted_y):
        min_x = self.x
        max_y = self.y
        traveling_y = math.inf
        valid_points = []
        max_a = 0
        x_i = sorted_x.index(self)
        valid_points = []

        y_i = sorted_y.index(self)
        while sorted_y[y_i].y ==max_y:
            y_i+=1
        while y_i <len(sorted_y):
            temp_x = sorted_y[y_i].x
            if temp_x>=min_x:
                if sorted_y[y_i].next.x < min_x:
                    traveling_y = sorted_y[y_i].y
                    break
            y_i+=1
        while sorted_x[x_i].x ==min_x:
            x_i-=1
        while x_i >0:
            temp_y = sorted_x[x_i].y
            if temp_y >max_y:
                if temp_y <= traveling_y:
                    valid_points.append(sorted_x[x_i])
                    traveling_y = temp_y               
                if sorted_x[x_i].next.y <=max_y:
                    break
                x_i-=1
            else:
                x_i-=1
        if len(valid_points)>0:
            max_a = max(i.area(self) for i in valid_points)
        return max_a


class Line:
    def __init__(self,p1,p2,id):
        self.id=id
        self.p1 = p1
        self.p2 = p2
        self.vertical = (p1.x==p2.x)
        self.horizontal = (p1.y==p2.y)


    def intersect_corner(self,other): #This is searching the given data to see if there are any line intersections
        if self.p1==other.p1 or self.p2==other.p2 or self.p1==other.p2 or self.p2==other.p1:
            return True
        else:
            return False
    def intersect_parallel(self,other):
        if self.horizontal:
            if other.horizontal:
                if self.p1.y ==other.p1.y:
                    if self.p1.x<other.p1.x and self.p2.x < other.p1.x and self.p1.x<other.p2.x and self.p2.x < other.p2.x:
                        return False
                    elif self.p1.x>other.p1.x and self.p2.x > other.p1.x and self.p1.x>other.p2.x and self.p2.x > other.p2.x:
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False
        else:
            if other.vertical == self.vertical:
                if self.p1.x ==other.p1.x:
                    if self.p1.y<other.p1.y and self.p2.y < other.p1.y and self.p1.y<other.p2.y and self.p2.y < other.p2.y:
                        return False
                    elif self.p1.y>other.p1.y and self.p2.y > other.p1.y and self.p1.y>other.p2.y and self.p2.y > other.p2.y:
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False        
    def intersect_perp(self,other):
        if self.horizontal:
            if other.vertical:
                if self.p1.x<other.p1.x<self.p2.x or self.p1.x>other.p1.x>self.p2.x:
                    if other.p1.y<self.p1.y<other.p2.y or other.p1.y>self.p1.y>other.p2.y:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif self.vertical:
            if other.horizontal:
                if self.p1.y<other.p1.y<self.p2.y or self.p1.y>other.p1.y>self.p2.y:
                    if other.p1.x<self.p1.x<other.p2.x or other.p1.x>self.p1.x>other.p2.x:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


f= open("AdventofCodeDay9.txt","r") #through exploring the code, no 3-pt straight lines exist,
all_points = [] #and there are no line intersections, or shared end points. This significantly simplifies the problem.
i = 0
prev_point = Point(-5,-5,-5)
for row in f:
    x,y = row.split(",")[0],row.split(",")[1]
    new_point = Point(int(x),int(y),i)
    prev_point.next = new_point
    new_point.prev = prev_point
    all_points.append(new_point)
    prev_point = new_point
    i+=1
new_point.next = all_points[0]
all_points[0].prev = new_point
lowest_x = all_points[0]
highest_x = all_points[0]
lowest_y = all_points[0]
highest_y = all_points[0]

potential_alt_lows = []
for i in all_points:
    if i.x <lowest_x.x:
        lowest_x = i
        potential_alt_lows = []
    elif i.x ==lowest_x.x:
        potential_alt_lows.append(i)
    if i.x > highest_x.x:
        highest_x = i
    if i.y < lowest_y.y:
        lowest_y = i
    if i.y > highest_y.y:
        highest_y =i

convex_iter = -1
potential_alt_lows.append(lowest_x)


bottom_left_corner = max(potential_alt_lows, key = lambda i:i.y)

sorted_x = sorted(all_points,key = lambda i:i.x)

sorted_y = sorted(all_points,key= lambda i:i.y)



current_node = bottom_left_corner
direction = "W"
#current_node.convex_concave = 0 #convex = 0 concave = 1

while current_node.convex_concave == -1:
    prev_node = current_node
    current_node = current_node.next
    if direction == "E":
        if current_node.y<prev_node.y:
            prev_node.direction = "N"
            direction = "N"
            prev_node.convex_concave = 1
            prev_node.possible.append("tl")
            prev_node.possible.append("tr")
            prev_node.possible.append("bl")
        elif current_node.y > prev_node.y:
            prev_node.direction = "S"
            direction = "S"
            prev_node.convex_concave = 0
            prev_node.possible.append("tr")
    elif direction =="N":
        if current_node.x>prev_node.x:
            direction = "E"
            prev_node.direction = "E"
            prev_node.convex_concave = 0
            prev_node.possible.append("tl")
        elif current_node.x < prev_node.x:
            direction = "W"
            prev_node.direction = "W"
            prev_node.convex_concave = 1
            prev_node.possible.append("tl")
            prev_node.possible.append("bl")
            prev_node.possible.append("br")
    elif direction =="W":
        if current_node.y<prev_node.y:
            direction = "N"
            prev_node.direction = "N"
            prev_node.convex_concave = 0
            prev_node.possible.append("bl")
        elif current_node.y > prev_node.y:
            direction = "S"
            prev_node.direction = "S"
            prev_node.convex_concave = 1
            prev_node.possible.append("tr")
            prev_node.possible.append("br")
            prev_node.possible.append("bl")
    elif direction =="S":
        if current_node.x>prev_node.x:
            direction = "E"
            prev_node.direction = "E"
            prev_node.convex_concave = 1
            prev_node.possible.append("tr")
            prev_node.possible.append("tl")
            prev_node.possible.append("br")
        elif current_node.x < prev_node.x:
            direction = "W"
            prev_node.direction = "W"
            prev_node.convex_concave = 0
            prev_node.possible.append("br")

i = 0

print("total pairs without constraint: ",len(all_points)*len(all_points))

temp_values = 0
max_area = 0
pts = 0
for i in all_points:
    for j in i.possible:
        temp_max = 0
        if j =="br":
            temp_max =i.validate_br(sorted_x,sorted_y)
        elif j =="bl":
            temp_max =i.validate_bl(sorted_x,sorted_y)
        elif j == "tl":
            temp_max = i.validate_tl(sorted_x,sorted_y)
        elif j == "tr":
            temp_max = i.validate_tr(sorted_x,sorted_y)
        else:
            print("Invalid type of corner")
        if temp_max>max_area:
            max_area = temp_max
    pts+=1

print("Max area:", max_area)

f.close()