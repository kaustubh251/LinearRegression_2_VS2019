
import matplotlib as mplot
import numpy as npy
file1 = open("Salary_Data.csv","rt")
z = file1.read()
Z = z.split()
Z1 = []
for element in Z:
    Z1.append(element.split(','))
N_ele = len(Z1)
count = N_ele
x = []
y = []
while count>1:
    x.append(float(Z1[count-1][0]))
    y.append(float(Z1[count-1][1]))
    count-=1
A = []
for element in x:
    arr = [1, element, element*element, element*element*element]
    A.append(arr)
A_T = npy.transpose(A)
B = npy.matmul(A_T, A)
C = npy.matmul(A_T, y)
D = npy.linalg.inv(B)
E = npy.matmul(D, C)
experience = float(input())
salary = 0
count = 0
for element in E:
    salary += element*npy.power(experience, count)
    count += 1
print(salary)