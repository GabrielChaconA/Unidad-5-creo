from sympy import diff, symbols, sympify, integrate
import numpy as np
class simpson_3_8:
    def simpson_3_8(self):
        x = np.array([-1,-2/3,-1/3,0,1/3,2/3,1])
        a,b,m = -1,1,len(x)-1
        if m %3 == 0 :
            m = m/3
            print(m)
        print(self.proceso(x,self.h(b,a,m),m))

        return
    def h(self,b,a,m) : return((b-a)/(3*m))

    def proceso(self,x_array,h,m):
        
        I_final, funcion,i= 0, 0,0 
        for j in range(int(m)):
            print(h)
            x = symbols('x')
            funcion_str = "exp(x**4)"
            print()
            funcion_expr = sympify(funcion_str)
            funcion = (3/8)*(h)*(funcion_expr.subs(x, x_array[i])+ 3*(funcion_expr.subs(x, x_array[i+1]))+ 3*(funcion_expr.subs(x, x_array[i+2]))+ funcion_expr.subs(x, x_array[i+3]))
            
            i = i + 3
            
            I_final = I_final + funcion 
        sp_expr = sympify(funcion_expr)    
        segunda_derivada = diff(sp_expr, x, 4)
        print( "E = {}".format(((-3/8)*h**5) * segunda_derivada) )   
        return I_final
