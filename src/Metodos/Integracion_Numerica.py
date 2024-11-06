
import numpy as np
class integracion_Numerica:
    def integracion_Numerica(self):
       x = np.array([0,2,4,6,8,10,12])
       y = np.array([4,5.5,8,13.5,22,31.5,38])
       print("INGRESE VALOR")
       valor = 7
       i =  0
       print("Valor ingresado {}".format(valor))
    
       for J in range(len(x)-1):
          print(i)
          if valor == x[i]:
             print("progresion")
             print(self.pro(x,y,i))
             break
          if i > 0 and  valor > x[i-1] and valor < x[i+1] and i < len(x)-1:
             print("central")
             print(self.central(x,y,i))
             break
          if valor == x[len(x)-1]:
             print("regresion")
             print(self.regre(x,y,len(x)-1) )
             break 
          i+=1
      
       return
    def pro(self, x,y,i):
        
        valor = (y[i+1]-y[i])/ (x[i+1]-x[i])
        print(" {} - {} / {} - {}  ".format(y[i+1],y[i], x[i+1],x[i]))
        return valor
    def regre(self, x,y,i):
      print(i)
      valor = (y[i]-y[i-1])/ (x[i]-x[i-1])
      print(" {} - {} / {} - {}  ".format(y[i],y[i-1], x[i],x[i-1]))

      return valor
    def central(self, x,y,i):
        valor = (y[i+1]-y[i-1])/ (x[i+1]-x[i-1])
        print(" {} - {} / {} - {}  ".format(y[i+1],y[i-1], x[i+1],x[i-1]))

        return valor