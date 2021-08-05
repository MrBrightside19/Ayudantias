# -*- coding: utf-8 -*-
"""
integrantes y compositores de posible solución a tarea 1:
    Nicolás González 
    Daniel Rozas 
    Carlos Moil 
    Matías Olmos
    
"""
import random
import os
os.system ('cls')

from colorama import init
init()
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end ="")
    return None

Estatafador = 'E'
Agente = 'A'
ColAgente = 0
FilAgente = 0
ColEstafador = 0
FilEstafador = 0
Tiempo = 0
SW = 1
print("Ha comenzado: Atrapame Si Puedes")
input()
os.system('cls')

input() 
while SW == 1 :
    SW = 0
    ColAgente = random.randint(1, 20); FilAgente = random.randint(1, 20)
    FilEstafador = random.randint(1, 20); ColEstafador = random.randint(1, 20)
    if ColAgente == ColEstafador and FilAgente == FilEstafador:
        SW = 1
    if ColAgente <= (ColEstafador + 2) and ColAgente >= (ColEstafador - 2):
        SW = 1
    if FilAgente <= (FilEstafador + 2) and FilAgente >= (FilEstafador - 2):
        SW = 1
        




pos(ColAgente, FilAgente); print("A")
pos(ColEstafador, FilEstafador); print("E")
input()
os.system('cls')


cont_pasos_E = 0
cont_pasos_A = 0





########################## M O V I E N T O S #########################

while Tiempo <= 70:
    Tiempo = Tiempo + 1
    
    mov = random.randint(1, 2) # Random para determinar quien se mueve #
                               # 1 = Estafador
                               # 2 = Agente
    
    if mov == 1:
        cont_pasos_E = cont_pasos_E + 1
        pos (22,1) ; print ("Estafador se comienza a mover")
                #Casos de movimientos Rectos
        #OESTE            
        if FilEstafador == FilAgente and ColEstafador < ColAgente:
            ColEstafador = ColEstafador - 1 
        #ESTE    
        if ColEstafador > ColAgente and FilEstafador == FilAgente:
            CColEstafador = ColEstafador + 1
        #NORTE
        if FilEstafador < FilAgente and ColEstafador == ColAgente:
            FilEstafador = FilEstafador - 1
        #SUR    
        if FilEstafador > FilAgente and ColEstafador == ColAgente:
            FilEstafador = FilEstafador + 1
        # Casos movimiento Diagonales #
            #SurOeste:
        if ColEstafador < ColAgente and FilEstafador > ColAgente:
            ColEstafador = ColEstafador - 1
            FilEstafador = FilEstafador + 1
            #SurEste:
        if ColEstafador > ColAgente and FilEstafador > ColAgente:
            ColEstafador = ColEstafador + 1
            FilEstafador = FilEstafador + 1                
            #NorEste:
        if ColEstafador > ColAgente and FilEstafador < ColAgente:
            ColEstafador = ColEstafador + 1
            FilEstafador = FilEstafador - 1
            #NorOeste:
        if ColEstafador < ColAgente and FilEstafador < ColAgente:
            ColEstafador = ColEstafador - 1
            FilEstafador = FilEstafador - 1
            # Caso en que se sale de los parametros #
        if ColEstafador > 20 or ColEstafador < 1:
            ColEstafador  = random.randint(1, 20) ; FilEstafador  = random.randint(1, 20)
        if FilEstafador > 20 or FilEstafador < 1:
            FilEstafador  = random.randint(1, 20) ; ColEstafador  = random.randint(1, 20)
        pos(ColAgente, FilAgente); print("A")
        pos(ColEstafador, FilEstafador); print("E")
        
        pos(23,1) ; print("La persecución tiene una duración de: ", Tiempo, "segundos.")
        pos(24,1); print("Cantidad de pasos del estafador: ", cont_pasos_E)
        pos(25,1) ; print("Cantidad de pasos del agente: ", cont_pasos_A)
        input()
        os.system('cls')            
# El turno de movimiento es para el AGENTE 
    if mov == 2:
        pos (22,1) ; print ("Agente se comienza a mover")
        cont_pasos_A = cont_pasos_A + 1 
                # Casos de movimientos Rectos
        #ESTE        
        if ColAgente < ColEstafador and FilAgente == FilEstafador:
            ColAgente = ColAgente + 1
        #OESTE    
        if ColAgente > ColEstafador and FilAgente == FilEstafador:
            ColAgente = ColAgente - 1
        #SUR   
        if FilAgente < FilEstafador and ColAgente == ColEstafador:
            FilAgente = FilAgente + 1
        #NORTE
        if FilAgente > FilEstafador and ColAgente == ColEstafador:
            FilAgente = FilAgente - 1
        # Casos de movimientos Diagonales 
                #SurOeste:
        if ColAgente > ColEstafador and FilAgente < FilEstafador:
            ColAgente = ColAgente - 1
            FilAgente = FilAgente + 1
            #SurEste:
        if ColAgente < ColEstafador and FilAgente < FilEstafador:
            ColAgente = ColAgente + 1
            FilAgente = FilAgente + 1
            #NorEste:
        if ColAgente < ColEstafador and FilAgente > FilEstafador:
            ColAgente = ColAgente + 1
            FilAgente = FilAgente - 1
            #NorOeste:
        if ColAgente > ColEstafador and FilAgente > FilEstafador:
            ColAgente = ColAgente - 1
            FilAgente = FilAgente - 1
        pos(ColEstafador, FilEstafador); print("E")
        pos(ColAgente, FilAgente); print("A")
        pos(23,1);print("La persecución tiene una duración de: ", Tiempo, "segundos.")
        pos(24,1); print("Cantidad de pasos del estafador: ", cont_pasos_E)
        pos (25,1) ; print("Cantidad de pasos del agente: ", cont_pasos_A)
        input()
        os.system('cls')
        
        if ColAgente == ColEstafador and FilAgente == FilEstafador:
            pos(ColAgente, FilAgente); print("X")
            pos(22,1);print("El estafador ha sido capturado")
            pos(23,1);print("La persecución tuvo una duración de: ", Tiempo, "segundos.")
            pos(24,1); print("Cantidad de pasos del estafador: ", cont_pasos_E)
            pos (25,1) ; print("Cantidad de pasos del agente: ", cont_pasos_A)
            Tiempo = 80
            input()
            os.system('cls')
    if Tiempo == 70:
        pos(22,1);print("El estafador logró escapar")
        pos(23,1);print("La persecución tuvo una duración de: ", Tiempo, "segundos.")
        pos(24,1);print("Cantidad de pasos del estafador: ", cont_pasos_E)
        pos(25,1);print("Cantidad de pasos del agente: ", cont_pasos_A)     
        input()
        input()#dejar solo 1 input()
        input()
        
# Codigo cumple con los requisitos, buena ejecuccion, sin visualizacion de tablero
# nota: 100

