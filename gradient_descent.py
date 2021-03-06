import math

LEARNING_RATE = 0.1
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

gradient_descent(summer, fall, spring, 0, 10, 10, 20)

x1 = [1, 1, 0, 0]
x2 = [1, 0, 1, 0]
y= [1, 0, 0, 0]

