import os
if __name__  == '__main__':
    titulo = """
    +++++++++++++++++++++++++++++++++++++++
    +SOFTWARE DE CAMBIOS DE DIVISAS S.A.S +         
    +++++++++++++++++++++++++++++++++++++++
    """
    isActive = True
    lstop = [1,2,3,4,5]
    print('Porfavor seleccione el tipo de cambio que desea hacer')
    opciones = ('1.Pesos a dolares\n2.Pesos a euros\n3.euros a pesos\n4.pesos a yenes\n5.Salir')
    while isActive:
        try:
            os.system('cls')
            print(titulo)
            print(opciones)
            op = int(input(':)_'))
            if (op in lstop):
                if (op ==1):
                    try:
                        print('Ingrese el valor en COP que desea convertir a USD')
                        cop = float(input(':)_ '))
                        operacion = (cop/(3944))
                    except ValueError:
                        print('Cantidad ingresada no es valida con un valor nuemrico')
                        os.system('pause')
                    else:
                        print(f'La cantidad de usd de {cop} son {operacion}')
                        os.system('pause')
                elif (op ==2):
                    try:
                        print('Ingrese el valor en COP que desea convertir a EUR')
                        cop = float(input(':)_ '))
                        operacion = (cop/(4276))
                    except ValueError:
                        print('Cantidad ingresada no es valida con un valor nuemrico')
                        os.system('pause')
                    else:
                        print(f'La cantidad de EUR de {cop} son {operacion}')
                        os.system('pause')
                elif (op ==3):
                    try:
                        print('Ingrese el valor en EUR que desea convertir a COP')
                        euro = float(input(':)_ '))
                        operacion = ((4276)/euro)
                    except ValueError:
                        print('Cantidad ingresada no es valida con un valor nuemrico')
                        os.system('pause')
                    else:
                        print(f'La cantidad de EUR de {euro} son {operacion}')
                        os.system('pause')
                elif (op ==4):
                    try:
                        print('Ingrese el valor en COP que desea convertir a YEN')
                        cop = float(input(':)_ '))
                        operacion = (cop/(26.30))
                    except ValueError:
                        print('Cantidad ingresada no es valida con un valor nuemrico')
                        os.system('pause')
                    else:
                        print(f'La cantidad de YEN de {cop} son {operacion}')
                        os.system('pause')
                elif (op ==5):
                    print('Vuelva pronto')
                    isActive = False
            else:
                print('Numero ingresado no es valido')
                os.system('pause')
        except ValueError:
            print('Opcion seleccionada no es valida')
            os.system('pause')
            isActive = True
