import numpy as np
from scipy.integrate import odeint
import plotly.express as px
import pandas as pd

r = 28.0
sigma = 10.0
b = 8.0 / 3.0
t_min = 0
t_max = 100
t_step = .000001
counter = 0

values = np.empty((0, 2))
state0 = [1.0, 1.0, 1.0]
t = np.arange(t_min, t_max, t_step)
prev_z_1 = 0
prev_z_2 = 0
prev_max = 0
extrema = False

def f(state, t):
    global prev_z_1
    global prev_z_2
    global prev_max
    global extrema
    global values
    x, y, z = state  # Unpack the state vector
    if -10 < x * y - b * z < 10:
        extrema = True
    elif prev_z_1 < prev_z_2 and z < prev_z_2 and extrema and prev_max != 0:
        values = np.append(values, np.array([[prev_max, z]]), axis=0)
        prev_max = z
    elif prev_z_1 < prev_z_2 and z < prev_z_2 and extrema:
        prev_max = z
    else:
        extrema = False
    prev_z_1 = prev_z_2
    prev_z_2 = z
    return sigma * (y - x), x * (r - z) - y, x * y - b * z  # Derivatives


states = odeint(f, state0, t)

df = pd.DataFrame({"z_{n}": values[:, 0], "z_{n+1}": values[:, 1]})
fig = px.scatter(df, x="z_{n}", y="z_{n+1}")
fig.show()