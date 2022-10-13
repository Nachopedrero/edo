from sympy import *
import math
init_printing()
x = sympy.Symbol("x")
y= sympy.Function ("y")


ecuacion = Eq(y(x).diff(),2*(x-2)**2+(y(x)/x-2))
print(dsolve(ecuacion,y(x)))