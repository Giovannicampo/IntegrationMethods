import math
import time
from abc import ABC, abstractmethod
from functions import Function

class NumericIntegration(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def integrate():
        pass


class RectangleIntegration(NumericIntegration):

    def __init__(self) -> None:
        super().__init__("Rectangle Method")

    def integrate(self, f: Function, a: float, b: float, n: int) -> float:
        delta_x = (b - a) / n
        sum = 0
        for i in range(1, n+1):
            y_k = f.function(a + i*delta_x)
            sum += y_k
        return delta_x * sum
    
    
class TrapezoidIntegration(NumericIntegration):

    def __init__(self) -> None:
        super().__init__("Trapezoid Method")

    def integrate(self, f: Function, a: float, b: float, n: int) -> float:
        delta_x = (b - a) / n
        sum = 0
        for i in range(1, n):
            y_k = f.function(a + i*delta_x)
            sum += y_k
        y_0 = f.function(a)
        y_n = f.function(a + n*delta_x)
        sum = y_0 + 2*sum + y_n
        return sum*delta_x/2
         
    