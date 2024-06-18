from abc import ABC, abstractmethod
from functions import Function
from integration import *
from chart import *
from utils import newLine, separator

class Integrator(ABC):

    def __init__(self, numInt: NumericIntegration, chart: Chart) -> None:
        self.numericIntegrator = numInt
        self.chart = chart

    @abstractmethod
    def integrate(self, f: Function, a: float, b: float, resolution: int) -> float:
        self.numericIntegrator.integrate(f, a, b, resolution)

    @abstractmethod
    def showChart(self, f: Function, a: float, b: float, resolution: int) -> None:
        self.chart.render(f, a, b, resolution)

    @abstractmethod
    def printAll(self, f: Function, a: float, b: float, resolution: int) -> None:
        result = self.numericIntegrator.integrate(f, a, b, resolution)
        print(f'[{self.numericIntegrator.name}] definite integral from {b} to {a} of {f.name}')
        print(f'results: {result}, calculated by cycling {resolution} times')
        print(f'while exact result is {f.integral(a,b)}')
        separator()
        newLine()
        self.showChart(f, a, b, resolution)


class RectIntegrator(Integrator):

    def __init__(self) -> None:
        super().__init__(RectangleIntegration(), RectangleChart())

    def integrate(self, f: Function, a: float, b: float, resolution: int) -> float:
        return super().integrate(f, a, b, resolution)
    
    def showChart(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().showChart(f, a, b, resolution)
    
    def printAll(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().printAll(f, a, b, resolution)
    
class TrapIntegrator(Integrator):

    def __init__(self) -> None:
        super().__init__(TrapezoidIntegration(), TrapezoidChart())

    def integrate(self, f: Function, a: float, b: float, resolution: int) -> float:
        return super().integrate(f, a, b, resolution)
    
    def showChart(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().showChart(f, a, b, resolution)
    
    def printAll(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().printAll(f, a, b, resolution)
    
class SimpIntegrator(Integrator):

    def __init__(self) -> None:
        super().__init__(SimpsonIntegration(), SimpsonChart())

    def integrate(self, f: Function, a: float, b: float, resolution: int) -> float:
        return super().integrate(f, a, b, resolution)
    
    def showChart(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().showChart(f, a, b, resolution)
    
    def printAll(self, f: Function, a: float, b: float, resolution: int) -> None:
        return super().printAll(f, a, b, resolution)
    

class IntCreator:

    def getRect() -> Integrator:
        return RectIntegrator()
    
    def getTrap() -> Integrator:
        return TrapIntegrator()
    
    def getSimp() -> Integrator:
        return SimpIntegrator()
    