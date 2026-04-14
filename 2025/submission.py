import io
import numpy as np
import math
class switch:
    id = -1
    lights = []
    def __init__(self, id,lights):
        self.id = id
        self.lights = frozenset(lights)

    def ret_id(self):
        return self.id
    def ret_lights(self):
        return self.lights
    def __str__(self):
        return "Id:"+str(self.id)+"lights: "+str(self.lights)
    
def parse_line(input_string):
    button_requirements = []
    switch_options = []
    joltage_reqs = []
    str_num = 0
    for i in input_string.split(" "):
        j = 0
        if i[j]=="[":
            while j<len(i):
                if i[j]=="#":
                    button_requirements.append(str(j-1))
                j+=1
        elif i[j]=="(":
            switch_options.append(switch(id = str_num,lights = i[1:len(i)-1].split(",")))
            str_num+=1
        else:
            pass
    return frozenset(button_requirements),switch_options,joltage_reqs

def bsf(reqs,switches):
    presses = 1
    states = {} #key is current lights on and off, value is switch ids already clicked
    k = True
    for i in switches:
        states[i.ret_lights()]=[i]
        if i.ret_lights() ==reqs:
            return 1
    while k:
        new_states = {}
        presses+=1
        for i in states.keys():
            for j in switches:
                if j not in states[i]:
                    candidate = i^j.ret_lights()
                    if candidate ==reqs:
                        return presses
                    else:
                        new_states[candidate] = states[i]+[j]
        states = new_states
    return presses

f= open("AdventofCodeDay10.txt","r") 
total_switches = 0

for row in f:
    reqs,switches,jolt = parse_line(row)
    if len(reqs)==0:
        pass
    print(total_switches)
    total_switches+=bsf(reqs,switches)

print(total_switches)
f.close()
        
