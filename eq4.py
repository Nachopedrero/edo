from sympy import *
import math
init_printing()
x = sympy.Symbol("x")
y= sympy.Function ("y")
ics = {y(3):-1}


ecuacion = Eq(y(x).diff(),(y(x)*x**2-y(x))/(y(x-1)))
print(sympy.dsolve(ecuacion,y(x),ics= ics))