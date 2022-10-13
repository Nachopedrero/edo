import imp
from sympy import *
import math

init_printing()
x = sympy.Symbol("x")
y= sympy.Function ("y")



ecuacion = Eq(2*x*y(x).diff(),y(x)+3*(x**2))
print(dsolve(ecuacion,y(x)))