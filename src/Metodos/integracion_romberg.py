import numpy as np
class integracion_romberg:
    def integracion_romberg(self):
        I1 = np.array([0.1728,0.988,1.3648,1.4808,1.4956])
        I2 = np.array([])
        i ,k,fin= 0,2,len(I1)
        Flag = True

        while(Flag):
         print(I1)
         
         
         I2 = np.append(I2,((4**(k-1)*I1[i+1])-I1[i])/(4**(k-1)-1))
         print("{}*{} - {} / {}= {}".format(4**(k-1),I1[i+1],I1[i],(4**(k-1)-1) , ((4**(k-1)*I1[i+1])-I1[i])/(4**(k-1)-1)))
         i+=1
         if i == len(I1)-1:
          print("====================================")
          I1 = I2
          I2 = np.array([])
          
          k+=1
          i=0
          j=0
         if k >fin:
            Flag = False

        print(I1[len(I1)-1])
        
         
          
        
        
        return