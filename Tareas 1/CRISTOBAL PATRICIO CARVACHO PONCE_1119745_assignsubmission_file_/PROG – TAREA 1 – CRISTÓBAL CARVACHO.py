"""
Integrantes:
Cristóbal Patricio Carvacho Ponce
Javier Ignacio Marambio Lagos
Cristian Antonio Morales Cortés
"""
### BIBLIOTECAS ###
from colorama import init, Back
init(autoreset = True)
import random
import os
os.system ("cls")
#DEFINIR AGENTE Y ESTAFADOR
agente_y = random.randint(1,20)
agente_x = random.randint(1,20)
estafador_y = random.randint(1,20)
estafador_x = random.randint(1,20)
while abs(agente_x - estafador_x) < 3:
	agente_x = random.randint(1,20)
while abs(agente_y - estafador_y) < 3:
	agente_y = random.randint(1,20)
#DEFINIR VARIABLES
tiempo = 0
sw = 0
more_a = 0
more_e = 0
pasos_agente = 0
pasos_estafador = 0
### TABLA ###
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="");
    return None
pos(1,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  1")
pos(2,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  2")
pos(3,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  3")
pos(4,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  4")
pos(5,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  5")
pos(6,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  6")
pos(7,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  7")
pos(8,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  8")
pos(9,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  9")
pos(10,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 10")
pos(11,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 11")
pos(12,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 12")
pos(13,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 13")
pos(14,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 14")
pos(15,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 15")
pos(16,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 16")
pos(17,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 17")
pos(18,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 18")
pos(19,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 19")
pos(20,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 20")
pos(21,1); print("  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20  ")
#AGENTE Y ESTAFADOR EN TABLA
pos (agente_y, agente_x*3); print (Back.BLUE + "A")
pos (estafador_y, estafador_x*3); print (Back.RED + "E")
pos (23,1); print ("Tiempo: ", tiempo, "segundos")
pos (25,1); print ("Pasos del agente: ", pasos_agente)
pos (27,1); print ("Pasos del estafador: ", pasos_estafador)
input()
while sw == 0:
    def pos(x,y):
        print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="");
        return None
    pos(1,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  1")
    pos(2,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  2")
    pos(3,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  3")
    pos(4,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  4")
    pos(5,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  5")
    pos(6,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  6")
    pos(7,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  7")
    pos(8,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  8")
    pos(9,1); print ("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  9")
    pos(10,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 10")
    pos(11,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 11")
    pos(12,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 12")
    pos(13,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 13")
    pos(14,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 14")
    pos(15,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 15")
    pos(16,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 16")
    pos(17,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 17")
    pos(18,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 18")
    pos(19,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 19")
    pos(20,1); print("  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  + 20")
    pos(21,1); print("  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20  ")
    tiempo += 1
    turno = random.randint(1,2)
	# Agente = 1
	# Estafador = 2
    if turno == 1:
        pasos_agente += 1
        #columna
        if estafador_y > agente_y:
            agente_y += 1
        elif estafador_y < agente_y:
            agente_y -= 1
        #fila
        if estafador_x > agente_x :
            agente_x += 1
        elif estafador_x < agente_x:
            agente_x -= 1
        # si el agente sobrepasa los limites columna
        if agente_y > 20:
            agente_y = 1
        elif agente_y < 1:
            agente_y = 20
        # si el agente sobrepasa los limites Fila
        if agente_x > 20:
            agente_x = 1
        elif agente_x < 1:
            agente_x = 20
            
    elif turno == 2:
        pasos_estafador += 1
        if agente_y < estafador_y :
            estafador_y += 1
        elif agente_y > estafador_y:
            estafador_y -= 1
        if agente_x < estafador_x :
            estafador_x += 1
        elif agente_x > estafador_x:
            estafador_x -= 1
        # si el estafador sobrepasa los limites columna
        if estafador_y > 20:
            estafador_y = random.randrange (1,20)
            estafador_x = random.randrange(1,20)
        elif estafador_y < 1:
            estafador_y = random.randrange(1,20)
            estafador_x = random.randrange(1,20)
        # si el estafador sobrepasa los limites fila
        elif estafador_x > 20:
            estafador_x = random.randrange(1,20)
            estafador_y = random.randrange(1,20)
        elif estafador_x < 1:
            estafador_x = random.randrange(1,20)
            estafador_y = random.randrange(1,20)
    if estafador_y == agente_y and estafador_x == agente_x:
        sw = 1
    if tiempo == 70 :
        sw = 2
    pos (estafador_y, estafador_x*3); print (Back.RED + "E")
    pos (agente_y, agente_x*3); print (Back.BLUE + "A")
    pos (23,1); print ("Tiempo: ", tiempo, "segundos")
    pos (25,1); print ("Pasos del agente: ", pasos_agente)
    pos (27,1); print ("Pasos del estafador: ", pasos_estafador)
    if sw == 1:
        pos(29,1); print("El estafador ha sido capturado")
    elif sw == 2:
        pos(29,1); print ("El estafador logró escapar")
    input()

# Ejecucion funciona correctamente, podria ser mas eficiente, validaciones correctas
# NOTA: 100