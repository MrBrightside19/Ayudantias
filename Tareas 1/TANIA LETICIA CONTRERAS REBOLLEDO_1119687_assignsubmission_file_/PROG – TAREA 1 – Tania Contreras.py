# Tarea 1 Laboratorio: Atrapame Si Puedes
# Matías Castillo | Tania Contreras | Franco Hernández | Agustín Uribe

import os; import random; import time; import win32ui
from colorama import init, Fore, Back, Style
os.system('cls'); init(autoreset=True)

# Modulos
def pos(x,y):
    print("\033[" + str(y) + ";" + str(x) + "H", sep="", end="")
    return None

def MsgBox(Mensaje="", Titulo="", Tipo=0):
    return win32ui.MessageBox(Mensaje,Titulo,Tipo)

def mov(x1, x2, y1, y2, num, num2):
    if y1 == y2: #Horizontal
        if x1 > x2:
            x1 += num
        else:
            x1 -= num
    elif x1 == x2:  #Vertical
        if y1 > y2:
            y1 += num2
        else:
            y1 -= num2
    elif y1 > y2:   #Diagonal abajo
        if x1 > x2: #Derecha
            x1 += num
            y1 += num2
        else:       #Izquierda
            x1 -= num
            y1 += num2
    elif y1 < y2:   #Diagonal arriba
        if x1 > x2: #Derecha
            x1 += num
            y1 -= num2
        else:       #Izquierda
            x1 -= num
            y1 -= num2
    return x1, y1

# Se construye el escenario
x = 1; y = 1; n = 0
while y <= 41: # Número de filas
    pos(x, y); print("F{:02}".format(n))
    y += 2
    n += 1

x = 1; y = 1; n = 0
while x <= 81: # Número de columnas
    pos(x, y); print("C{:02}".format(n))
    x += 4
    n += 1

x = 6; y = 3
while x <= 86 and y <= 41: # Puntos
    pos(x, y); print("•") 
    x += 4
    if x == 86:
        x = 6
        y += 2

pos(1,1); print("000") # No me gustaba que la posición 1,1 quedara con un C01, así que lo dejé 000

# Se determina la posición inicial de los personajes
agentex = random.randrange(5,81,4); agentey = random.randrange(3,41,2)
estafadorx = random.randrange(5,81,4); estafadory = random.randrange(3,41,2)

# Reposiciona al estafador si es que está en las mismas coordenadas que el agente
while estafadorx == agentex and estafadory == agentey:
    estafadorx = random.randrange(5,81,4)
    estafadory = random.randrange(3,41,2)

# Reposiciona al estafador si es que está en una de las 2 casillas siguientes al agente
while abs(estafadorx - agentex) < 12 and abs(estafadory - agentey) < 5:
    estafadorx = random.randrange(5,81,4)
    estafadory = random.randrange(3,41,2)

# Se muestra posición inicial de los personajes en pantalla
pos(agentex, agentey);print(Back.GREEN + Fore.WHITE + Style.BRIGHT + " A ")
pos(estafadorx, estafadory);print(Back.RED + Fore.WHITE + Style.BRIGHT + " E ")

pos(1,43);print("Atrapame Si Puedes")
pos(1,45);input("Presione Enter para iniciar el programa.")

# Se inicia el programa
sec = -1; turno = 0; sw = 1
while sw == 1:
    turno = random.randint(0,1) #Determina el turno, 0  = estafador, 1 = agente
    ex = estafadorx; ey = estafadory #Posiciones anteriores del estafador
    ax = agentex; ay = agentey #Posiciones anteriores del agente
    
    if turno == 0:
        estafadorx, estafadory = mov(estafadorx, agentex, estafadory, agentey, 4, 2)
        
        #Vuelve a posicionar en el mapa al estafador cuando este toca los bordes
        if estafadorx < 5 or estafadorx > 82:
                estafadorx = random.randrange(5,81,4)
                estafadory = random.randrange(3,41,2)
        if estafadory < 3 or estafadory > 42:
                estafadorx = random.randrange(5,81,4)
                estafadory = random.randrange(3,41,2)
    if turno == 1:
        agentex, agentey = mov(agentex, estafadorx, agentey, estafadory, -4, -2)
    
    time.sleep(1)
    sec += 1
    pos(1, 47); print(f"Segundos transcurridos: {sec}")
    pos(ex,ey); print(" • ") # Para que no quede un rastro de "A" o "E"
    pos(ax,ay); print(" • ") # Lo mismo que arriba
    pos(estafadorx, estafadory);print(Back.RED + Fore.WHITE + Style.BRIGHT + " E ")
    pos(agentex, agentey);print(Back.GREEN + Fore.WHITE + Style.BRIGHT + " A ")
    
    if turno == 0:
        pos(1, 48);print(Back.RED + Fore.WHITE + Style.BRIGHT + "Turno de: Estafador")
    else:
        pos(1, 48);print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "Turno de:  Agente  ")
    
    if sec == 70 or (agentex == estafadorx and agentey == estafadory):
        sw = 0

# Resultado
if agentex == estafadorx and agentey == estafadory:
    pos(90, 11);MsgBox("El agente logró atrapar al estafador.", "Te atrapé", 0 + 64)
elif sec == 70:
    pos(estafadorx, estafadory); print(" • ")
    pos(90, 11);MsgBox("El estafador logró escapar.", "No puedes atraparme", 0 + 32)

pos(1, 49);input()


# Biblioteca time sleep mal empleada, ejecucion de los movimientos hacia abajo, no se refresca tablero
# Nota: Pendiente
