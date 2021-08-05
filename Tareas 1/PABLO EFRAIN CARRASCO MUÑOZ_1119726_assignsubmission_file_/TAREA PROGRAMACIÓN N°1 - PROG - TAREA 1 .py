# TAREA 1 PROGRAMACIÓN-Laboratorio   
# integrantes: Gonzalo Vargas Galleguillos
#              Pablo Carrasco Muñoz
#              Gerson Escalante González
#              Patricio Acevedo Terraza

import random
import os 
import colorama




os.system("cls")

psEstaf = 0
psAgent = 0
seg = 0
sw = 0
 
colorA = colorama.Fore.BLUE
colorE = colorama.Fore.RED
color = colorama.Fore.WHITE


def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None



agenteFil = random.randint(1, 20) 
agenteCol = random.randint(1, 20)
estafadorFil = random.randint(1, 20) 
estafadorCol = random.randint(1, 20) 

while abs(agenteFil - estafadorFil) < 2 and abs(agenteCol - estafadorCol) < 2 :
    agenteFil = random.randint(1, 20); agenteCol = random.randint(1, 20)

while sw == 0 :
    input()
    os.system("cls")

    mover = random.randint(0, 1)

    if mover == 0 :
        psAgent += 1
        if estafadorCol > agenteCol and estafadorFil > agenteFil  :
            agenteCol += 1
            agenteFil += 1
        elif estafadorCol > agenteCol and estafadorFil < agenteFil  :
            agenteCol += 1
            agenteFil -= 1
        elif estafadorCol < agenteCol and estafadorFil < agenteFil  :
            agenteCol -= 1
            agenteFil -= 1
        elif estafadorCol < agenteCol and estafadorFil > agenteFil  :
            agenteCol -= 1
            agenteFil += 1
        elif estafadorFil > agenteFil and estafadorCol > agenteCol :
            agenteFil += 1
            agenteCol += 1
        elif estafadorFil < agenteFil and estafadorCol < agenteCol :
            agenteFil -= 1
            agenteCol -= 1
        elif estafadorFil < agenteFil and estafadorCol > agenteCol :
            agenteFil -= 1
            agenteCol += 1
        if estafadorCol > agenteCol  :
            agenteCol += 1
        else :
            if estafadorCol < agenteCol :
                agenteCol -= 1
            else :
                if estafadorFil > agenteFil :
                    agenteFil += 1
                else :
                    if estafadorFil < agenteFil :
                        agenteFil -= 1                   
               

    if mover == 1 :
        psEstaf += 1
        if estafadorCol > agenteCol and estafadorFil > agenteFil :
            estafadorCol += 1
            estafadorFil += 1
        elif estafadorCol > agenteCol and estafadorFil < agenteFil :
            estafadorCol += 1
            estafadorFil -= 1
        elif estafadorCol < agenteCol and estafadorFil < agenteFil :
            estafadorCol -= 1   
            estafadorFil -= 1
        elif estafadorCol < agenteCol and estafadorFil > agenteFil :
            estafadorCol -= 1
            estafadorFil += 1
        elif estafadorFil > agenteFil and estafadorCol > agenteCol :
            estafadorFil += 1
            estafadorCol += 1
        elif estafadorFil > agenteFil and estafadorCol < agenteCol :
            estafadorFil += 1
            estafadorCol -= 1
        elif estafadorFil < agenteFil and estafadorCol < agenteCol :
            estafadorFil -= 1
            estafadorCol -= 1
        elif estafadorFil < agenteFil and estafadorCol > agenteCol :
            estafadorFil -= 1
            estafadorCol += 1
        else :
            if estafadorCol > agenteCol  :
                estafadorCol += 1
                           
            else :
                if estafadorCol < agenteCol  :
                    estafadorCol -= 1   
                                    
                else :
                    if estafadorFil > agenteFil :
                        estafadorFil += 1
                                            
                    if estafadorFil < agenteFil :
                        estafadorFil -= 1
                                                
                                                
        
                    


    seg += 1
    

    
    
    if estafadorFil == agenteFil and estafadorCol == agenteCol :
        sw = 1

    if seg == 70 :
        sw = 1
     
    #mostrar en pantalla
    pos(estafadorFil, estafadorCol); print(colorE,"E")
    pos(agenteFil, agenteCol); print(colorA,"A")

    pos(24,1); print(color,"---------------------------------------------")
    pos(25,1); print(color,"Tiempo          :", seg, "segundos")
    pos(26,1); print(color,"Pasos Estafador :", psEstaf)
    pos(27,1); print(color,"Pasos Agente    :", psAgent)
    pos(28,1); print(color,"---------------------------------------------")
    
        
    if estafadorCol > 20 or estafadorFil > 20 :
        pos(29, 1); print("El estafador salió del mapa")
        estafadorFil = random.randint(1, 20); estafadorCol = random.randint(1, 20)
    elif estafadorCol < 1 or estafadorFil < 1 :
        pos(29, 1); print("El estafador salió del mapa")
        estafadorFil = random.randint(1, 20); estafadorCol = random.randint(1, 20) 

if sw == 1 :
    os.system("cls")
    pos(10,10); print("*****SE HA TERMINADO*****") 
    if estafadorFil == agenteFil and estafadorCol == agenteCol :
        pos(13,8); print("EL ESTAFADOR A SIDO CAPTURADO")
        pos(14,1); print(color,"---------------------------------------------")
        pos(15,1); print(color,"Tiempo          :", seg, "segundos")
        pos(16,1); print(color,"Pasos Estafador :", psEstaf)
        pos(17,1); print(color,"Pasos Agente    :", psAgent)
        pos(18,1); print(color,"---------------------------------------------")
    elif seg == 70 and estafadorFil != agenteFil and estafadorCol != agenteCol :
        pos(13,8); print("EL ESTAFADOR SE HA ESCAPADO")
        pos(14,1); print(color,"---------------------------------------------")
        pos(15,1); print(color,"Tiempo          :", seg, "segundos")
        pos(16,1); print(color,"Pasos Estafador :", psEstaf)
        pos(17,1); print(color,"Pasos Agente    :", psAgent)
        pos(18,1); print(color,"---------------------------------------------")

    input()
    
# Codigo completo, no se visualiza tablero, ubicacion de los personajes con problemas,
# se logran ubicar a menos de 2 cuadres de distancia,
# a menos que sea por el diseño del tablero
# ocurrio que inicio uno encima del otro
# Nota 80-90