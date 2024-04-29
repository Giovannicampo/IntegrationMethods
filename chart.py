import matplotlib.pyplot as plt
import numpy as np
from functions import Function

DOMAIN_OFFSET = 5

class Chart:

    def _renderLine(self, f: Function, x):
        plt.title(f'Definite integral of {f.name}')
        plt.plot(x, f.function(x))
        plt.legend('f(x)')

    def _exactIntegral(self, f: Function, x, a, b, color):
        plt.axhline(color = 'black')
        plt.fill_between(x, f.function(x), where = [(x > a) and (x < b) for x in x], color = color)

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a-2, b+2, 1000)
        self._renderLine(f,x)
        self._exactIntegral(f, x, a, b, '#00ff0020')
        plt.show()

class RectangleChart(Chart):

    def __rectangleMethod(self, f: Function, a, b, resolution):
        delta_x = (b - a) / resolution
        x_left = np.linspace(a, b - delta_x, resolution)
        y_left = [f.function(x_temp) for x_temp in x_left]
        plt.bar(x_left, y_left, width = delta_x, alpha = 0.75, align='edge', edgecolor='g', color='green')

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a - DOMAIN_OFFSET, b + DOMAIN_OFFSET, 1000)
        super()._renderLine(f,x)
        super()._exactIntegral(f, x, a, b, '#00ff0020')
        self.__rectangleMethod(f, a, b, resolution)
        plt.show()

class TrapezoidChart(Chart):

    def __trapezoidMethod(self, f: Function, a, b, resolution):
        delta_x = (b - a) / resolution
        x = np.linspace(a, b, resolution + 1)
        y = [f.function(x_temp) for x_temp in x]
        for i in range(resolution):
            xs = [x[i],x[i],x[i+1],x[i+1]]
            ys = [0,y[i],y[i+1],0]
            plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a - DOMAIN_OFFSET, b + DOMAIN_OFFSET, 1000)
        super()._renderLine(f,x)
        super()._exactIntegral(f, x, a, b, '#00ff0020')
        self.__trapezoidMethod(f, a, b, resolution)
        plt.show()

