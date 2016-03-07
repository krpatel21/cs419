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


def perceptron(x1, x2, y, weight, weight1, weight2, i):
    if i == 4:
        i = 0

    o = 1 * weight + x1[i] * weight1 + x2[i] * weight2
    if o > 0:
        o = 1
    else:
        o = -1

    delta_w = LEARNING_RATE * (y[i] - o)
    delta_w1 = LEARNING_RATE * (y[i] - o) * x1[i]
    delta_w2= LEARNING_RATE * (y[i] - o) * x2[i]

    weight = weight + delta_w
    weight1 = weight1 + delta_w1
    weight2 = weight2 + delta_w2

    i = i+1

    print "delta w", delta_w, delta_w1, delta_w2
    print "weights", weight, weight1, weight2
    print

    perceptron(x1, x2, y, weight, weight1,weight2, i)

perceptron(x1, x2, y, 0.2, 0.1, 0.4, 0)