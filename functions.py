import math
from abc import ABC, abstractmethod
from utils import *

class Function (ABC):

    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def function(self, x: float) -> float:
        pass

    @abstractmethod
    def integral(self, a: float, b: float) -> float:
        pass

class CubicFunction (Function):

    def __init__(self) -> None:
        super().__init__(CUBIC_FUNCTION)
    
    # override
    def function(self, x: float) -> float:
        return x**3
    
    # override
    def integral(self, a: float, b: float) -> float:
        primitive = lambda x: x**4/4
        return primitive(b) - primitive(a)
    
class ArctanDerivativeFunction (Function):

    def __init__(self) -> None:
        super().__init__(ARCTAN_DER_FUNCTION)

    # override
    def function(self, x: float) -> float:
        return 1/(x**2 + 1)
    
    # override
    def integral(self, a: float, b: float) -> float:
        primitive = lambda x: math.atan(x)
        return primitive(b) - primitive(a)
    
class LogDerivativeFunction (Function):

    def __init__(self) -> None:
        super().__init__(LOG_DER_FUNCTION)
    
    # override
    def function(self, x: float) -> float:
        return 1/x
    
    # override
    def integral(self, a: float, b: float) -> float:
        primitive = lambda x: math.log(x)
        return primitive(b) - primitive(a)
    
class CustomFunction (Function): 

    def __init__(self) -> None:
        super().__init__(CUSTOM_FUNCTION_1)
    
    # override
    def function(self, x: float) -> float:
        return abs(x)*pow(x,2)*pow(math.e,3*pow(x,2))

    # override
    def integral(self, a: float, b: float) -> float:
        primitive = lambda x : (math.pow(x,2) * math.pow(math.e, 3 * math.pow(x, 2)) - math.pow(math.e, 3 * math.pow(x,2)) / 3) / 6
        if (a < 0.0) & (b < 0.0):
            return primitive (a) - primitive(b)
        elif a < 0.0:
            return (primitive(0) - primitive(a)) + (primitive(b) - primitive(0))
        return primitive(b) - primitive(a)