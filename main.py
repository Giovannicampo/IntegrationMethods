from functions import *
from integration import *
from utils import newLine, separator, title
from chart import Chart, RectangleChart, TrapezoidChart

RECT_RESOLUTION = 100
TRAP_RESOLUTION = 10

def calculateIntegral(integration: NumericIntegration, chart: Chart, function: Function, a: float, b: float, resolution: int):
    result = integration.integrate(function, a, b, resolution)
    print(f'[{integration.name}] definite integral from {b} to {a} of {function.name}')
    print(f'results: {result}, calculated by cycling {resolution} times')
    print(f'while exact result is {function.integral(a,b)}')
    chart.render(function, a, b, resolution)


if __name__ == "__main__":
    title('main.py')
    newLine()

    rect = RectangleIntegration()
    trap = TrapezoidIntegration()
    simp = SimpsonIntegration()

    rectChart = RectangleChart()
    trapChart = TrapezoidChart()

    cubicFunc = CubicFunction()
    arctanDerivativeFunc = ArctanDerivativeFunction()
    logDerivativeFunc = LogDerivativeFunction()
    customFunc = CustomFunction()

    # title(cubicFunc.name)
    # calculateIntegral(rect, rectChart, cubicFunc, 1.0, 10.0, RECT_RESOLUTION)
    # separator()
    # calculateIntegral(trap, trapChart, cubicFunc, 1.0, 10.0, TRAP_RESOLUTION)
    # newLine()

    title(arctanDerivativeFunc.name)
    calculateIntegral(rect, rectChart, arctanDerivativeFunc, 1.0, 3.0, RECT_RESOLUTION)
    separator()
    calculateIntegral(trap, trapChart, arctanDerivativeFunc, 1.0, 3.0, TRAP_RESOLUTION)
    separator()
    calculateIntegral(simp, trapChart, arctanDerivativeFunc, 1.0, 3.0, 3)
    newLine()

    # title(logDerivativeFunc.name)
    # calculateIntegral(rect, rectChart, logDerivativeFunc, 1.0, 3.0, RECT_RESOLUTION)
    # separator()
    # calculateIntegral(trap, rectChart, logDerivativeFunc, 1.0, 3.0, TRAP_RESOLUTION)
    # newLine()

    # title(customFunc.name)
    # calculateIntegral(rect, rectChart, customFunc, 1.0, 3.0, RECT_RESOLUTION)
    # separator()
    # calculateIntegral(trap, rectChart, customFunc, 1.0, 3.0, TRAP_RESOLUTION)
    # newLine()