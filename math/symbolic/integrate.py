# sympy integral demonstration
from sympy import *
x, y, z = symbols('x y z')

# Use unicode in printing of the result
init_printing(use_unicode=True)

# Integrate sqrt(x)
integrate(sqrt(x),x)

# Integrate ln(1/x)
integrate(ln(1/x),x)