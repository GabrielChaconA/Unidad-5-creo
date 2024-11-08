from Metodos.Integracion_Numerica import integracion_Numerica
from Metodos.Interpolacion_de_Newton import Interpolacion_de_Newton
from Metodos.regla_del_trapecio import regla_del_trapecio
from Metodos.extrapolacion_Richardson import extrapolacion_Richardson
from Metodos.simpson_1_3 import simpson_1_3
class Menu:
    def Menu(self):
        istance_integracion_Numerica = integracion_Numerica()
        instance_Interpolacion_de_Newton = Interpolacion_de_Newton()
        instance_trapecio = regla_del_trapecio()
        instance_extrapolacion_Richardson = extrapolacion_Richardson()
        instance_simpson1_3 = simpson_1_3()
        print("SELECCIONES OPCION")
        opcion = "5"
        if opcion == "1":
            istance_integracion_Numerica.integracion_Numerica()
        if opcion == "2":
            instance_Interpolacion_de_Newton.Interpolacion_de_Newton()
        if opcion == "3":
            instance_trapecio.regla_del_trapecio()
        if opcion == "4":
            instance_extrapolacion_Richardson.extrapolacion_Richardson()  
        if opcion == "5":
            instance_simpson1_3.simpson_1_3()
        



        return