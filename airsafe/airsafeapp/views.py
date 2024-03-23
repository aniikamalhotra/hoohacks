from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def index(request):
    return HttpResponse("Hello! Welcome to the AirSafe App!")


def interpolateBspline(x, y, xi):
    yi = []
    A = y
    for i in xi:
        #if x[0] <= i <= x[1]:
        index = 0
        while x[index] < i:
            index += 1
        if x[index] == i:
            yi.append(y[index])
        else:
            yi.append(y[index - 1] + (i - x[index - 1]) * (y[index] - y[index - 1]) / (x[index] - x[index - 1]))
        # else:
        #     yi.append(None)
    return yi, A


def interpolatePoly(x, y, xi):
    aVal = len(x)
    if aVal != len(y):
        raise ValueError("Error: x and y must have the same number of elements")

    A = np.zeros((aVal, aVal))

    for i in range(aVal):
        A[:, i] = x ** i

    co = np.linalg.solve(A, y)

    yi = np.polyval(co[::-1], xi)

    return yi, co


df = pd.read_csv("cardiacMRIdata.csv")
time = df.loc[:, "Time (ms)"]
baseline = df.loc[:, "Baseline"]
dobutamine = df.loc[:, "Dobutamine"]

f, axes = plt.subplots(3, 1)
axes[0].plot(time, dobutamine, '.-')
axes[0].set_ylabel('Volume')

# calculates times at which to interpolate
tInterpolated = np.linspace(np.min(time), np.max(time), 100)
yiP, aP = interpolatePoly(time, dobutamine, tInterpolated)
axes[1].plot(tInterpolated, yiP, '.-')
axes[1].set_ylabel('Volume')

yiB, aB = interpolateBspline(time, dobutamine, tInterpolated)
axes[2].plot(tInterpolated, yiB, '.-')
axes[2].set_ylabel('Volume')


plt.show(block=True)
plt.interactive(False)
