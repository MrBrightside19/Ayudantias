#### TRABAJO DE PROGRAMACION
#### INTEGRANTES: MATIAS RIQUELME Y PYA PEREZ
#### PARALELO: 192-B o 301
import random
import colorama
from colorama import init, Fore, Back, Style
import os
os.system('cls')

init()
def pos(fila,colum):
    return "\033[" + str(fila) + ";" + str(colum) + "H"

######|posicion Agente

AgenteCol = random.randint(1,20)
AgenteFil = random.randint(1,20)

######|Posicion Estafador

Listo="No"
while Listo=="No":
    EstafCol = random.randint(1,20)
    EstafFil = random.randint(1,20)
     
   
    if EstafCol!=AgenteCol and EstafFil!=AgenteFil and abs(AgenteCol - EstafCol) >= 2 and abs(AgenteFil - EstafFil) >= 2:
        Listo="Si"



######|Comienzo    Capturado="No"
Capturado="No"
Tiempo=0
######|Comienzo de la persecucion 
while Capturado=="No" and Tiempo<70:

######|Turnos de movimiento
    Turno=random.randint(0,1)

######|Movimiento Agente
    if Turno==0:
        if EstafCol> AgenteCol:
            AgenteCol = AgenteCol + 1
            if AgenteCol==21:
                AgenteCol= AgenteCol-20

        if EstafCol<AgenteCol:
            AgenteCol = AgenteCol - 1
            if AgenteCol==0:
                AgenteCol= AgenteCol + 20

        if EstafFil>AgenteFil:
            AgenteFil = AgenteFil + 1
            if AgenteFil==21:
                AgenteFil= AgenteFil - 20

        if EstafFil<AgenteFil:
            AgenteFil = AgenteFil - 1
            if AgenteFil==0:
                AgenteFil= AgenteFil + 20
            
######|Movimiento Estafador
    if Turno==1:

        if AgenteCol< EstafCol:
            EstafCol = EstafCol + 1
            if EstafCol== 21:
                EstafCol = random.randint(1,20)

        if AgenteCol>EstafCol:
            EstafCol = EstafCol - 1
            if EstafCol== 0:
                EstafCol= random.randint(1,20)

        if AgenteFil<EstafFil:
            EstafFil = EstafFil+ 1
            if EstafFil== 21:
                EstafFil= random.randint(1,20)

        if AgenteFil>EstafFil:
            EstafFil = EstafFil - 1
            if EstafFil == 0:              
                EstafFil=random.randint(1,20)

    if AgenteCol==EstafCol and AgenteFil==EstafFil:
        Capturado="Si"

    
######|Tablero
    colum = 0
    fila = 0
    while colum < 20 and fila < 20:
        print(pos(fila+3,colum+4) + " . . . . . . . . . . . . . . . . . . . . ")
        fila += 1

    print(pos(EstafCol+2,EstafFil*2+3)+ Fore.RED + "E")
    print(pos(AgenteCol+2,AgenteFil*2+3)+ Fore.BLUE + "A")

    pos(28,0);print(Fore.RESET)

    fila = 5  #Numeracion Arriba
    numeracionx = 1
    while numeracionx <= 20:
        if numeracionx >= 10:
            print(pos(1,fila) + str(numeracionx-10))
            if numeracionx == 10:
                print(pos(1,fila) + "1")
                print(pos(2,fila) + "0")
            if numeracionx == 20:
                print(pos(1,fila) + "2")
                print(pos(2,fila))
        else:
            print(pos(1,fila) + str(numeracionx))
        numeracionx += 1
        fila += 2
        #print(pos(AgenteFil,EstafFil))
    
    colum = 3   #Numeracion Abajo
    numeraciony = 1
    while numeraciony <= 20:
        if numeraciony >= 10:
            print(pos(colum,2) + str(numeraciony-10))
            if numeraciony == 10:
                print(pos(colum,1) + "1")
            if numeraciony == 20:
                print(pos(colum,2) + "20")
        else:
            print(pos(colum,2) + str(numeraciony))
        numeraciony += 1
        colum += 1


    
    Tiempo = Tiempo + 1
    
######|Condiciones para finalizar  
    print()
    pos(29,0);print("Agente: ",str(AgenteFil)+","+str(AgenteCol),"  ")
    pos(31,0);print("Estafador: ",str(EstafFil)+","+str(EstafCol),"  ")
    pos(33,0);print("Tiempo: ",Tiempo)
       
    input()
if Capturado =="Si":
    print("El Estafador ha sido capturado")
    
if Tiempo==70:
    print("El Estafador ha escapado") 


input()

#Ejecucion con fallas, si quedan ambos personajes en la misma fila o columna juegan
# en la misma linea, estafador tiende a devolverse hacia el agente

# Nota: 80 - 90