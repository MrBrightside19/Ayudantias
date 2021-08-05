
"""
Integrantes: Diego Alonso Bravo Quezada, Rodrigo Ignacio Baos Henriquez, 
             Jacqueline Elena Palma Moya, Benjamin Eduardo Perez Lopez                          
"""
import random
import os
import colorama

colorama.init()

from colorama import init, Fore, Back, Style
init(autoreset = True)

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

Atrapado = 0 ; Segundos = 0 ; PasosEstafador = 0 ; PasosAgente = 0

EstafadorColumna = random.randint(2,21)
EstafadorFila = random.randint(2,21)

AgenteColumna = random.randint(2,21)
AgenteFila = random.randint(2,21)

while abs(EstafadorColumna - AgenteColumna) <=2 and abs(EstafadorFila - AgenteFila) <=2:
    AgenteColumna = random.randint(2,21)
    AgenteFila = random.randint(2,21)

os.system("cls")

print(" 123456789X123456789X")

for i in range (1,11):
    if i == 10 :
        print ("X")
    else:
        print(i)
for i in range (1,11):
    if i == 10 :
        print ("X")
    else:
        print(i)
pos(EstafadorFila,EstafadorColumna); print(Back.RED + Fore.BLACK + "E")
pos(AgenteFila,AgenteColumna); print(Back.CYAN + Fore.BLACK + "A")    
    
Saltos = 0
Saltos = 21 - AgenteFila
for i in range (Saltos):
    print()
print("Tiempo         : ", Segundos, " segundos")
print("Pasos Estafador: ", PasosEstafador)
print("Pasos Agente   : ", PasosAgente)
input()

while Segundos < 70 and Atrapado == 0:
    os.system("cls")
    Segundos += 1
    Turno = random.randrange(2)
    
    if Turno == 0:
        PasosEstafador += 1
        if EstafadorFila > AgenteFila:
            EstafadorFila += 1
            
        elif EstafadorFila < AgenteFila:
            EstafadorFila = EstafadorFila - 1
            
        if EstafadorColumna > AgenteColumna:
            EstafadorColumna += 1
            
        elif EstafadorColumna < AgenteColumna:
            EstafadorColumna = EstafadorColumna - 1
            
        if EstafadorFila > 21 or EstafadorColumna > 21 or EstafadorFila < 2 or EstafadorColumna < 2:
            EstafadorColumna = random.randint(2,21)
            EstafadorFila = random.randint(2,21)
    else:
        PasosAgente += 1
        if AgenteFila < EstafadorFila:
            AgenteFila += 1
            
        elif AgenteFila > EstafadorFila:
            AgenteFila = AgenteFila - 1
            
        if AgenteColumna < EstafadorColumna:
            AgenteColumna += 1
            
        elif AgenteColumna > EstafadorColumna:
            AgenteColumna = AgenteColumna - 1
            
    if EstafadorFila == AgenteFila and EstafadorColumna == AgenteColumna:
        Atrapado = 1
    print(" 123456789X123456789X")

    for i in range (1,11):
        if i == 10 :
            print ("X")
        else:
            print(i)
    for i in range (1,11):
        if i == 10 :
            print ("X")
        else:
            print(i)
    pos(EstafadorFila,EstafadorColumna); print(Back.RED + Fore.BLACK + "E")
    pos(AgenteFila,AgenteColumna); print(Back.CYAN + Fore.BLACK + "A")    
        
    Saltos = 0
    Saltos = 21 - AgenteFila
    for i in range (Saltos):
        print()
    print("Tiempo         : ", Segundos, " segundos")
    print("Pasos Estafador: ", PasosEstafador)
    print("Pasos Agente   : ", PasosAgente)
    print("")
    if Atrapado == 1 :
        if Segundos < 20:
            print("El agente Carl Hanratty atrapo al estafadador Frank Abagnale Jr. luego de solo ", Segundos, " segundos!")
        else:
            print("El estafador fue atrapado!")
    elif Segundos == 70: 
        print("Se acabo el tiempo y el estafador escapo!")
    
    input()  
        

# Diseño de tablero simple, ejecucion cumple y funciona correctamente, podria ser mas eficiente
# NOTA?: 100