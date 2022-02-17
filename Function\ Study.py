# This Program will do a full analysis of a funcion, and print all results (graph excluded)
# to Terminal.

import matplotlib
import sympy


# Derivatives
from sympy import*
x = symbols('x')
f = input("f(x)=" )
y = f
f1 = diff(y)
print('Derivatives')
print(f1)
f2 = diff(f1)
print(f2)

# Zeros
print("")
print('Zeros')
x=float

