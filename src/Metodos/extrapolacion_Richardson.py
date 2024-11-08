import numpy as np
class extrapolacion_Richardson:
    def extrapolacion_Richardson(self):
     x = np.array([0,0.25,0.5,0.75,1])
     y = np.array([1.2,1.1035,0.925,0.6363,0.2])
     val = (len(x)/2)+0.5
     h1 = x[len(x)-1]-x[0]
     h2 = x[len(x)-2]-x[1]
     D1 = (y[len(x)-1]-y[0])/x[len(x)-1]-x[0]
     D2 = (y[len(x)-2]-y[1])/(x[len(x)-2]-x[1])
     print(D1,D2)
     if h2 == h1/2:
        Vv = ((4*D2)-D1)/3
        print ("RESULTADO :{}".format(Vv))
     else:
        Vv = D2+ ((D2-D1)/((h1/h2)**2-1))
        print ("RESULTADO :{}".format(Vv))

     
       
    
     





     return 