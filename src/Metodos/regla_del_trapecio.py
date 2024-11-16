from sympy import symbols, sympify, integrate
import numpy as np
class regla_del_trapecio:
    def regla_del_trapecio(self):
        
     x = symbols('x')
     funcion_str = "exp(x**4)"
     funcion_expr = sympify(funcion_str)
     limite_a, limite_b , n= -1,1,5

      # Integra la expresión
     ##integral = integrate(funcion_expr, x)
     print("Función:", funcion_expr)
     print(self.crear_funcion(limite_a,limite_b,funcion_expr,n))
     

     return
    
    def crear_funcion(self,a,b,funcion_expr,h):
     x = symbols('x')
     valor_a_evaluar,h = 0.5, (b-a)/h
     x_,suma,i= a,0,0
     y = np.array([])
     while(True):
      y= np.append(y, round(funcion_expr.subs(x, x_),4))
      if x_ > a and x_<b:
        suma = y[i] + suma

      x_=x_+h
      i+=1
      if x_ > b:
        break
     
      

     return ((h)/2)*(y[0]+(2*suma)+y[len(y)-1])