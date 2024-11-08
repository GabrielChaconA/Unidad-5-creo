from sympy import symbols, sympify, integrate
import numpy as np
class simpson_1_3:
    def simpson_1_3(self):
     x = symbols('x')
     funcion_str = "exp(x**4)"
     funcion_expr = sympify(funcion_str)
     limite_a, limite_b , n= -1,1,6
     print(funcion_expr.subs(x, -0.6))

      # Integra la expresión
     ##integral = integrate(funcion_expr, x)
     print("Función:", funcion_expr)
     print(self.crear_funcion(limite_a,limite_b,funcion_expr,n))
     

     return
    def crear_funcion(self,a,b,funcion_expr,n):
     x = symbols('x')
     valor_a_evaluar,h = 0.5, (b-a)/n
     x_,suma,i,pares, impares= a,0,0,0,0
     print("H:", h)
     
     y = np.array([])
     while(True):
       print(i)
       print(x_)
       y= np.append(y, round(funcion_expr.subs(x, x_),4))
       if( i%2 == 0 and i >0 ):
         print("par",i)
         print("{} + {}".format(pares,round(y[i],1) ))
         if x_< b-(1/3):
          pares = round(y[i]+ pares,4)
       if (i%2 != 0 and i >0   or i == 1) :
         print("impar",i)
         print("{} + {}".format(impares,y[i] ))
         if x_ < b-(1/3):
          impares = round(y[i]+ impares,4)
       x_= round(x_+h,4)
      
       i+=1
      
       if x_ > b:
     
        break
     print(y)
     print("{}/{} 4({}) +2({}) + {} + {}".format(h,3,impares,pares,y[0],y[len(y)-1]))
     return y, (h/3)*((4*impares)+(2*pares)+y[0]+y[len(y)-1])