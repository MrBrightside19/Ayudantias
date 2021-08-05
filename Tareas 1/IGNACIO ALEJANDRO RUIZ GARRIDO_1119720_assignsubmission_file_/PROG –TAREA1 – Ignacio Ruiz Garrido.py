"""
Primera Tarea Programación lab.
Atrápame si puedes.

Ignacio Ruiz Garrido
Nicolás Castillo Prado
Matias Carvajal Depassier
Marcos Caviedes Peralta

"""

import time
import random
import os
os.system('color')
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def Mostrar_Mapa (FEst2,CEst2,FAge2, CAge2,largo):
    FEst2 -= 1
    CEst2 -= 1                                                      # Ajuste por diferencia en manejo de rangos (números)
    FAge2 -= 1                                                      # entre nosotros y python..... ahora que lo pienso esto lo pudimos solucionar de como 7 formas más "correctas". pero bueno ya está.
    CAge2 -= 1
    print("   ", end="")
    for i in range(largo):                                          # Enumeración superior de matriz
        print(" {:02d} ".format(i + 1), end="")
    print("")
    for i in range(largo):                                          # Dibujo de matriz
        print("{:02d}".format(i + 1), end="")                       # Enumeración lateral izq de matriz
        for j in range(largo):                                      # 4 posibilidades:Casilla Agente y Estafador juntos, Cas.Est, Cas.Age, Cas. vacia.
            if FEst2 == i and FAge2 == i and CAge2 == j and CEst2 == j:
                print("|" + "\033[4;31;42m" + "E" + "\033[0;m" +"\033[;42m"+ "_" + "\033[4;34;42m" + "A" + "\033[0;m", end="")
            elif FEst2 == i and CEst2 == j:
                print("|" + "\033[;31m" + "_E_" + "\033[0;m", end="")
            elif FAge2 == i and CAge2 == j:
                print("|" + "\033[;34m" + "_A_" + "\033[0;m", end="")
            else:
                print("|___", end='')
        print("|")

                                                                    #Comienzo del Main

FEst = random.randint(1, 20)
CEst = random.randint(1, 20)
FAge = random.randint(1, 20)
CAge = random.randint(1, 20)
while (abs(FEst - FAge) <= 2) and (abs(CEst - CAge) <= 2):          # Checkeo cercanía, si Est está muy cerca de Age
    FEst = random.randint(1, 20)
    CEst = random.randint(1, 20)
Tiempo = 0
PasosEst = 0
PasosAge = 0
Juega = 0
bandera = 1

while (Tiempo < 70) and ((FEst != FAge) or (CEst != CAge)):         # Comienzo de la persecución
    Juega = random.randint(1, 2)                                    # Definimos quien juega : 1=Agente, 2=Estafador
    Mostrar_Mapa(FEst, CEst, FAge, CAge, 20)                        # 1°
    time.sleep(0.2)
    clearConsole()

    if Juega == 1:                                                  # Distinción de como se mueve cada protagonista, ya que tienen distintos roles.
        PasosAge = PasosAge + 1

        if (FEst < FAge) and (CEst == CAge):
            FAge = FAge - 1
        if (FEst == FAge) and CEst < CAge:
            CAge = CAge - 1
        if FEst > FAge and CEst == CAge:
            FAge = FAge + 1
        if FEst == FAge and CEst > CAge:
            CAge = CAge + 1
        if FEst < FAge and CEst < CAge:
            FAge = FAge - 1
            CAge = CAge - 1
        if FEst > FAge and CEst > CAge:
            FAge = FAge + 1
            CAge = CAge + 1
        if FEst > FAge and CEst < CAge:
            FAge = FAge + 1
            CAge = CAge - 1
        if FEst < FAge and CEst > CAge:
            FAge = FAge - 1
            CAge = CAge + 1

    if Juega == 2:
        PasosEst = PasosEst + 1

        if FEst < FAge and CEst == CAge:
            FEst = FEst - 1
        if FEst == FAge and CEst < CAge:
            CEst = CEst - 1
        if FEst > FAge and CEst == CAge:
            FEst = FEst + 1
        if FEst == FAge and CEst > CAge:
            CEst = CEst + 1
        if FEst < FAge and CEst < CAge:
            FEst = FEst - 1
            CEst = CEst - 1
        if FEst > FAge and CEst > CAge:
            FEst = FEst + 1
            CEst = CEst + 1
        if FEst > FAge and CEst < CAge:
            FEst = FEst + 1
            CEst = CEst - 1
        if FEst < FAge and CEst > CAge:
            FEst = FEst - 1
            CEst = CEst + 1
        if FEst > 20 or FEst < 1 or CEst > 20 or CEst < 1:
            FEst = random.randint(1, 20)
            CEst = random.randint(1, 20)

    Tiempo = Tiempo + 1

    #print("Tiempo transcurrido:", Tiempo, "segundos")
    #print("Jugador", Juega)
    #print("Esta es la posición del Agente Fila ", FAge, "Columna", CAge, "dentro del while")
    #print("Esta es la posición del Estafador Fila ", FEst, "Columna", CEst, "dentro del while")

    Mostrar_Mapa(FEst, CEst, FAge, CAge, 20)                        # 1°
    input("")
    clearConsole()

if(FEst == FAge) and (CEst == CAge):
    print("EL ESTAFADOR HA SIDO ATRAPADO")
elif Tiempo == 70:
    print("Huichipirichi, EL ESTAFADOR LOGRO ESCAPAR")
else:
    print(" no se como llegaste aqui, hay algo malo. ")

print("El Estafador ha dado", PasosEst, "pasos.")
print("El Agente ha dado", PasosAge, "pasos.")
print("Tiempo Transcurrido:", Tiempo, "segundos")

#time.sleep(2)
input()


# 1° Se muestra el mapa del tablero dos veces, 1ra vez para poder ver el primer paso y la 2da vez para poder ver cuando atrapan al Estafador (si es que ocurre)

# Codigo funcional, no muestra estado de los personajes durante ejecucion
# NOTA: 100