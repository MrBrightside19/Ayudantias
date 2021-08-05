# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:17:15 2021

@author: diego
"""
#Profesor, perdon por la demora, se me fue la orientación de los días y creí que hoy era Domingo.
#Hice la Tarea yo solo.
#No pude hacer la última parte de generar en pantalla el movimiento de los protagonistas,
#lo que si logré hacer fue posicionar los mensajes que se pedían en pantalla.
#Mil disculpas, saludos.
import colorama
import random 
colorama.init()
import os
os.system('cls')
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

FilAgent = random.randint(1, 20) ; ColAgent = random.randint(1, 20)
FilEst = random.randint(1, 20) ; ColEst = random.randint(1, 20)
while abs(FilAgent - FilEst) <= 2 and abs(ColAgent - ColEst) <= 2 :
    FilEst = random.randint(1, 20) ; ColEst = random.randint(1, 20)
pos(1,1) ; print("Columna Inicial Agente:", ColAgent, "/", "Fila Inicial Agente:", FilAgent)
pos(2,1) ; print( "Columna Inicial Estafador:", ColEst, "/", "Fila Inicial Estafador:", FilEst)

#Aquí se verá al azar quien se moverá primero
Agent = random.randint(1, 10) ; Est = random.randint(1, 10)   
if Agent > Est :
        PrimerMovimiento = "Agente"
elif Agent < Est :
        PrimerMovimiento = "Estafador"
while Agent == Est :
        Agent = random.randint(1, 10) ; Est = random.randint(1, 10)   
        if Agent > Est :
            PrimerMovimiento = "Agente"
        elif Agent < Est :
            PrimerMovimiento = "Estafador"

print("Primero se moverá ", PrimerMovimiento)
Segundos = 0 ; PasosEst = 0 ; PasosAgent = 0
for segundos in range (1, 70) :
    Agent = random.randint(1, 10) ; Est = random.randint(1, 10)   
    if Agent > Est :
        PrimerMovimiento = "Agente"
    elif Agent < Est :
        PrimerMovimiento = "Estafador"
    while Agent == Est :
        Agent = random.randint(1, 10) ; Est = random.randint(1, 10)   
    if Agent > Est :
            PrimerMovimiento = "Agente"
    elif Agent < Est :
            PrimerMovimiento = "Estafador"
           
    if PrimerMovimiento == "Estafador":
        if (ColEst - ColAgent > 0 and FilEst - FilAgent > 0) or (ColEst - ColAgent > 0 and FilEst - FilAgent < 0) or (ColEst - ColAgent > 0 and FilEst - FilAgent == 0) :
            ColEst = ColEst + 1
            
        if (ColEst - ColAgent < 0 and FilEst - FilAgent < 0) or (ColEst - ColAgent < 0 and FilEst - FilAgent > 0) or (ColEst - ColAgent < 0 and FilEst - FilAgent == 0) :
            ColEst = ColEst - 1
            
        if (FilEst - FilAgent < 0 and ColEst - ColAgent == 0) or (FilEst - FilAgent < 0 and ColEst - ColAgent > 0) or (FilEst - FilAgent < 0 and ColEst - ColAgent < 0) :     
            FilEst = FilEst - 1
            
        if (FilEst - FilAgent > 0 and ColEst - ColAgent == 0) or (FilEst - FilAgent > 0 and ColEst - ColAgent < 0) or (FilEst - FilAgent > 0 and ColEst - ColAgent > 0) :
            FilEst = FilEst + 1
            
        while (ColEst == 20 and ColEst - ColAgent > 1) or (ColEst == 1 and ColEst - ColAgent < 1) or (FilEst == 20 and FilEst - FilAgent > 1) or (FilEst == 1 and FilEst - FilAgent < 1) :
             FilEst = random.randint(1, 20) ; ColEst = random.randint(1, 20)
             Segundos = Segundos + 1
             PasosEst = PasosEst + 1
             
         
    if PrimerMovimiento == "Agente":
        if (ColAgent - ColEst < 0 and FilAgent - FilEst > 0) or (ColAgent - ColEst < 0 and FilAgent - FilEst < 0) or (ColAgent - ColEst < 0 and FilAgent - FilEst == 0) :
            ColAgent = ColAgent + 1 
            
            
        if (ColAgent - ColEst > 0 and FilAgent - FilEst < 0) or (ColAgent - ColEst > 0 and FilAgent - FilEst > 0) or (ColAgent - ColEst > 0 and FilAgent - FilEst == 0) :
            ColAgent = ColAgent - 1
             
            
        if (FilAgent - FilEst > 0 and ColAgent - ColEst > 0) or (FilAgent - FilEst > 0 and ColAgent - ColEst < 0) or (FilAgent - FilEst > 0 and ColAgent - ColEst == 0):
            FilAgent = FilAgent - 1
            
             
        if (FilAgent - FilEst < 0 and ColAgent - ColEst < 0) or (FilAgent - FilEst < 0 and ColAgent - ColEst > 0) or (FilAgent - FilEst < 0 and ColAgent - ColEst == 0):
            FilAgent = FilAgent + 1
        
        PasosAgent = PasosAgent + 1
        
    Segundos = Segundos + 1      
    
    if Segundos == 70 :
     pos(22,1) ; print("Juego Finalizado, El Agente logró escapar")
     break
    elif (FilAgent == FilEst) and (ColAgent == ColEst):
     pos(22,1) ; print("Juego Finalizado, el Agente atrapó al Estafador.")
     break
 
  
pos(23,1) ; print("La persecución duró:  ", Segundos, "Segundos")
pos(24,1) ; print("El Estafador dio ", PasosEst, "pasos")
pos(25,1) ; print("El Agente dio ", PasosAgent, "pasos")
input("")

#Codigo no funcional, no implementa tablero, ejecucion termina automaticamente si posibilidad
# de detenerlo en cada movimiento . Pendiente revision de codigo