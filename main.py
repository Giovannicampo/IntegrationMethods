from functions import *
from utils import newLine, title
from integrator import IntCreator

RESOLUTION = 10


if __name__ == "__main__":
    title('main.py')
    newLine()

    # integrators
    rectInt = IntCreator.getRect()
    trapInt = IntCreator.getTrap()
    simpInt = IntCreator.getSimp()

    #cubic function
    cubicFunc = CubicFunction()

    rectInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)
    trapInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)
    simpInt.printAll(cubicFunc, 1.0, 10.0, RESOLUTION)

    #arctan der function
    arctanDerFunc = ArctanDerivativeFunction()

    rectInt.printAll(arctanDerFunc, 1.0, 10.0, RESOLUTION)
    trapInt.printAll(arctanDerFunc, 1.0, 10.0, RESOLUTION)
    simpInt.printAll(arctanDerFunc, 1.0, 10.0, RESOLUTION)