import os
import modules.menu as menu
import modules.regempleado as re
isActive = True 
while isActive:
    os.system('cls')
    op = menu.menu()
    if (op == 1):
        re.empleado()
    if (op == 2):
        pass
    if (op == 3):
        isActive = False
        print('Muchas gracias por hacer uso del software')
        os.system('pause')