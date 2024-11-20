from sympy import symbols, sympify, integrate
import numpy as np
class reglea_del_rectangulo:
## No no entiendo este metodo
    def reglea_del_rectangulo(self):
      x_tabla = np.array([])
      x = symbols('x')
      funcion_str = "x**2-3*x-9"
      funcion_expr = sympify(funcion_str)
      limite_a, limite_b , n= 0,4,120


      # Integra la expresión
     ##integral = integrate(funcion_expr, x)
      self.evaluar(funcion_expr,self.rectangulo(self.crear_x(self.h(limite_a,limite_b,n),limite_a,limite_b)))
      return
    
    

    def crear_x(self, h, limite_a,limite_b):
     print(h)
     x_tabla = np.array([])
     aumento = limite_a
     
     while(True):
        x_tabla =  np.append(x_tabla, round(aumento,4))
        aumento+=h
        if aumento > limite_b:
           break
     return x_tabla
    
    def  rectangulo(self,x_tabla):
       print(x_tabla)
       x_= np.array([])
       i = 0

       while(True):
          if i >0:
           x_ = np.append(x_,((x_tabla[i-1]+x_tabla[i])/2))
          i+=1
          if i > len(x_tabla)-1:
             break
          
       print(x_)
       return x_
    def evaluar(self,funcion_expr,x_array):
       x = symbols('x')
       y = np.array([])
       i = 0
       while(True):
          
        y = np.append(y, round(funcion_expr.subs(x, x_array[i]),4))
        i+= 1
        if i > len(x_array)-1:
             break 
       
       print(y)
       return y
    

    def h(self, a,b,n):
       return (b-a)/n