import math
import time
from abc import ABC, abstractmethod
from functions import Function
from utils import RECT_METHOD, TRAP_METHOD, SIMP_METHOD

class NumericIntegration(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def integrate() -> float:
        pass


class RectangleIntegration(NumericIntegration):

    def __init__(self) -> None:
        super().__init__(RECT_METHOD)

    def integrate(self, f: Function, a: float, b: float, n: int) -> float:
        delta_x = (b - a) / n
        sum = 0
        for i in range(1, n+1):
            y_k = f.function(a + i*delta_x)
            sum += y_k
        return delta_x * sum
    
    
class TrapezoidIntegration(NumericIntegration):

    def __init__(self) -> None:
        super().__init__(TRAP_METHOD)

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
         
class SimpsonIntegration(NumericIntegration):

    def __init__(self) -> None:
        super().__init__(SIMP_METHOD)

    def integrate(self, f: Function, a: float, b: float, n: int) -> float:
        delta_x = (b - a) / (n * 2)
        y_k = [f.function(a + i*delta_x) for i in range(0, 2*n+1)]
        sum_temp_0 = 0
        for i in range(1, n+1):
            sum_temp_0 += y_k[2*i-1]
        sum_temp_1 = 0
        for i in range(1, n):
            sum_temp_1 += y_k[2*i]
        tot_sum = y_k[0] + 4 * sum_temp_0 + 2 * sum_temp_1 + y_k[n*2]
        return tot_sum * delta_x / 3

        

    