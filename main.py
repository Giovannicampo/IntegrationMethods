from functions import *
from integration import *
from utils import newLine, separator, title
from chart import Chart, RectangleChart, TrapezoidChart, SimpsonChart
from integrator import IntCreator

RESOLUTION = 10


if __name__ == "__main__":
    title('main.py')
    newLine()

    # integrators
    rectInt = IntCreator.getRect()
    trapInt = IntCreator.getTrap()
    simpInt = IntCreator.getSimp()

    #functions
    cubicFunc = CubicFunction()

    rectInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)
    trapInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)
    simpInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)