import os 
import modules.corefiles as core
if (__name__ == '__main__'):
    os.system('cls')
    print('Bienvenido usuario')
    print('Ingrese el id del viver a ingresar')
    id = int(input(':)_ '))
    print('Ingrese el nombre del viver a ingresar')
    nombre = str(input(':)_ '))
    print('Ingrese el valor del viver a ingresar')
    valor = int(input(':)_ '))
    print('Ingrese el stock minimo del viver')
    min = int(input(':)_ '))
    print('Ingrese el stock maximo del viver')
    max = int(input(':)_ '))
    dicinventario = {
        'id': id,
        'name':nombre,
        'valor': valor,
        'stockmin': min,
        'stockmax': max
    }
    core.checkFile('inventario.json', {})
    core.UpdateFile('inventario.json',{id:dicinventario})