from sympy import diff, symbols, sympify, integrate
import numpy as np
class gauss_legendre:
    def gauss_legendre(self):
        #si se pone cualquier valor de c y x en los array queda 
        x = symbols('x')
        a,b = 1,1.5
        c = np.array([5/9,8/9,5/9])
        xn = np.array([-np.sqrt(3/5),0,np.sqrt(3/5)])
        f = np.array([])
        funcion_str = "exp(-x**2)"
        funcion_expr = sympify(funcion_str)
        if a != -1 and b!= 1:
            equi = ((b+a)/2)+((b-a)/2)
        for i in range(len(c)):
             f= np.append(f, round(funcion_expr.subs(x,((b+a)/2)+(((b-a)/2)* xn[i])),4))
             f[i] = f[i]*c[i]
             
        print(np.sum(f)*((b-a)/2))

        return