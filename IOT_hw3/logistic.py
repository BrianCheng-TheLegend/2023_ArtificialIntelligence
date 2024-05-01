# use logistic regression to approximate OR function
import numpy as np

# OR function
x1 = [0, 1, 0, 1]
x2 = [0, 0, 1, 1]
y = [0, 1, 1, 1]

# initial variables
w1 = 2
w2 = 2
b =-2
learning_rate = 0.5

# initial logistic function
z1 = [0]*4
y_hat = [0]*4
y_minus = [0]*4

# iterations
iterations = 2

for iteration in range(iterations):
    for i in range(4):
        z1[i] = w1 * x1[i] + w2 * x2[i] + b
        y_hat[i] = 1/(1+np.exp(-z1[i]))
        y_minus[i] = y_hat[i]  - y[i] 
    
    # update w1 w2 b
    w1 = w1 -learning_rate * sum(np.multiply(y_minus,x1))
    w2 = w2 -learning_rate * sum(np.multiply(y_minus,x2))
    b = b -learning_rate * sum(y_minus)

    # print iterations, last y hat, updated w1
    print("Iteration : ",(iteration+1))
    print("Previous iteration y hat = ", y_hat)
    print("Update w1 = ", w1)
    print("Update w2 = ", w2)
    print("Update b = ", b)

    for i in range(4):
        z1[i] = w1 * x1[i] + w2 * x2[i] + b
        y_hat[i] = 1/(1+np.exp(-z1[i]))
    print("Update y hat = ", y_hat)


### expect result
# Iteration :  1
# Previous iteration y hat =  [0.11920292202211755, 0.5, 0.5, 0.8807970779778823]
# Update w1 =  2.309601461011059
# Update w2 =  2.309601461011059
# Update b =  -1.5
# Update y hat =  [0.18242552380635635, 0.6920245715574536, 0.6920245715574536, 0.9576779336458453]
# Iteration :  2
# Previous iteration y hat =  [0.18242552380635635, 0.6920245715574536, 0.6920245715574536, 0.9576779336458453]
# Update w1 =  2.4847502084094093
# Update w2 =  2.4847502084094093
# Update b =  -1.2620763002835544
# Update y hat =  [0.2206166757677421, 0.7725337652398471, 0.7725337652398471, 0.9760471625441138]
###