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


state0 = [2.0, 3.0, -14.0]
state1 = [2 + 10e-16, 3, -14.0]
t = np.arange(0.0, 25.0, 0.0001)


states_1 = odeint(f, state0, t)
states_2 = odeint(f, state1, t)
intermediate = (np.array(states_1) - np.array(states_2))
delta = np.zeros(t.size)
for i in range(t.size):
    delta[i] = np.linalg.norm(intermediate[i])
delta = np.emath.log(delta)

df = pd.DataFrame({"t": t, "delta": delta})
fig = px.scatter(df, x="t", y="delta", trendline="ols")
fig.update_traces(marker_size=2)
fig.show()
results = px.get_trendline_results(fig)
print(results.px_fit_results.iloc[0].summary())
