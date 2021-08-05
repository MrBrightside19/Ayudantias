# -*- coding: utf-8 -*-
# Nathaly Cunich
# Alexander Cuellar
# Jetsabel Correa


#FEst y CEst son las variables para el estafador <- ContPasosE
#FAge y CAge son las variables para el agente <- ContPasosA
#Mov es la variable para la direccion
#TU JUGARAS COMO EL AGENTE
import os
import random
import colorama
colorama.init(autoreset = True)
Tiempo = 0 
ContPasosE = 0
ContPasosA = 0

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None
###################### P A R T E  I N I C I A L ######################


FEst = random.randint(1, 20); CEst = random.randint(1, 20)
FAge = random.randint(1, 20); CAge = random.randint(1, 20)
while  abs(FEst - FAge) <= 2  and  abs(CEst - CAge) <= 2  : 
	FEst  = FEst + 1  ; CEst  = CEst + 1
     
Sw = 0



while Sw == 0:
    while (FEst != FAge) and (CEst != CAge):
        os.system("cls")
        for Fila in range(1, 20):
            for Columna in range(1, 20):
                if (Fila == FEst) and (Columna == CEst):
                    print(colorama.Back. BLUE + " E ", end="")
                else:
                    if (Fila == FAge) and (Columna == CAge):
                        print(colorama.Back.RED + " A ", end="")
                    else:
                        print(" * ", end="")
            print(" ")
        print(" ")
        FEst = random.randint(1, 20); CEst = random.randint(1, 20)
        FAge = random.randint(1, 20); CAge = random.randint(1, 20)
        while  abs(FEst - FAge) <= 2  and  abs(CEst - CAge) <= 2  : 
	        FEst  = FEst + 1  ; CEst  = CEst + 1
            
        # pos(22, 1); input("Presione ENTER para continuar: ")
        pos(24, 1); print("Estafador (", FEst, ", ", CEst, ")"        "Agente (", FAge, ", ", CAge, ")")
        pos(25, 1); print("Tiempo transcurrido = ", Tiempo, "segundos.")
        pos(26, 1); print("El estafador dio ", ContPasosE," pasos.")
        pos(27, 1); print("El agente dio", ContPasosA, "pasos.")
        
                
        if (FEst == FAge) and (CEst == CAge):
            pos(28, 1); print("El agente ha atrapado al estafador. PERDISTE")
            Sw == 1
    
        if Tiempo == 70:
            print("Se acabo el tiempo, el estafador escapo")
        input()

##################### M O V I M I E N T O  E S T A F A D O R #####################    
    
        Mov = random.randint(0, 3)
    
        if Mov == 0:
            if FEst > 1:
                FEst = FEst - 1
                Tiempo = Tiempo + 1
                ContPasosE = ContPasosE + 1
        
        print(end="")
        
    
        if Mov == 1:
            if CEst < 20:
                CEst = CEst + 1
                Tiempo = Tiempo + 1
                ContPasosE = ContPasosE + 1
        
        print(end="")
        
    
        if Mov == 2:
            if FEst < 20:
                FEst = FEst + 1
                Tiempo = Tiempo + 1
                ContPasosE = ContPasosE + 1
        
        print(end="")
        
    
        if Mov == 3:
            if CEst > 1:
                FEst = FEst - 1
                Tiempo = Tiempo + 1
                ContPasosE = ContPasosE + 1
        
        print(end="")
        
    
        if FEst > 20:
            FEst = random.randint(1, 20)
        else:
            if FEst < 1:
                FEst = random.randint(1, 20)
        print(end="")
        
        if CEst > 20:
            CEst = random.randint(1, 20)
        else:
            if CEst < 1:
                CEst = random.randint(1, 20)
        print(end="")
        
##################### M O V I M I E N T O  A G E N T E #####################

        if FEst == FAge:
            if Mov == 0:
                if FEst < FAge:
                    FAge = FAge - 1
                else:
                    FAge = FAge + 1
                Tiempo = Tiempo + 1
                ContPasosA = ContPasosA + 1
            
            print(end="")
            
        
            if Mov == 1:
                if CEst > CAge:
                    CAge = CAge + 1
                else:
                    CAge = CAge - 1
                Tiempo = Tiempo + 1
                ContPasosA = ContPasosA + 1
            
            print(end="")
            
        
            if Mov == 2:
                if FEst > FAge:
                    FAge = FAge + 1
                else:
                    FAge = FAge - 1
                Tiempo = Tiempo + 1
                ContPasosA = ContPasosA + 1
            
            print(end="")
            
        
            if Mov == 3:
                if CEst < CAge:
                    CAge = CAge - 1
                else:
                    CAge = CAge + 1
                Tiempo = Tiempo + 1
                ContPasosA = ContPasosA + 1 
            
            print(end="")
            
        
        if FAge > 20:
            FAge = random.randint(1, 20)
        print(end="")
        
        if CAge > 20:
            CAge = random.randint(1, 20)
            print(end="")
        
            if CEst == CAge:
                if Mov == 0:
                    FAge = FAge - 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
                
        
                if Mov == 1:
                    if FEst > FAge:
                        FAge = FAge + 1
                    else:
                        FAge = FAge - 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
                
        
                if Mov == 2:
                    CAge = CAge + 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
                
        
                if Mov == 3:
                    if FEst < FAge:
                        FAge = FAge - 1
                    else:
                        FAge = FAge + 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
                
        
            if (FEst != FAge) and (CEst != CAge):
                if Mov == 0:
                    if CEst > CAge:
                        CAge = CAge + 1
                    else:
                        CAge = CAge - 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
                
        
                if Mov == 1:
                    if FEst > FAge:
                        FAge = FAge + 1
                    else:
                        FAge = FAge - 1
                    Tiempo = Tiempo + 1
                    ContPasosA = ContPasosA + 1
                
                print(end="")
        

# NO VOLVER A UTILIZAR TIME.SLEEP
# CON UN INPUT AL FINAL BASTA

#No cumple con lo solicitado, ambos personajes aparecen al azar, queda atrapado
# en bucles Nota: 55-70