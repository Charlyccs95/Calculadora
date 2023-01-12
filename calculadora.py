def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    while True:
        print('************')
        print('Calculadora')
        print('************')
        print('Seleccione una operacion a realizar')
        print('Menu')
        print('1) Suma')
        print('2) Resta')
        print('3) Multiplicacion')
        print('4) Division')
        print('5) raiz n')
        print('6) Exponente')
        print('7) Seno')
        print('8) Apagar o Terminar')
        opc = input("Ingresa el numero de la operacion deseada: ")
        try:
            opc = int(opc)
            while (opc > 0 and opc <=8):
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
                    elif (opc>= 8):
                        print("""
                        
Adios, gracias por usar mi calculadora

""")
                        quit()
        except ValueError:
            print ("La entrada es incorrecta: escribe un numero entero")
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
