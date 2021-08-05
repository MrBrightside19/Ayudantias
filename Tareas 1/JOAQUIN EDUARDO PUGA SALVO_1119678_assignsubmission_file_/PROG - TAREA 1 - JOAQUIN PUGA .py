# Integrantes: 
# Eduardo Andrés Maturana Cáceres
# Nicolas Ignacio Saavedra Meneses
# Esteban Exequiel Reyes Lagos 
# Joaquín Eduardo Puga Salvo

from colorama import init, Back, Fore
from random import randint as r
import os
import win32ui

def mostrar_por_pantalla(columna , fila): #funcion que muestra el tablero , posiciones de los personajes e informacion de ellos por la consola 
    print ("\033[" + str(columna) + ";" + str(fila)+ "H" , sep = "" , end = "")
    return None

def movimietos_personajes(personaje_x , personaje_y , personaje2_x , personaje2_y , pasos , turno ): #  funcion que recibe las coordenadas de los personajes para 
                                                                                                     #  poder realizar los movimientos de ellos en el tablero 

    pasos += 1

    mostrar_por_pantalla (personaje_y , personaje_x); print(Fore.LIGHTWHITE_EX + Back.BLACK + "·")

    if turno == 1 :
        if personaje_x < personaje2_x:
            personaje_x += 2
        elif personaje_x > personaje2_x:
            personaje_x -= 2
    
        if personaje_y < personaje2_y:
            personaje_y += 1
        elif personaje_y > personaje2_y:
            personaje_y -= 1
    elif turno == 0 :
        if personaje_x < personaje2_x:
            personaje_x -= 2
        elif personaje_x > personaje2_x:
            personaje_x += 2
    
        if personaje_y < personaje2_y:
            personaje_y -= 1
        elif personaje_y > personaje2_y:
            personaje_y += 1

    if turno == 0:
        if (personaje_x == 1 or personaje_x == 43) or (personaje_y == 2 or personaje_y == 23):
            personaje_x = r(3, 42)
            while personaje_x % 2 == 0 :
                personaje_x = r(3, 42)
            personaje_y = r(3 , 22)

    if turno == 0:
        mostrar_por_pantalla (personaje_y , personaje_x); print(Fore.BLACK + Back.LIGHTRED_EX + "E")
        return personaje_x , personaje_y , pasos 
    elif turno == 1 :
        mostrar_por_pantalla (personaje_y , personaje_x); print(Fore.BLACK + Back.LIGHTGREEN_EX + "A")
        return personaje_x , personaje_y , pasos 

def MsgBox(Mensaje="", Titulo="", Tipo= 0): # ventana final con el resultado del programa 
    return win32ui.MessageBox(Mensaje,Titulo,Tipo)

def conclusion (respuesta): # funcion para determinar el resultado mostrado en la funcion msgbox
                            # entregando los parametros correspondientes al resultado de la ejecucion  
    if respuesta == 1:
        ventana = MsgBox("El estafador ha sido capturado.", "Resultado.", 0 + 64)
        if ventana == 1:
            exit()

    elif respuesta == 2:
        ventana = MsgBox("El estafador logró escapar.", "Resultado.", 5 + 64)
        if ventana == 4:
            main()
        elif ventana == 2:
            exit()

def main (): # funcion principal, donde se ejecutara el programa

    columna = 1 ; fila = 1 ; contador = 1 

    init(autoreset= False) 
    print(Back.BLACK) 
    os.system("cls")
#----------------------- generacion del tablero -------------------------------
    mostrar_por_pantalla(1 , 21) ; print (Fore.LIGHTWHITE_EX + "1") 
    mostrar_por_pantalla(1 , 41) ; print (Fore.LIGHTWHITE_EX + "2") 
    mostrar_por_pantalla(12 , 1) ; print (Fore.LIGHTWHITE_EX + "1")
    mostrar_por_pantalla(22, 1) ; print (Fore.LIGHTWHITE_EX + "2")

    while contador < 42:
        auxiliar_fila = str(fila)
        if contador % 2 != 0 and contador > 2 :
            if fila < 10 :
                mostrar_por_pantalla(2 , contador) ; print (Fore.LIGHTWHITE_EX + auxiliar_fila)
                fila += 1
            else : 
                fila = 0
                auxiliar_fila = str(fila)
                mostrar_por_pantalla(2 , contador) ; print (Fore.LIGHTWHITE_EX + auxiliar_fila)
                fila += 1
        else : 
            mostrar_por_pantalla(2 , contador) ; print (" ")
        contador += 1

    contador = 3 

    while contador < 23: 
        auxiliar_columna = str(columna)
        
        if columna < 10 :
            mostrar_por_pantalla(contador , 2) ; print (Fore.LIGHTWHITE_EX + auxiliar_columna)
            columna += 1
        else : 
            columna = 0
            auxiliar_columna = str(columna)
            mostrar_por_pantalla(contador , 2) ; print (Fore.LIGHTWHITE_EX + auxiliar_columna)
            columna += 1
        contador += 1

    columna = 3 
    for i in range (20):
        fila = 3 
        for j in range (39):
            if fila % 2 != 0 and fila > 2 :
                mostrar_por_pantalla(columna,fila); print(Fore.LIGHTWHITE_EX + "·" )
            fila += 1
        columna += 1

    mostrar_por_pantalla(25,1);input (Back.BLACK + Fore.LIGHTWHITE_EX + "Presione enter para posicionar a los personajes...")
    mostrar_por_pantalla(25,1);print (Back.BLACK + Fore.LIGHTWHITE_EX + "                                                  ")
#------------------- posicionamiento de los personajes en el tablero -----------------------
    tiempo = 0
    atrapado = 0; pasos_agente = 0
    escapo = 0; pasos_estafador = 0

    estafador_x = r(3, 42)
    while estafador_x % 2 == 0 :
        estafador_x = r(3, 42)
    estafador_y = r(3 , 22)
    mostrar_por_pantalla (estafador_y , estafador_x); print(Fore.BLACK + Back.LIGHTRED_EX + "E")

    agente_x = r(3, 42)
    while agente_x % 2 == 0 :
        agente_x = r(3, 42)
    agente_y = r(3 , 22)
    mostrar_por_pantalla (agente_y , agente_x); print(Fore.BLACK + Back.LIGHTGREEN_EX + "A")

#----------------- validacion de coordenadas personajes -------------------------------------
    while (abs((agente_x/2) - (estafador_x/2))) <= 2 and (abs(agente_y - estafador_y)) <= 2:
        mostrar_por_pantalla (agente_y , agente_x); print(Fore.LIGHTWHITE_EX + Back.BLACK + "·")
        agente_x = r(3, 42)
        while agente_x % 2 == 0 :
            agente_x = r(3, 42)
        agente_y = r(3 , 22)
        mostrar_por_pantalla (agente_y , agente_x); print(Fore.BLACK + Back.LIGHTGREEN_EX + "A")

    mostrar_por_pantalla(25,1);input (Back.BLACK + Fore.LIGHTWHITE_EX + "presione enter para comenzar ...")

# ----------------------------- comienzo de la persecucion de los personajes --------------------------------
    while atrapado != 1 and escapo != 2:
        tiempo += 1

        turno = r(0,1)
        if turno == 0:
            estafador_x , estafador_y , pasos_estafador  = movimietos_personajes(estafador_x , estafador_y , agente_x , agente_y , pasos_estafador , turno)

        elif turno == 1:
            agente_x , agente_y , pasos_agente  = movimietos_personajes(agente_x , agente_y , estafador_x , estafador_y , pasos_agente , turno)

        mostrar_por_pantalla (25,1) ; print (Fore.LIGHTWHITE_EX + Back.BLACK + "el tiempo transcurrido es de : " , tiempo , " segundos")
        mostrar_por_pantalla (26,1) ; print (Fore.LIGHTWHITE_EX + Back.BLACK + "Pasos del agente:",pasos_agente )
        mostrar_por_pantalla (27,1) ; print (Fore.LIGHTWHITE_EX + Back.BLACK + "Pasos del estafador:",pasos_estafador )

        if agente_x == estafador_x and agente_y == estafador_y:
            atrapado = 1
            mostrar_por_pantalla(agente_y,agente_x) ; print (Fore.BLACK + Back.LIGHTCYAN_EX + "X")
            conclusion(1)

        elif tiempo == 70:
            escapo = 2
            conclusion(2)
        input() 

main()

# Codigo confuso. Cumple con los requistos, completo y funcional
# Nota: 100
