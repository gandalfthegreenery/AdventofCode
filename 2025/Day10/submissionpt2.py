import io
import numpy as np
import math


class switch:
    id = -1
    lights = []
    def __init__(self, id,lights):
        self.id = id
        self.lights = lights

    def ret_id(self):
        return self.id
    def ret_lights(self):
        return self.lights
    def __str__(self):
        return "Id:"+str(self.id)+"lights: "+str(self.lights)
    def __repr__(self):
        return "Id:"+str(self.id)+"lights: "+str(self.lights)
    

def parse_line_to_matricies(input_string):
    joltage_requirements = []
    str_num = 0
    button_num = len(input_string.split(" "))-2
    light_num = len(input_string.split(" ")[-1].split(","))
    temp_j = input_string.split(" ")[-1].strip("{}\n").split(",")
    joltage_requirements=[int(k) for k in temp_j]
    switch_arr = []
    for i in input_string.split(" "):
        if i[0]=="(":
            temp = i.strip("()").split(",")
            temp_arr = [0]*light_num
            for light in temp:
                temp_arr[int(light)]=1
            switch_arr.append(temp_arr)
        else:
            pass
    return switch_arr,joltage_requirements

def rref(reqs,switches):
    num_equations = len(reqs)
    pivot_row=0
    if len(switches[0])!=num_equations:
        print("Error, number of equations should equal number of reqs")
    switches = np.array(switches,dtype=float)
    reqs = np.array(reqs,dtype=float)
    work_arr = switches.T
    reqs = reqs.reshape((work_arr.shape[0],1))
    work_arr = np.append(work_arr,reqs,1)
    pivot_col = 0
    while pivot_col < len(work_arr[0])-1 and pivot_row<num_equations:
        #identify pivot row:
        max_row = np.argmax(abs(work_arr[pivot_row:,pivot_col]))+pivot_row
        if abs(work_arr[max_row,pivot_col]) < 1e-7:
            pivot_col+=1
            continue
        work_arr[[pivot_row,max_row]]=work_arr[[max_row,pivot_row]]
        work_arr[pivot_row]/=work_arr[pivot_row,pivot_col]
        col = work_arr[:,pivot_col].copy()
        col[pivot_row]=0
        work_arr -=col[:,None]*work_arr[pivot_row]
        pivot_row+=1
        pivot_col+=1
    work_arr[abs(work_arr)<1e-7] =0
    return work_arr

def free_variables(matrix):
    piv_var = []
    piv_row = []
    m, n = np.shape(matrix)
    for r in range(m):
        row = matrix[r,:-1]
        non_zero = np.where(np.abs(row)>1e-8)
        if len(non_zero[0])==0:
            continue
        pivot = non_zero[0][0]
        if abs(matrix[r,pivot]-1)<1e-8:
            piv_var.append(pivot)
            piv_row.append(r)
    free_variables = []
    for col in range(n-1):
        if int(col) in piv_var:
            continue
        free_variables.append(col)
    return free_variables, piv_var, piv_row


f= open("AdventofCodeDay10.txt","r") 
total_switches = 0

def max_buttons(reqs,switches):
    switches = np.array(switches)
    reqs = np.array(reqs)
    work_arr = switches.T
    reqs = np.tile(reqs[:,None],len(work_arr[0]))
    m = np.multiply(reqs,work_arr)
    m = np.min(np.where(m > 0, m, np.inf),axis=0)
    m = np.round(m).astype(int)
    return m


def pivot_vars_from_free(b,A_f,x_f):
    return b - np.matmul(A_f,x_f)

for row in f:
    switches,reqs = parse_line_to_matricies(row)
    rref_matrix=rref(reqs,switches)
    m,n = np.shape(rref_matrix)
    n=n-1
    #print(rref_matrix)
    free_vars, piv_vars,piv_row = free_variables(rref_matrix)
    #print(free_vars)
    A_p = rref_matrix[:,piv_vars]
    A_f = rref_matrix[:,free_vars]
    b=rref_matrix[:,-1]
    x_0 = np.zeros(n)
    x_0[piv_vars]=b[piv_row]

    V = np.zeros((n, len(free_vars)))

    if len(free_vars)==0:
        total_switches +=np.sum(b)
        continue

    for i, free_col in enumerate(free_vars):
        V[free_col, i] = 1
        V[piv_vars, i] = -A_f[piv_row, i]

    minimum_sum = np.inf

    free_vars = np.round(free_vars).astype(int)
    
    if len(free_vars)==1:
        max_values= max_buttons(reqs,switches)
        bound = max(max_values)
        for i in range(-bound,bound+1):
            t = np.array([i])
            x = x_0+V@t
            if not np.allclose(x,np.round(x)):
                continue
            x = np.round(x).astype(int)
            if np.any(x<0):
                continue
            if any(x>max_values):
                continue
            sum = np.sum(x)
            if sum<minimum_sum:
                minimum_sum=sum

    elif len(free_vars)==2:
        max_values= max_buttons(reqs,switches)
        bound = max(max_values)
        for i in range(-bound,bound+1):
            for j in range(-bound,bound+1):
                t = np.array([i,j])
                x = x_0+V@t
                if not np.allclose(x,np.round(x)):
                    continue
                x = np.round(x).astype(int)
                if np.any(x<0):
                    continue
                if any(x>max_values):
                    continue
                sum = np.sum(x)
                if sum<minimum_sum:
                    minimum_sum=sum
    elif len(free_vars)==3:
        max_values= max_buttons(reqs,switches)
        bound = max(max_values)
        for i in range(-bound,bound+1):
            for j in range(-bound,bound+1):
                for k in range(-bound,bound+1):
                    t = np.array([i,j,k])
                    x = x_0+V@t
                    if not np.allclose(x,np.round(x)):
                        continue
                    x = np.round(x).astype(int)
                    if np.any(x<0):
                        continue
                    if any(x>max_values):
                        continue
                    sum = np.sum(x)
                    if sum<minimum_sum:
                        minimum_sum=sum
    else:
        print("more than 3 free variables")
    total_switches+=minimum_sum

print(total_switches)

print(total_switches)
f.close()
        
