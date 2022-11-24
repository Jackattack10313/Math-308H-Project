import numpy as np
from scipy.integrate import odeint
import plotly.express as px
import pandas as pd

r = 28.0
sigma = 10.0
b = 8.0 / 3.0


def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (r - z) - y, x * y - b * z  # Derivatives


state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 100.0, 0.0005)


states = odeint(f, state0, t)
print(states)

df = pd.DataFrame({"Convection Rate": states[:, 0], "Horizontal Temperature Variation": states[:, 1], "Vertical Temperature Variation": states[:, 2], "time": t})
fig = px.scatter_3d(df, x="Convection Rate", y="Horizontal Temperature Variation", z="Vertical Temperature Variation", color="time")
fig.show()