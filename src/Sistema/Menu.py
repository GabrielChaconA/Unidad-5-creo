from Metodos.Integracion_Numerica import integracion_Numerica
from Metodos.Interpolacion_de_Newton import Interpolacion_de_Newton
class Menu:
    def Menu(self):
        istance_integracion_Numerica = integracion_Numerica()
        instance_Interpolacion_de_Newton = Interpolacion_de_Newton()
        print("SELECCIONES OPCION")
        opcion = "2"
        if opcion == "1":
            istance_integracion_Numerica.integracion_Numerica()
        if opcion == "2":
            instance_Interpolacion_de_Newton.Interpolacion_de_Newton()



        return