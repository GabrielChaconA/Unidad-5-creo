
from sympy import diff, symbols, sympify, integrate
import numpy as np
class Regla_boole_5:
    def Regla_boole_5(self):
        x = np.array([-1,-0.6,-0.2,0.2,0.6,1])
        a,b,m = -1,1,len(x)-1
        
        if m %5 == 0 :
            m = m/5
            
        print(self.proceso(x,m,b,a))

        return
    

    def proceso(self,x_array,m,b,a):
        
        I_final, funcion,i= 0, 0,0 
        for j in range(int(m)):
            h= (x_array[i+5]-x_array[i])
            print(h)
            x = symbols('x')
            funcion_str = "exp(x**4)"
          
            funcion_expr = sympify(funcion_str)
            
            funcion = (h/288) * ( 19 * funcion_expr.subs(x, x_array[i]) + 75 * funcion_expr.subs(x, x_array[i+1]) +50 * funcion_expr.subs(x, x_array[i+2]) + 50 * funcion_expr.subs(x, x_array[i+3]) +
    75 * funcion_expr.subs(x, x_array[i+4]) + 19 * funcion_expr.subs(x, x_array[i+5])
)

            
            i = i + 5
            
            I_final = I_final + funcion 
            sp_expr = sympify(funcion_expr)    
            segunda_derivada = diff(sp_expr, x, 4)
            print( "E = {}".format(((-3/8)*h**5) * segunda_derivada) )  
            print(I_final)
            
        return I_final