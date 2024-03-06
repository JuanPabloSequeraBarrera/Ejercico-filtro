import os 
import modules.menu as menu
def empleado():
    empleados = {}
    facturas = {}
    print(menu.titulo)
    cargo = ('almacenista','jefe IT','Administrador','mensajero','gerente')
    print('Bienvenido al registro de empleados')
    try:
        print('Digite el id del empleado')
        id = int(input(':)_ '))
        print('Digite el id nombre del empleado')
        nombre = str(input(':)_ '))
        print('Ingrese la fecha del registro')
        fecha = str(input(':)_ '))
        print('Seleccione el mes a facturar')
        mes = str(input(':)_ '))
        print(f'Escriba el tipo de empleado de {nombre}')
        print(cargo)
        carg = str(input(":)_ ")).lower()
        if (carg in cargo):
            print('Cuantos dias trabajó')
            dias = int(input(':)_ '))
            print('Cuanto le pagan por dia')
            valordia = float(input(':)_ ')) 
            print('Trabajó horas extras?')
            extra= bool(input('Si(s) No(enter)'))
            if (extra == True):
                print('¿cuantas horas trabajo?')
                horaext = int(input(':)_ '))
                tothoras = (horaext*5500)
            else:
                pass
            print('Debe algo en la cafeteria?')
            caf= bool(input('Si(s) No(enter)'))
            if (caf == True):
                print('¿cuanto debe?')
                cafeteria = float(input(':)_ '))
            else:
                    pass
            print('Tiene cuota de prestamo?')
            pres= bool(input('Si(s) No(enter)'))
            if (pres == True):
                print('¿cuanto paga?')
                prestamo = float(input(':)_ '))
            else: 
                        pass
            sueldo = ((dias*valordia)+(tothoras)-(prestamo)-(cafeteria))
            sueldobase = (dias*valordia)
            emp = {
                 'id':id,
                 'Nombre':nombre,
                 'cargo': cargo,
                 'salario': sueldo
            }
            empleados.update({id:emp})
            fact = {
                'id': id,
                'mes pagado': mes,
                'fecha': fecha,
                'sueldo': sueldobase,
                'horasextras': horaext,
                'prestamo': prestamo,
                'cafeteria': cafeteria,
                'totalpagado':sueldo
            }
            facturas.update({id:fact})
        else:
            print('Tipo de cargo no encontrado, desea volver a intentar? Si(s) No(Enter)')
            resp = bool(input(':)_ '))
            if (resp == True):
                empleado()
            else:
                return
    except ValueError:
        print('Dato ingresado no es valido')
        os.system('pause')
        empleado