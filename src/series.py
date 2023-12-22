import numpy as np


def skew_tent_map(n=2**15, omega=0.1847, x0=.5):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, len(x)):
        if x[i-1] < omega:
            x[i] = x[i-1]/omega
        else:
            x[i] = (1-x[i-1])/(1-omega)
    return x


def logistic_map(n=2**15, r=4, x0=.4):
    x = np.zeros(n)
    x[0] = x0
    for i in range(n-1):
        x[i+1] = r*x[i]*(1-x[i])
    return x


def schuster_map(n=2**15, z=2.0, x0=.5):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i], _ = np.modf(x[i-1] + x[i-1]**z)
    return x


# there was a mistake in original implementation of Henon map
def henon_map(n=1000000, a=1.4, b=0.3, x0=.4, y0=.4):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = y0
    y[0] = x0
    for i in range(2, len(x)):
        x[i] = 1 - a * x[i-1] ** 2 + y[i-1]
        y[i] = b * x[i-1]
    return x


def lorenz_map(n=10000):
    with open("lorenz.txt", "r") as f:
        data = [float(x.rstrip("\n")) for x in f.readlines()]
    n = n if n < len(data) else len(data)
    return np.array(data)[:n]
