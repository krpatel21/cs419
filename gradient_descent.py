# import numpy as np
#
# x = np.array([1,2,3])
# y = np.array([-7,8,9])
# print np.dot(x,y)
# # x = np.matrix(((1,3), (4, 0), (2, 1)))
# # y = np.matrix(((1),(5)))
#
# x = np.matrix(((1,3,2),(4,0,1)))
# y = np.matrix(((1,3),(0,1),(5,2)))
# print x * y
#
# x = np.matrix(((1,3,2),(4,0,1)))
# y = np.matrix('1;0;5')
# print x * y
import math

LEARNING_RATE = 0.0002
summer = [38, 43, 35, 69]
fall = [75, 80, 65, 144]
spring = [70, 70, 96, 137]


def gradient_descent(x1, x2, y, theta, theta1, theta2, iterations):
    if iterations == 0:
        return
    n = len(x1)
    sum = 0

    for i in range(n):
        sum += theta + theta1 * x1[i] + theta2 * x2[i] - y[i]
    temp1 = theta - LEARNING_RATE * (1 / float(n)) * sum
    sum = 0

    for i in range(n):
        sum += (theta + theta1 * x1[i] + theta2 * x2[i] - y[i]) * x1[i]
    temp2 = theta1 - LEARNING_RATE * (1 / float(n)) * sum
    sum = 0

    for i in range(n):
        sum += (theta + theta1 * x1[i] + theta2 * x2[i] - y[i]) * x2[i]
    temp3 = theta2 - LEARNING_RATE * (1 / float(n)) * sum

    theta = temp1
    theta1 = temp2
    theta2 = temp3

    print theta, theta1, theta2
    gradient_descent(x1, x2, y, theta, theta1, theta2, iterations-1)

gradient_descent(summer, fall, spring, 0, 10, 10, 600)

print math.pow(10, -3)