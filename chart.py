import matplotlib.pyplot as plt
import numpy as np
from functions import Function
from utils import EXACT_INT, RECT_METHOD, TRAP_METHOD

DOMAIN_OFFSET = 5

class Chart:

    def _renderLine(self, f: Function, x, methodName: str):
        plt.title(f'Definite integral of {f.name} - {methodName}')
        plt.plot(x, f.function(x))
        plt.legend('f(x)')

    def _exactIntegral(self, f: Function, x, a, b, color):
        plt.axhline(color = 'black')
        plt.fill_between(x, f.function(x), where = [(x > a) and (x < b) for x in x], color = color)

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a-2, b+2, 1000)
        self._renderLine(f,x, EXACT_INT)
        self._exactIntegral(f, x, a, b, '#00ff0020')
        plt.show()

class RectangleChart(Chart):

    def __rectangleMethod(self, f: Function, a, b, resolution):
        delta_x = (b - a) / resolution
        x_left = np.linspace(a, b - delta_x, resolution)
        y_left = [f.function(x_temp + delta_x) for x_temp in x_left]
        plt.bar(x_left, y_left, width = delta_x, alpha = 0.75, align='edge', edgecolor='g', color='green')

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a - DOMAIN_OFFSET, b + DOMAIN_OFFSET, 1000)
        super()._renderLine(f,x, RECT_METHOD)
        super()._exactIntegral(f, x, a, b, '#00ff0020')
        self.__rectangleMethod(f, a, b, resolution)
        plt.show()

class TrapezoidChart(Chart):

    def __trapezoidMethod(self, f: Function, a, b, resolution):
        x = np.linspace(a, b, resolution + 1)
        y = [f.function(x_temp) for x_temp in x]
        for i in range(resolution):
            xs = [x[i],x[i],x[i+1],x[i+1]]
            ys = [0,y[i],y[i+1],0]
            plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a - DOMAIN_OFFSET, b + DOMAIN_OFFSET, 1000)
        super()._renderLine(f,x, TRAP_METHOD)
        super()._exactIntegral(f, x, a, b, '#00ff0020')
        self.__trapezoidMethod(f, a, b, resolution)
        plt.show()

class SimpsonChart(Chart):

    def __calc_parabola_vertex(self, x1, y1, x2, y2, x3, y3):
        denom = (x1-x2) * (x1-x3) * (x2-x3)
        A = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
        B = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
        C = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom
        return A,B,C

    def __simpsonMethod(self, f: Function, a, b, resolution):
        # if resolution is not divisible for 3, then make it so
        resolution -= resolution % 3
        delta_x = (b - a) / resolution
        x = np.linspace(a, b, resolution)
        y = [f.function(x_temp) for x_temp in x]
        dim = len(x)
        # offset prevents from out of bound indexing
        offset = 1 if dim % 6 != 0 else 2
        for i in range(0, dim - offset, 2):
            A,B,C = self.__calc_parabola_vertex(x[i], y[i], x[i+1], y[i+1], x[i+2], y[i+2])
            x_pos = np.arange(x[i], x[i+2], delta_x/10)
            y_pos = []
            for j in range(len(x_pos)):
                x_val = x_pos[j]
                y_temp=(A*(x_val**2)) + (B*x_val) + C
                y_pos.append(y_temp)
            plt.plot(x_pos, y_pos, linestyle='-.', color='red')
            plt.fill_between(x_pos, y_pos, color = 'orange', alpha = 0.7)
            # plt.fill(x_pos, y_pos, 'orange', edgecolor='orange',alpha=0.2)
        

    def render(self, f: Function, a, b, resolution):
        x = np.linspace(a-2, b+2, 1000)
        self._renderLine(f,x, EXACT_INT)
        self.__simpsonMethod(f, a, b, resolution)
        # self._exactIntegral(f, x, a, b, '#00ff0020')
        plt.show()

