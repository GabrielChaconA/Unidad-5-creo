from sympy import symbols, sympify, integrate
import numpy as np
class integrales_impropias():

    def integrales_impropias(self):
      x_tabla = np.array([])
      x = symbols('x')
      funcion_str = "exp(x**2)"
      funcion_expr = sympify(funcion_str)
      limite_a, limite_b , n= 0,1,5
        


      return