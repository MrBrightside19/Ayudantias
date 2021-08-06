import time
from colorama import init, Back, Fore
from random import randint as r
import os
import win32ui
def MsgBox(Mensaje="", Titulo="", Tipo= 0):
    return win32ui.MessageBox(Mensaje,Titulo,Tipo)

def asignar_posiciones(columna , fila): #--> esta funcion no se toca, porque es la que nos muestra las cosas en la terminal
    print ("\033[" + str(columna) + ";" + str(fila)+ "H" , sep = "" , end = "")
    return None

def conclusion (respuesta):
    if respuesta == 1:
        ventana = MsgBox("El agente atrapo al estafador\n¿Desea reintentar?", "Resultado.", 4 + 64)
        if ventana == 6:
            main()
        elif ventana == 7 :
            os._exit()
    elif respuesta == 2:
        ventana = MsgBox("Lamentablemente el estafador escapo.", "Resultado.", 5 + 64)
        if ventana == 4:
            main()
        elif ventana == 2:
            os._exit()

def main ():
    x = 1 ; y = 1 ; contador = 1 ; tiempo = 0

    init(autoreset= False) # --> el autoreset esta en falso para que se mantenga el color blanco de fondo
    print(Back.LIGHTWHITE_EX) # --> le da el color blanco del fondo
    os.system("cls")

    asignar_posiciones(1 , 21) ; print (Fore.BLACK + "1") # --> son los numeros que estan sobre los 0s de las coordenadas 
    asignar_posiciones(1 , 41) ; print (Fore.BLACK + "2") # tanto como el eje x , como el y
    asignar_posiciones(12 , 1) ; print (Fore.BLACK + "1")
    asignar_posiciones(22, 1) ; print (Fore.BLACK + "2")

    while contador < 42: #--> genera los numeros de el eje x, si me equivoque en la letra, pero despues lo solucionamos
        auxiliar_contador = str(contador)
        auxiliar_y = str(y)
        if contador % 2 != 0 and contador > 2 :
            if y < 10 :
                asignar_posiciones(2 , auxiliar_contador) ; print (Fore.BLACK + auxiliar_y)
                y += 1
            else : 
                y = 0
                auxiliar_y = str(y)
                asignar_posiciones(2 , auxiliar_contador) ; print (Fore.BLACK + auxiliar_y)
                y += 1
        else : 
            asignar_posiciones(2 , auxiliar_contador) ; print (" ")
        contador += 1

    contador = 3 # --> se reinicia la variable para poder usarla en el siguiente eje

    while contador < 23: # --> eje y, aunque diga x, es el y
        auxiliar_contador = str(contador)
        auxiliar_x = str(x)
        
        if x < 10 :
            asignar_posiciones(auxiliar_contador , 2) ; print (Fore.BLACK + auxiliar_x)
            x += 1
        else : 
            x = 0
            auxiliar_x = str(x)
            asignar_posiciones(auxiliar_contador , 2) ; print (Fore.BLACK + auxiliar_x)
            x += 1
        contador += 1

    columna = 3 # termina en 21
    for i in range (20):
        auxiliar_columna = str(columna)
        fila = 3 # termina en 41
        for j in range (39):
            auxiliar_fila = str(fila)
            if fila % 2 != 0 and fila > 2 :
                asignar_posiciones(columna,fila); print(Fore.BLACK + "·" )
            elif fila % 2 == 0 : 
                asignar_posiciones(columna,fila); print(Fore.BLACK + " ")
            fila += 1
        columna += 1
    #-------------------------- movimiento personajes-----------------------------------
    atrapado = 0; pasos_agente = 0
    escapo = 0; pasos_estafador = 0

    estafador_x = r(3, 42)
    while estafador_x % 2 == 0 :
        estafador_x = r(3, 42)
    estafador_y = r(3 , 22)
    asignar_posiciones (estafador_y , estafador_x); print(Fore.BLACK + Back.GREEN + "E")

    agente_x = r(3, 42)
    while agente_x % 2 == 0 :
        agente_x = r(3, 42)
    agente_y = r(3 , 22)
    asignar_posiciones (agente_y , agente_x); print(Fore.BLACK + Back.RED + "A")

    while atrapado != 1 and escapo != 2:
        tiempo += 1

        turno = r(0,1)
        if turno == 0:
            pasos_estafador += 1
            asignar_posiciones (estafador_y , estafador_x); print(Fore.BLACK + Back.WHITE + "·")
            estafador_x = r(3, 42)
            while estafador_x % 2 == 0 :
                estafador_x = r(3, 42)
            estafador_y = r(3 , 22)
            asignar_posiciones (estafador_y , estafador_x); print(Fore.BLACK + Back.GREEN + "E")

        elif turno == 1:
            pasos_agente += 1
            asignar_posiciones (agente_y , agente_x); print(Fore.BLACK + Back.WHITE + "·")
            agente_x = r(3, 42)
            while agente_x % 2 == 0 :
                agente_x = r(3, 42)

            agente_y = r(3 , 22)
            asignar_posiciones (agente_y , agente_x); print(Fore.BLACK + Back.RED + "A")

        asignar_posiciones (25,1) ; print (Fore.BLACK + Back.WHITE + "el tiempo transcurrido es de : " , tiempo , " segundos")
        asignar_posiciones (26,1) ; print (Fore.BLACK + Back.WHITE + "Pasos del agente:",pasos_agente )
        asignar_posiciones (27,1) ; print (Fore.BLACK + Back.WHITE + "Pasos del estafador:",pasos_estafador )
        input()

        if agente_x == estafador_x and agente_y == estafador_y:
            atrapado = 1
            asignar_posiciones(agente_y,agente_x) ; print (Fore.BLACK + Back.LIGHTBLUE_EX + "X")
        elif tiempo == 70:
            asignar_posiciones (25,1) ; print (Fore.BLACK + Back.WHITE + "el tiempo transcurrido es de : " , tiempo , " segundos")
            escapo = 2
    if atrapado == 1:
        conclusion(1)
    elif escapo == 2: 
        conclusion(2)

main()