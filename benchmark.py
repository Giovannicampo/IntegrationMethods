from integrator import IntCreator, Integrator
from functions import *
import matplotlib.pyplot as plt
import numpy as np


class Benchmark:

    def __init__(self) -> None:
        self.rectInt = IntCreator.getRect()
        self.trapInt = IntCreator.getTrap()
        self.simpInt = IntCreator.getSimp()

    def __measureError(self, int: Integrator, f: Function, a, b, res) -> float:
        return abs( int.integrate(f, a, b, res) - f.integral(a, b) )


    def __calculateError(self, f: Function, a, b) -> tuple:
        xAxis = np.arange(10, 100, 1)
        rectError = [self.__measureError(self.rectInt, f, a, b, r) for r in xAxis]
        trapError = [self.__measureError(self.trapInt, f, a, b, r) for r in xAxis]
        simpError = [self.__measureError(self.simpInt, f, a, b, r) for r in xAxis]
        return [xAxis, rectError, trapError, simpError]
    
    def showAccuracy(self, f: Function, a, b):
        xAxis, rectError, trapError, simpError = self.__calculateError(f, a, b)
        print(rectError[0], trapError[0], simpError[0])
        plt.plot(xAxis, rectError, label='Rect Err')
        plt.plot(xAxis, trapError, label='Trap Err')
        plt.plot(xAxis, simpError, label='Simp Err')
        plt.title(f'Accuracy benchmarking - {f.name}')
        plt.xlabel('Resolution')
        plt.ylabel('Error')
        plt.legend(loc="upper right")

        plt.show()


ben = Benchmark()

ben.showAccuracy(ArctanDerivativeFunction(), 1.0, 10.0)
ben.showAccuracy(CubicFunction(), 1.0, 10.0)