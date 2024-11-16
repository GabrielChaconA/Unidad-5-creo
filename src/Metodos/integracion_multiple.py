import numpy as np
class integracion_multiple:
    def integracion_multiple(self):
        x = np.array([0,4,8,0,4,8,0,4,8])
        y_ = np.array([0,0,0,3,3,3,6,6,6])
        y = np.array([])
        T = np.array([72,64,24,54,70,54,0,40,48])
        I =np.array([])
        m , i= (len(T))/3, 0
        
        for j in range(int(m)):
           y = np.append(y,y_[i])
           i+=3
        
        a,b,c,d = 0,8,0,6
        Final= 0
        I = self.trapecio(x,T)
        
        Final = self.trapecio(y,I)
        Final = (np.sum(Final))/((d-c)*(b-a) )
        print(Final)

        return
    def trapecio(self,x,T):
        print(x,T)
        I =np.array([])
        i ,h= 0,0
        m = (len(x))/3
        print(m)
        for j in range(int(m)):
          subarray = x[[i,i+1,i+2]]
          diferencias = np.diff(subarray)
          son_iguales = np.all(diferencias == diferencias[0])
          if son_iguales:
             h = diferencias[0]
           
          I = np.append(I, (h/2)*(T[i]+2*T[i+1]+T[i+2]))
          print(I)

          
          i +=3
        return I