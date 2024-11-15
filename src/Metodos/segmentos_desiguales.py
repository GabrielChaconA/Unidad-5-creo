from sympy import symbols, sympify, integrate
import numpy as np

class segmentos_desiguales:
    def segmentos_desiguales(self):
        x_lista = np.array([-1,-0.9,-0.7,-0.3,0,0.4,1])
        i ,F = 0,0
        x = symbols('x')
        funcion_str = "exp(x**4)"
        funcion_expr = sympify(funcion_str)



        while(True):
         h = x_lista[i]- x_lista[i+1]
         R = (abs(h/2) )* (funcion_expr.subs(x, x_lista[i]) + funcion_expr.subs(x, x_lista[i+1]))
         print(funcion_expr.subs(x, x_lista[i]) + funcion_expr.subs(x, x_lista[i+1]),i,abs(h/2))
         F = R + F 
         i+=1
         
         if i == len(x_lista)-1:
            break
         
         


        print(x_lista,F)
        return