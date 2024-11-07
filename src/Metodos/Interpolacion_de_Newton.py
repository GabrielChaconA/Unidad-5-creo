import numpy as np
class Interpolacion_de_Newton:
    def Interpolacion_de_Newton(self):
         x = np.array([3,5,8,10,12,20])
         y = np.array([1,10,25,55,105,240])
         print("DIME TU VALOR")
         valor = 11
         
         print("TU VALOR ES {}".format(valor))
         x,y,h = self.crear_n(x,y)
         k = self.k(valor,x)
         print(self.funcion(y,h,k))
         print(self.funcion_2(y,h))
         
        
        


         return
    
    def k(self,valor,x):
        K = (valor-x[0])/2

        return K
    def funcion(self,y,h,k):
       print(k)
       return 1/h*((y[1]-y[0]) + ((2*(k)-1)/2)*(y[2]-2*y[1]+y[0]))
    def funcion_2(self,y,h):
       
       return (1/h**2)*(y[2]-2*y[1]+y[0])
    
    def crear_n(self,x,y):
        n_tabla_x = np.array([])
        n_tabla_y = np.array([])
        i = 0 
        flag = True
        h = x[i+1]-x[i]
       
        contador = 1
        
        while(flag):
            
            if i > 0 and i < len(x)-1:
                if x[i+1]-x[i] == h:
              
                 #array = np.append(array, 4)
                 
                 contador = contador + 1  
               
                else:
             
                 contador = 1
                 n_tabla_x = np.array([])
                 h = x[i+1]-x[i]
                
                if contador == 2:
                   n_tabla_x = np.append(n_tabla_x,x[i-1])
                   n_tabla_x = np.append(n_tabla_x,x[i])
                   n_tabla_x = np.append(n_tabla_x,x[i+1])
                   n_tabla_y = np.append(n_tabla_y,y[i-1])
                   n_tabla_y = np.append(n_tabla_y,y[i])
                   n_tabla_y = np.append(n_tabla_y,y[i+1])
                  
                   
                   flag = False
                   break
            i +=1

        return n_tabla_x,n_tabla_y,h