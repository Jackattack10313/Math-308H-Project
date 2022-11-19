import pandas as pd
import plotly.express as px
import numpy as np
from sys import maxsize
from math import pow

sigma = 10
r = 28
b = 8 / 3
stepSize = 1
iterations = int(input("Enter the number of iterations: "))
allowedError = float(input("Enter the truncation error: "))
xInitial = float(input("Enter the initial rate of convection - x: "))
yInitial = float(input("Enter the initial horizontal temperature variation - y: "))
zInitial = float(input("Enter the vertical temperature variation - z: "))


def functionEval(function, xn, yn, zn):
    x, y, z = xn, yn, zn
    return eval(function)


def RK45(function, xn, yn, zn):
    global stepSize
    error = maxsize
    while error > allowedError:
        k1 = stepSize * functionEval(function, xn, yn, zn)
        k3 = stepSize * functionEval(function, xn + 1/3 * stepSize, yn + 1/3 * stepSize, zn + 1/3 * stepSize)
        k4 = stepSize * functionEval(function, xn + 3/4 * stepSize, yn + 3/4 * stepSize, zn + 3/4 * stepSize)
        k5 = stepSize * functionEval(function, xn * stepSize, yn * stepSize, zn * stepSize)
        k6 = stepSize * functionEval(function, xn * 5/6 * stepSize, yn * 5/6 * stepSize, zn * 5/6 * stepSize)
        error = abs(-1/150 * k1 + 3/100 * k3 - 16/75 * k4 - 1/20 * k5 + 6/25 * k6)
        if error > allowedError:
            stepSize = 0.9 * stepSize * pow(allowedError/error, 1/5)
    return 47/450 * k1 + 12/25 * k3 + 32/225 * k4 + 1/30 * k5 + 6/25 * k6


x = np.array([xInitial])
y = np.array([yInitial])
z = np.array([zInitial])
time = np.array([0])

for i in range(iterations):
    if i % 1000 == 0:
        print(i)
    z = np.append(z, [RK45("x*y-b*z", x[i], y[i], z[i]) + z[i]])
    y = np.append(y, [RK45("x*(r-z)-y", x[i], y[i], z[i]) + y[i]])
    x = np.append(x, [RK45("sigma*(y-x)", x[i], y[i], z[i]) + x[i]])
    time = np.append(time, [time[i] + stepSize])

df = pd.DataFrame({"Convection Rate": x, "Horizontal Temperature Variation": y, "Vertical Temperature Variation": z,
                   "time": time})
fig = px.scatter_3d(df, x="Convection Rate", y="Horizontal Temperature Variation", z="Vertical Temperature "
                                                                                     "Variation", color="time")
fig.show()
