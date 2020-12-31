
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
# experience = 3.277
experience = float(input())
def salaryCalculator(E, experience):
    salary = 0
    count = 0
    for element in E:
        salary += element*npy.power(experience, count)
        count += 1
    return salary
salary = salaryCalculator(E, experience)
print(salary)
# calculating regression coefficient
N = len(y)
y_bar = 0
for element in y:
    y_bar += element
y_bar = y_bar/N
S_t = 0
for element in y:
    S_t += (element - y_bar)*(element - y_bar)
S_r = 0
count = 0
while count<N:
    experience = x[count]
    salaryFromData = y[count]
    salaryPredicted = salaryCalculator(E, experience)
    S_r += (salaryFromData - salaryPredicted)*(salaryFromData - salaryPredicted)
    count += 1
r = (S_t - S_r)/S_t
print(r)
# Plotting the datapoints
mplot.scatter(x, y)
mplot.show()
