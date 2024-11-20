import pandas as pd
import numpy as np
import sympy as sp
import math
def impropias():
    function_str = "((1/sqrt(2*pi))*exp(-(x**2)/2))"
    while True:
        print("Ingrese los límites de integración")
        print(" Si quiere ingresar infinito o menos infinito , +inf o -inf")
        a , b = input("Limite a:  "),input("Limite b:  ")
        vandera  = True
        if is_number(a) and is_number(b):
            print()
        else:
            if is_number(a) == False:
                if comprobar_infinito(a) == False:
                    print("NO VALIDO")
                    vandera = False
            if is_number(b) == False:
                if comprobar_infinito(b) == False:
                    print("NO VALIDO")
        if vandera == True:
            ejecutar(function_str, a, b)
            break
        else:
            print("Continuar?")

#Metodos para preguntar y evitar errores 
def ask_for_double(nombre_valor):
    while True:
        try:
            return float(input(f"Ingrese {nombre_valor}: "))
        except Exception as e:
            print("Se ingresó un valor inválido, intente de nuevo")

def ask_for_int(nombre_valor):
    while True:
        try:
            return int(input(f"Ingrese {nombre_valor}: "))
        except Exception as e:
            print("Se ingresó un valor inválido, intente de nuevo")


def cifras(numero, n):
    if numero == 0:
        return 0
    else:
        numero_float = float(numero) 
        factor = n - (int(f"{numero_float:e}".split('e')[1]) + 1)
        return round(numero_float, factor)
    

def verificar_equidistancia(valores_x):
    h = valores_x[1] - valores_x[0]
    error_tolerable = 1/(math.pow(10, 4))
    for i in range(1, len(valores_x) - 1):
        new_h = valores_x[i + 1] - valores_x[i]
        if abs(new_h - h) > error_tolerable: 
            return False
    return True

def is_number(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def comprobar_infinito(cad):
    if cad == '+inf' or cad == '-inf':
        return True
    return False

def calcular_valores_xy_tabla(function_str, h, a, b):
    x = sp.symbols('x')
    function = sp.sympify(function_str)
    valores_x = []
    i = a
    while i <= b:
        valores_x.append(i)
        i += h
    valores_y = []
    for value in valores_x:
        valores_y.append(cifras(function.subs(x, value), 6))
        print(f"{cifras(value, 6)}, {cifras(function.subs(x, value), 6)}") #Para obtener como un csv en la consola
    return [valores_x, valores_y]



#METODO DEL TRAPECIO
def calcular_valores_y_Trapecio(function_str, n, a, b):
    x = sp.symbols('x')
    function = sp.sympify(function_str)
    h = (b - a)/n
    valores_x = []
    i = a
    while i <= b:
        valores_x.append(i)
        i += h

    valores_y = []
    for value in valores_x:
        valores_y.append(cifras(function.subs(x, value), 6))
        
    return valores_y

def suma_trapecio(valores_y):
    suma_valores_y = valores_y[0] + valores_y[-1]
    suma_parcial = 0
    for i in range(1, len(valores_y) - 1):
        suma_parcial += valores_y[i]
    suma_valores_y += 2*suma_parcial
    return suma_valores_y

def ejecutar_metodo_Trapecio(function_str, n, a, b):
    valores_y = calcular_valores_y_Trapecio(function_str, n, a, b)
    suma_valores_y = suma_trapecio(valores_y)
    h = (b - a)/n
    return (h/2)*(suma_valores_y)

#METODO DEL RECTANGULO
def integral_rectangulo(function_str, n, a, b):
    t = sp.symbols('t')
    function = sp.sympify(function_str)
    h = (b - a)/n
    valores_x = []
    i = a
    while i <= b:
        valores_x.append(i)
        i += h
    
    medias_x = []
    for i in range(len(valores_x) - 1):
        medias_x.append((valores_x[i] + valores_x[i + 1]) / 2)
    
    suma = 0
    for value in medias_x:
        suma += cifras(function.subs(t, value), 6)
    
    return h*suma

def Rectangulo(function_str, n, a, b):
    return integral_rectangulo(function_str, n, a, b)

#con tabla de valores
def ejecutar(function_str, a, b):
    valor_integral = 0
    x, t = sp.symbols('x t')
    function_original = function_str
    if 'exp' in function_str:
        function_str = function_str.replace('exp', 'key_word')
        function_str = function_str = function_str.replace('x', '(1/t)')
        function_str = function_str.replace('key_word', 'exp')
    else:
        function_str = function_str.replace('x', '(1/t)')
    function_str += '*(-1/t**2)'

    t_values = []
    if comprobar_infinito(a) == True and comprobar_infinito(b) == True:
        t_values = [0, -1, 1, 0]
    else:
        if comprobar_infinito(a) == True:
            b = float(b)
            new_b = -2
            if b == new_b: new_b = -2
            t_values = [0, 1/new_b, 1/b]
        else:
            a = float(a)
            new_a = 1
            if b == new_a: new_b = 2
            t_values = [1/a, new_b, b]

    for i in range(len(t_values) - 1): 
        t_i = t_values[i]
        t_j = t_values[i + 1]
        if t_i != 0 and t_j != 0:
            n = ask_for_int("el número de segmentos para el método el trapecio")
            r = ejecutar_metodo_Trapecio(function_original, n, 1/t_i, 1/t_j)
            print(r)
            valor_integral += r
        else:
            n = ask_for_int("el número de segmentos para el método del rectángulo")
            r = Rectangulo(f"-{function_str}", n, t_j, t_i)
            print(r)
            valor_integral += r

    print(valor_integral)
    


