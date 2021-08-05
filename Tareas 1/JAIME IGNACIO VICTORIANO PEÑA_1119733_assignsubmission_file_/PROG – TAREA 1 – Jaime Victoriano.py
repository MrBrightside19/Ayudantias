#Integrantes:
#            Lucas Matías Ossandón Geve
#            Jaime Ignacio Victoriano Peña
#            Juan Daniel Vilugrón Jofré
#            Joaquín Andres Hidalgo Paredes 
import os
os.system("cls")
import colorama
from colorama import init
import random
init(autoreset=True)

def pos(x,y):# --> pos (x,y) == pos (columna,fila)
    print("\033[" + str(x) + ";" +str(y) + "H", sep="",end="")
    return None

##GENERACION##
estafadorX = random.randint(1,20)
estafadorY = random.randint(1,20)

agenteX = random.randint(1,20)
agenteY = random.randint(1,20)

seg = 0 ; PasosEstafador = 0 ; PasosAgente = 0 ; sw = 0

while (estafadorX == agenteX and estafadorY == agenteY) or (estafadorX - 2 <= agenteX and estafadorY - 2 <= agenteY and estafadorX + 2 >= agenteX and estafadorY + 2 >= agenteY):

    estafadorX = random.randint(1,20)
    estafadorY = random.randint(1,20)

    agenteX = random.randint(1,20)
    agenteY = random.randint(1,20)



#  Empieza la caza

while seg <= 70 and sw == 0:
    os.system("cls")

    pos(1,22);print(colorama.Fore.GREEN + "1")
    pos(1,42);print(colorama.Fore.GREEN + "2")

    contador = 4 
    for j in range(1,21):
        auxiliar = str(contador)
        if j == 20:
            j = 0
        if j >= 10:
            w = str(j-10)
            pos(2,contador);print(colorama.Fore.GREEN + w)
            contador += 1
        elif contador % 2 == 0:
                z = str (j)
                pos(2,contador);print(colorama.Fore.GREEN + z)
                contador += 1
        contador += 1

    columna = 3
    fila = 4
    while fila <= 42:
        pos(columna,fila);print(colorama.Fore.WHITE + "*")
        columna += 1
        if columna == 23:
            fila += 2
            columna = 3

    posicion = 1
    for i in range(3,23):
        if i >= 12:
            x = str(i-2)
            pos(i,1);print(colorama.Fore.GREEN + x)
        else:
            auxi = str(posicion)
            pos(i,2);print(colorama.Fore.GREEN + auxi)
        posicion += 1

    pos(estafadorY+2,(estafadorX+1)*2);print(colorama.Back.RED + colorama.Fore.WHITE + "E")
    pos(agenteY+2,(agenteX+1)*2);print(colorama.Back.YELLOW + colorama.Fore.WHITE + "A")
    print(colorama.Back.RESET + colorama.Fore.RESET + "")

    if agenteX == estafadorX and agenteY == estafadorY:
        sw = 1
        pos(agenteY+2,(agenteX+1)*2);print(colorama.Fore.LIGHTMAGENTA_EX + "X")

    pos(25,1);print("Tiempo          :",seg)
    pos(26,1);print("Pasos Estafador :",PasosEstafador)
    pos(27,1);print("Pasos Agentes   :",PasosAgente)
    pos(28,1);print("Pos Estafador   :",str(int(estafadorX)),",",str(int(estafadorY)))
    pos(29,1);print("Pos Agente      :",str(int(agenteX)),",",str(int(agenteY)))

    input()

    pickrate = random.randint(0,1)  #0=ESTAFADOR | 1=AGENTE

    if pickrate == 0:               #MOVIMIENTO ESTAFADOR

        PasosEstafador += 1

        if estafadorX < agenteX:
            estafadorX -= 1

        if estafadorX > agenteX:
            estafadorX += 1

        if estafadorY < agenteY:
            estafadorY -= 1

        if estafadorY > agenteY:
            estafadorY += 1

    if pickrate == 1:              #MOVIMIENTO AGENTE

        PasosAgente += 1

        if estafadorX < agenteX:
            agenteX -= 1

        if estafadorX > agenteX:
            agenteX += 1

        if agenteY > estafadorY:
            agenteY -= 1

        if agenteY < estafadorY:
            agenteY += 1
    
#Si sale del sitio
    while estafadorX < 1 or estafadorX > 20:
        estafadorX = random.randint(1,20)
        estafadorY = random.randint(1,20)

    while estafadorY < 1 or estafadorY > 20:
        estafadorX = random.randint(1,20)
        estafadorY = random.randint(1,20)


    if agenteX > 20 :
        agenteX = 1 
    elif agenteX < 1 : 
        agenteX = 20
    elif agenteY > 20: 
        agenteY = 1
    elif agenteY < 1 :
        agenteY = 20

    seg += 1
    

#Final
if seg >= 70 :
    pos(25,43);print("El estafador logró escapar")
if estafadorX == agenteX and estafadorY == agenteY :
    pos(25,43);print("El estafador ha sido capturado")
pos(26,43);print("La persecusion duro: ", seg-1 , "s")
pos(27,43);print("El estafador dio ", PasosEstafador-1 , " pasos, y el agente dio ", PasosAgente , "pasos ")

input()

# Cumplen con los requisitos, codigo funcional. Nota 100