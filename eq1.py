from sympy import *
import math
init_printing()
x = sympy.Symbol("x")
y= sympy.Function ("y")
ics = {y(math.pi/2):math.e}


ecuacion = Eq(sympy.sin(x)*y(x).diff(),y(x)*sympy.ln(y(x)))
print(dsolve(ecuacion,y(x),ics = ics))