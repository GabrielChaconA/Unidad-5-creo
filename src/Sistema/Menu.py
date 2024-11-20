from Metodos.Integracion_Numerica import integracion_Numerica
from Metodos.Interpolacion_de_Newton import Interpolacion_de_Newton
from Metodos.regla_del_trapecio import regla_del_trapecio
from Metodos.extrapolacion_Richardson import extrapolacion_Richardson
from Metodos.simpson_1_3 import simpson_1_3
from Metodos.simpson_3_8 import simpson_3_8
from Metodos.reglea_del_rectangulo import reglea_del_rectangulo
from Metodos.interpolacion_Lagrange import interpolacion_Lagrange
from Metodos.Regla_boole_4_5 import Regla_boole_4_5
from Metodos.Regla_boole_5 import Regla_boole_5
from Metodos.newton_cotes import newton_cotes
from Metodos.segmentos_desiguales import segmentos_desiguales
from Metodos.integracion_romberg import integracion_romberg
from Metodos.integracion_multiple import integracion_multiple
from Metodos.gauss_legendre import gauss_legendre
from Metodos.Integrales_Impropias import impropias


class Menu:
    def Menu(self):
        istance_integracion_Numerica = integracion_Numerica()
        instance_Interpolacion_de_Newton = Interpolacion_de_Newton()
        instance_trapecio = regla_del_trapecio()
        instance_extrapolacion_Richardson = extrapolacion_Richardson()
        instance_simpson1_3 = simpson_1_3()
        instance_simpson1_8 = simpson_3_8()
        instance_rectangulo = reglea_del_rectangulo()
        instance_interpolacion_Lagrange= interpolacion_Lagrange()
        instance_Regla_boole_4_5 = Regla_boole_4_5()
        instance_Regla_boole_5 = Regla_boole_5()
        instance_newton_cotes = newton_cotes()
        instance_segmentos_desiguales = segmentos_desiguales()
        instance_romberg = integracion_romberg()
        instance_multiple = integracion_multiple()
        instance_legendre = gauss_legendre()
        

        
        print("SELECCIONES OPCION")
        print("""
        SELECCIONE OPCIÓN:
        1. Integración Numérica
        2. Interpolación de Newton
        3. Regla del Trapecio
        4. Extrapolación de Richardson
        5. Simpson 1/3
        6. Simpson 3/8
        7. Regla del Rectángulo
        8. Interpolación de Lagrange    
        9. Regla de Boole 4/5
        10. Regla de Boole 5
        11. Newton-Cotes
        12. Segmentos desiguales 
        13.Inegracion Romberg
        14. Integracion multiple
        15.gauss_legendre
        16. impropias
        """)

        #opcion = input()
        opcion = "16"
        print("Selecciono: {} ".format(opcion))
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
        if opcion == "6":
            instance_simpson1_8.simpson_3_8()
        if opcion == "7":
            instance_rectangulo.reglea_del_rectangulo()
        if opcion == "8":
          instance_interpolacion_Lagrange.interpolacion_Lagrange()
        if opcion == "9":
            instance_Regla_boole_4_5.Regla_boole_4_5()
        if opcion == "10":
            instance_Regla_boole_5.Regla_boole_5()
        if opcion == "11":
            instance_newton_cotes.newton_cotes()
        if opcion == "12":
            instance_segmentos_desiguales.segmentos_desiguales() 
        if opcion == "13":
            instance_romberg.integracion_romberg()
        if opcion == "14":
            instance_multiple.integracion_multiple()
        if opcion == "15":
            instance_legendre.gauss_legendre()
        if opcion == "16":
            instance_integrales_impropias  = impropias()

            



        return