import numpy as np
from scipy.integrate import odeint
import plotly.express as px
import pandas as pd

sigma = 10
b = 8/3
r_min = 0
r_max = 150
r_step = .05
t_min = 0
t_max = 30
t_step = .001
counter = 0

values = np.zeros([2000000, 2])
r_vals = np.arange(r_min, r_max, r_step)
state0 = [1.0, 1.0, 1.0]
t = np.arange(t_min, t_max, t_step)
counter = 0

def f(state, t):
    global values
    global counter
    x, y, z = state  # Unpack the state vector
    if counter > values.size / 2:
        print("MEMORY EXCEEDED")
    if -7.5 < x * y - b * z < 7.5 and t > 2:
        values[counter][0] = r
        values[counter][1] = z
        counter += 1
    return sigma * (y - x), x * (r - z) - y, x * y - b * z  # Derivatives


for r in r_vals:
    if r % 1 == 0:
        print(r)
    states = odeint(f, state0, t)


df = pd.DataFrame({"r": values[:, 0], "z": values[:, 1]})
fig = px.scatter(df, x="r", y="z")
fig.update_traces(marker_size=1)
fig.show()