from sympy import symbols, sympify, integrate
import numpy as np
class Regla_boole_4_5:
    def Regla_boole_4_5(self):
        x = np.array([-1,-0.75,-0.50,-0.25,0,0.25,0.50,0.75,1])
        a,b,m = -1,1,len(x)-1
        
        if m %4 == 0 :
            m = m/4
            
        print(self.proceso(x,m,b,a))

        return
    

    def proceso(self,x_array,m,b,a):
        
        I_final, funcion,i= 0, 0,0 
        for j in range(int(m)):
            h= (x_array[i+4]-x_array[i])
            print(h)
            x = symbols('x')
            funcion_str = "exp(x**4)"
          
            funcion_expr = sympify(funcion_str)
            
            funcion = (h/90) * ( 7 * funcion_expr.subs(x, x_array[i]) + 32 * funcion_expr.subs(x, x_array[i+1]) +12 * funcion_expr.subs(x, x_array[i+2]) + 32 * funcion_expr.subs(x, x_array[i+3]) +
    7 * funcion_expr.subs(x, x_array[i+4])
)

            
            i = i + 4
            
            I_final = I_final + funcion 
            print(I_final)
            
        return I_final
