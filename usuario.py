import os
if __name__ == '__main__':
    isactive = True
    dicfin ={}
    while isactive:
        try:
            os.system('cls')
            print('Bienvenido usuario ')
            print('Porfavor ingrese su id ')
            id = int(input(':)_ '))
            print('Porfavor ingrese su nombre ')
            name = str(input(':)_ '))
            print('Porfavor ingrese sus apellidos ')
            name2 = str(input(':)_ '))
            print('Porfavor ingrese su direccion ')
            dir = str(input(':)_ '))
            print('Porfavor ingrese su ciudad ')
            city = str(input(':)_ '))
            print(f'Porfavor ingrese la longitud de {city}')
            lon = str(input(':)_ '))
            print(f'Porfavor ingrese la latitud de {city}')
            lat = str(input(':)_ '))
            print('Porfavor ingrese su email ')
            email = str(input(':)_ '))
            print('Porfavor ingrese su edad ')
            edad = int(input(':)_ '))
            print('Ingrese su ocupacion')
            ocup = str(input(':)_ '))
        except ValueError:
            print('Tipo de dato no valido para el item')
            os.system('pause')
        else:
            diccinfo = {
                "id": id,
                "nombre": name,
                "apellidos": name2,
                "ubicacion":{
                    "direccion":dir,
                    "lon": lon,
                    "lat": lat
                },
                "email": email,
                "edad": edad,
                "ocuapcion": ocup
            }
            dicfin.update({id:diccinfo})
            print('Su informacion fue registrada con exito')
            print(list(diccinfo))
            print('Desea agregar otra personas,S(si) Enter(no?')
            des = bool(input(':)_ '))
            if (des == True):
                isactive = True
            else:
                isactive = False
                print('Diccionario con todos los registros hechos,')
                print(list(dicfin.items()))
