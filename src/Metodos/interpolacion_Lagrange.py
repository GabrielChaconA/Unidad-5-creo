import numpy as np
class interpolacion_Lagrange:
    def interpolacion_Lagrange(self):
     x_Tabla = np.array([0,1.25,3.75])
     y_Tabla = np.array([13.5,12,10])
     i,x = 1,0

     #self.ubicacion(i) # aqui pondre en que rango de vlores voy a usar 
     operacion = (y_Tabla[i-1] * (((2 * x) - x_Tabla[i] - x_Tabla[i+1]) / ((x_Tabla[i-1] - x_Tabla[i]) * (x_Tabla[i-1] - x_Tabla[i+1]))) )+ (y_Tabla[i] * ((2 * x - x_Tabla[i-1] - x_Tabla[i+1]) / ((x_Tabla[i] - x_Tabla[i-1]) * (x_Tabla[i] - x_Tabla[i+1])))) + (y_Tabla[i+1] * ((2 * x - x_Tabla[i-1] - x_Tabla[i]) / ((x_Tabla[i+1] - x_Tabla[i]) * (x_Tabla[i+1] - x_Tabla[i-1]))) )



     print(operacion)
     return