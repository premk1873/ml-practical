Aim: For a given set of training data examples stored in a .CSV file
implement least square algorithm.

def calculateB(x, y, n):
    sx = sum(x)
    sy = sum(y)
    sxsy = 0
    sx2 = 0

    for i in range(n):
        sxsy += x[i] * y[i]
        sx2 += x[i] * x[i]

    b = (n * sxsy - sx * sy) / (n * sx2 - sx * sx)
    return b


def leastRegLine(X, Y, n):
    b = calculateB(X, Y, n)
    meanX = sum(X) / n
    meanY = sum(Y) / n

    a = meanY - b * meanX

    print("Regression line:")
    print("Y = ", '%.3f' % a, " + ", '%.3f' % b, "*X", sep="")


import pandas as pd

datas = pd.read_csv('C:/Users/Lenovo/Downloads/data.csv')
print(datas)

X = datas.TEMPERATURE
Y = datas.PRESSURE
n = len(X)

leastRegLine(X, Y, n)
