import numpy as np
from scipy.integrate import odeint
import plotly.express as px
import pandas as pd

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0


def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives


state0 = [100.0, 100.0, 1.0]
t = np.arange(0.0, 550.0, 0.0005)


states = odeint(f, state0, t)

df = pd.DataFrame({"Convection Rate": states[:, 0], "Horizontal Temperature Variation": states[:, 1], "Vertical Temperature Variation": states[:, 2], "time": t})
fig = px.scatter_3d(df, x="Convection Rate", y="Horizontal Temperature Variation", z="Vertical Temperature Variation", color="time")
fig.show()