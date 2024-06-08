import fractional_integral as fi
import numpy as np
import math

def f(x):
    return x

def g(x):
    return math.cos( 2*math.pi*x )

def h(x):
    return np.exp(-x**2/2)*np.sqrt(2)/np.sqrt(math.pi)

def main():
    start = 0
    end = 2*math.pi
    by = 0.01
    grid = np.arange(start, end+by, by)

    functions = [f, g, h]
    for function in functions:
        fi.plot_primitives( function, grid=grid )

if __name__ == '__main__':
    main()