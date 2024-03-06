import os
titulo = """
    +++++++++++++++++++++++++++++++++++++++++++
    +Pago de la nomina mensual de los empleados+
    +++++++++++++++++++++++++++++++++++++++++++
""" 
lstopciones = [1,2,3]
opciones = ('1.Registro empleado\n2.Gerencia\n3.Salir')
def menu():
    os.system('cls')
    print(titulo)
    print(opciones)
    try:
        op = int (input(':)_ '))
        if (not op in lstopciones):
            print('numero no valido')
            os.system('pause')
            menu()
    except ValueError:
        print('Error en el dato ingresado')
        os.system('pause')
        menu()
    else:
        return op
                