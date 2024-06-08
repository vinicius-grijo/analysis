import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
import matplotlib.pyplot as plt
import scienceplots
plt.style.use([ 'notebook', 'grid','bright'])



from abc import ABC, abstractmethod
import numpy as np

class Integral(ABC):
    @abstractmethod
    def calculate_integral(self, func, a, x, alpha):
        pass

    @abstractmethod
    def calculate_primitive(self, func, grid, alpha):
        pass

class FractionalIntegral(Integral):
    def calculate_integral(self, func, alpha, a, x):
        def integrand(s):
            return (x - s)**(alpha - 1) * func(s) / gamma(alpha)
        
        integral, _ = quad(integrand, a, x)
        return integral
    
    def calculate_primitive(self, func, alpha, grid, a):
        primitive = [ self.calculate_integral(func, alpha, a, xi) for xi in grid ]
        return np.array(primitive)


def plot_primitives(func, grid=None, alphas=None, a=None):
    if grid is None:
        start = 0
        end = 1
        by = 0.01
        grid = np.arange( start, end + by, by)
    if alphas is None:
        alphas = [1, 1.5, 2]
    if a is None:
        a = 0
    plt.figure( figsize=(10,5) )
    for alpha in alphas:
        fractional_integral = FractionalIntegral()
        primitive = fractional_integral.calculate_primitive(func, alpha, grid, a)
        plt.plot(grid, primitive, label=f'alpha={alpha}')
        print(f'{alpha}')
    
    plt.xlabel('x')
    plt.ylabel('Fractional Primitive')
    plt.title('Fractional Primitives')
    plt.legend()
    plt.show()