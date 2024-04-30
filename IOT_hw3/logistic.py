# use logistic regression to approximate OR function
import numpy as np

x1 = [0, 1, 0, 1]
x2 = [0, 0, 1, 1]
y = [0, 1, 1, 1]

w1 = 2
w2 = 2
b =-2
learning_rate = 0.5

z1 = [0]*4
y1_old = [0]*4
y1_new = [0]*4
y1_minus = [0]*4
sigma_y1_minus_x1 = 0
sigma_y1_minus_x2 = 0
sigma_y1_minus = 0
w11_new = 0
w21_new = 0
b1_new = 0

for i in range(4):
    z1[i] = w1 * x1[i] + w2 * x2[i] + b
    y1_old[i] = 1/(1+np.exp(-z1[i]))
    y1_minus[i]  = y1_old[i]  - y[i] 
    sigma_y1_minus_x1 += y1_minus[i]*x1[i]
    sigma_y1_minus_x2 += y1_minus[i]*x2[i]
    sigma_y1_minus += y1_minus[i]

print("y1 = ", y1_old)
print("y1_minus = ", y1_minus)
print("sigma_y1_minus_x1 = ", sigma_y1_minus_x1)
print("sigma_y1_minus_x2 = ", sigma_y1_minus_x2)
print("sigma_y1_minus = ", sigma_y1_minus)

w11_new = w1 - learning_rate * sigma_y1_minus_x1
w21_new = w2 - learning_rate * sigma_y1_minus_x2
b1_new = b - learning_rate * sigma_y1_minus
print("w11_new = ", w11_new)
print("w21_new = ", w21_new)
print("b1_new = ", b1_new)

# variable after 1 iteration
w1 = w11_new; w2 = w21_new; b = b1_new
z1 = [0]*4
y1_old = [0]*4

for i in range(4):
    z1[i] = w1 * x1[i] + w2 * x2[i] + b
    y1_old[i] = 1/(1+np.exp(-z1[i]))
    

print("y1 = ", y1_old)

# 2 iteration
y1_new = [0]*4
y1_minus = [0]*4
sigma_y1_minus_x1 = 0
sigma_y1_minus_x2 = 0
sigma_y1_minus = 0
w11_new = 0
w21_new = 0
b1_new = 0

for i in range(4):
    y1_minus[i]  = y1_old[i]  - y[i] 
    sigma_y1_minus_x1 += y1_minus[i]*x1[i]
    sigma_y1_minus_x2 += y1_minus[i]*x2[i]
    sigma_y1_minus += y1_minus[i]

print("y1 = ", y1_old)
print("y1_minus = ", y1_minus)
print("sigma_y1_minus_x1 = ", sigma_y1_minus_x1)
print("sigma_y1_minus_x2 = ", sigma_y1_minus_x2)
print("sigma_y1_minus = ", sigma_y1_minus)

w11_new = w1 - learning_rate * sigma_y1_minus_x1
w21_new = w2 - learning_rate * sigma_y1_minus_x2
b1_new = b - learning_rate * sigma_y1_minus
print("w11_new = ", w11_new)
print("w21_new = ", w21_new)
print("b1_new = ", b1_new)

# variable after 2 iteration
w1 = w11_new; w2 = w21_new; b = b1_new
z1 = [0]*4
y1_old = [0]*4

for i in range(4):
    z1[i] = w1 * x1[i] + w2 * x2[i] + b
    y1_old[i] = 1/(1+np.exp(-z1[i]))

print("y1 = ", y1_old)