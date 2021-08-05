"""
INTEGRANTES: Josthin Ahumada Barrera
             Kathalinna Cáceres Torres
             Nicolás Vásquez Donoso
PARALELO A

Cuando el PROTAGONISTA == 1 el estafador se deberá mover, si el PROTAGONISTA == 2, el agente se deberá mover.
Si pasan 70 segundos y el estafador no es atrapado, el programa finaliza.
Si dentro de los 70 segundos el agente atrapa al estafador, el programa finaliza por el "SW".            
Desde la fila 106 al 109 corresponde al espacio simulado en forma de cuadrado donde se mueve el estafador y el agente.       
"""
import random
import colorama
colorama.init(autoreset = True) 
import os

def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None

APASOS = 0
EPASOS = 0

SEG = 0
SW = 0

FilA = random.randint(1,20)
ColA = random.randint(1,20)

FilE = random.randint(1,20)
ColE = random.randint(1,20)

while abs(FilA - FilE) <= 2 and abs(ColA - ColE) <= 2:
    
    FilE = random.randint(1,20)
    ColE = random.randint(1,20)
    
while SEG < 70 and SW == 0:
    
    SEG = SEG + 1
    
    PROTAGONISTA = random.randint(1,2)
    
    if PROTAGONISTA == 1:
        EPASOS = EPASOS + 1
        if ColA < ColE:
            ColE = ColE + 1
            if ColE > 20:
                ColE = random.randint(1,20)
                FilE = random.randint(1,20)
        
        elif ColA > ColE:
            ColE = ColE - 1
            if ColE < 1:
                ColE = random.randint(1,20)
                FilE = random.randint(1,20)
        elif ColA == ColE:
            ColE = ColE
            
        if FilA < FilE:
            FilE = FilE + 1
            if FilE > 20:
                ColE = random.randint(1,20)
                FilE = random.randint(1,20)
                
        elif FilA > FilE:
            FilE = FilE - 1
            if FilE < 1:
                ColE = random.randint(1,20)
                FilE = random.randint(1,20)
        elif FilA == FilE:
            FilE = FilE
            
    if PROTAGONISTA == 2:
        APASOS = APASOS + 1
        if ColA < ColE:
            ColA = ColA + 1
            if ColA > 20:
                ColA = 1
                
        elif ColA > ColE:
            ColA = ColA - 1
            if ColA < 1:
                ColA = 20
                
        elif ColA == ColE:
            ColA = ColA
        
        if FilA < FilE:
            FilA = FilA + 1
            if FilA > 20:
                FilA = 1
                
        elif FilA > FilE:
            FilA = FilA - 1
            if FilA < 1:
                FilA = 20
                
        elif FilA == FilE:
            FilA == FilA
            
    for j in range(1,21) :
        for i in range(1,21) :
            print(colorama.Fore.YELLOW + " * ", end="")
        print("")
    
    if FilA == FilE and ColA == ColE:
        SW = 1
    
    pos(FilA,ColA); print(colorama.Back.GREEN + " A ")
    pos(FilE,ColE); print(colorama.Back.RED + " E ")
    input()
    
    os.system("cls")
    
pos(23,23)

if SW == 1:
    print(colorama.Back.YELLOW + "¡EL ESTAFADOR HA SIDO CAPTURADO!")

if SEG >= 70 :
    print(colorama.Back.YELLOW + "¡EL ESTAFADOR LOGRÓ ESCAPAR!")

print()
print("==============================================")
print(" - Tiempo de persecución:",SEG, "segundos")
print()
print(" - Pasos del Agente:",APASOS)
print()
print(" - Pasos del Estafador:",EPASOS)
print("==============================================")
print()
input("                    ...ENTER PARA CERRAR EL PROGRAMA... ")

# Codigo funcional, no muestra en patalla estado del proceso
# nota: 90-100

'''
POSIBLE COPIA CON:
FELIPE ALBERTO PUENTE COLLINAO
DANIEL ESTEBAN GARRIDO GONZALEZ
NATALIA PAULINA ALVIAL DIAZ
'''