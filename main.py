#importaciones
from programas.sumar import sumar2
from programas.restar import restar2
from vistas.menu import menu2
from vistas.lineas import c_lineas
from datetime import datetime 

import time

#modulos de python
import os

programa = True
os.system("clear")
while True:
    hora_actual = datetime.now().strftime("%H:%M:%S")
    print("Hora actual:", hora_actual, end="\r")  # sobrescribe la línea
    time.sleep(1)  # espera 1 segundo
#repetir un código mientras dure una determinada condición
while(programa):
    c_lineas(30)
    menu2()
    

    res = int(input("[?] "))

    if res ==1:
        print("sumar dos números")
        sumar2()
        
#elif es como un sino
    elif res ==2:
        print("restar dos números")
        restar2()   
    elif res ==0:
        print("salir del programa")
        programa = False
        #aqui con el false cerramos el programa
