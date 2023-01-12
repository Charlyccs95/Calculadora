import numpy as np
import os
from time import sleep
import math


def Suma():
    x = int(input("Ingrese el primer número a sumar\n"))
    y = int(input("Ingrese el segundo número a sumar\n"))
    arr1 = np.array([x])
    arr2 = np.array([y])
    respuesta = np.add(arr1, arr2)
    myorder = "La Suma de {0} + {1} es: {2}"
    print(myorder.format(x, y, respuesta))
    sleep(3)
    print("""
    
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Suma()
    elif (opci == "no" or opci != "si"):
        repeat()


def Resta():
    x = int(input("Ingrese el primer número\n"))
    y = int(input("Ingrese el segundo número\n"))
    arr1 = np.array([x])
    arr2 = np.array([y])
    respuesta = np.subtract(arr1, arr2)
    myorder = "La resta de {0} - {1} es: {2}"
    print(myorder.format(x, y, respuesta))
    sleep(3)
    print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Resta()
    elif (opci == "no" or opci != "si"):
        repeat()


def Multiplicacion():
    x = int(input("Ingrese el primer número\n"))
    y = int(input("Ingrese el segundo número\n"))
    arr1 = np.array([x])
    arr2 = np.array([y])
    respuesta = np.multiply(arr1, arr2)
    myorder = "La Multiplicacion de {0} * {1} es: {2}"
    print(myorder.format(x, y, respuesta))
    sleep(3)
    print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Multiplicacion()
    elif (opci == "no" or opci != "si"):
        repeat()


def Division():
    x = int(input("Ingrese el primer número\n"))
    y = int(input("Ingrese el segundo número\n"))
    try:
        myorder = "La División de {0} / {1} es: {2}"
        print(myorder.format(x, y, x/y))
        print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
        """)
        opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
        if (opci == "si"):
            Division()
        elif (opci == "no" or opci != "si"):
            repeat()
    except ZeroDivisionError:
        print("No se Permite la Division Entre 0")
        sleep(3)
        print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
        """)
        opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
        if (opci == "si"):
            Division()
        elif (opci == "no" or opci != "si"):
            repeat()


def Raiz():
    x = int(input("Ingrese número al que desea calular su raiz\n"))
    y = int(input("Ingrese el indice de la raiz\n"))
    myorder = "{1}√{0} es: {2}"
    result = pow(x, 1/y)
    print(myorder.format(x, y, result))
    sleep(3)
    print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Raiz()
    elif (opci == "no" or opci != "si"):
        repeat()


def Exponente():
    x = int(input("Ingrese número\n"))
    y = int(input("Ingrese la potencia a elevar el numero anterior\n"))
    arr1 = np.array([x])
    arr2 = np.array([y])
    respuesta = np.power(arr1, arr2)
    myorder = "{0} a la {1}.ª es: {2}"
    print(myorder.format(x, y, respuesta))
    sleep(3)
    print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Exponente()
    elif (opci == "no" or opci != "si"):
        repeat()


def Sen():
    x = int(input("Ingrese número\n"))
    respuesta = math.sin(x)
    myorder = "El seno de {0} es: {1}"
    print(myorder.format(x, respuesta))
    sleep(3)
    print("""
Tecleea:
Si / para realizar la misma operación
NO / para realizar otra operación diferente
    """)
    opci = str(input("¿Desea realizar de nuevo la operación?\n").lower())
    if (opci == "si"):
        Sen()
    elif (opci == "no" or opci != "si"):
        repeat()


def Calculadora():
    """Funcion Para Calcular operaciónes Aritmeticas"""
    while True:
        print('************')
        print('Calculadora')
        print('************')
        print('Seleccione una operación a realizar')
        print('Menu')
        print('1) Suma')
        print('2) Resta')
        print('3) Multiplicacion')
        print('4) Division')
        print('5) raiz n')
        print('6) Exponente')
        print('7) Seno')
        print('8) Apagar o Terminar')
        opc = input("Ingresa el número de la operación deseada: ")
        try:
            opc = int(opc)
            while (opc > 0 and opc <= 8):
                if (opc > 0 and opc <= 8):
                    if (opc == 1):
                        Suma()
                    elif (opc == 2):
                        Resta()
                    elif (opc == 3):
                        Multiplicacion()
                    elif (opc == 4):
                        Division()
                    elif (opc == 5):
                        Raiz()
                    elif (opc == 6):
                        Exponente()
                    elif (opc == 7):
                        Sen()
                    elif (opc >= 8):
                        print("""
                        
Adios, gracias por usar mi calculadora

""")
                        quit()
        except ValueError:
            print("""
            
La entrada es incorrecta: escribe un número entero

""")
            sleep(3)
            repeat()


def repeat():
    try:
        while True:
            os.system("cls")  # limpia la consola
            Calculadora()
    except KeyboardInterrupt:
        os.system("cls")  # limpia la consola
        repeat()


repeat()