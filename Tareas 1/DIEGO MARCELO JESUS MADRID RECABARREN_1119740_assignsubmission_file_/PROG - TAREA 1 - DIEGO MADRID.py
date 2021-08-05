# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:58:36 2021

@author: diegu
"""
# Integrantes: Diego Madrid Recabarren

import random
import colorama
colorama.init(autoreset = True)

FilaE = random.randint(1,20)
ColumnaE = random.randint(1,20)
FilaA = random.randint(1,20)
ColumnaA = random.randint(1,20)
while abs(FilaE - FilaA) < 3 :
    FilaA = random.randint(1,20)
while abs(ColumnaE - ColumnaA)<3 :
    ColumnaA = random.randint(1,20)
Tiempo = 0
Sw = 1
PasosE = 0
PasosA = 0

while Sw == 1 :
    Selección = random.randint(1,2)
    if Selección == 1 :
        print(colorama.Fore.RED + "Se mueve el estafador")
        PasosE = PasosE + 1
        if ColumnaA < ColumnaE :
            ColumnaE = ColumnaE + 1
        else :
            if ColumnaA > ColumnaE :
                ColumnaE = ColumnaE - 1
        if FilaA < FilaE :
            FilaE = FilaE + 1
        else :
            if FilaA > FilaE :
                FilaE = FilaE - 1
        if FilaE < 1 :
            FilaE = random.randint(1,20)
            ColumnaE = random.randint(1,20)
        if FilaE > 20 :
            FilaE = random.randint(1,20)
            ColumnaE = random.randint(1,20)
        if ColumnaE < 1 :
            FilaE = random.randint(1,20)
            ColumnaE = random.randint(1,20)
        if ColumnaE > 20 :
            FileE = random.randint(1,20)
            ColumnaE = random.randint(1,20)
    else :
        print(colorama.Fore.BLUE + "Se mueve el agente")
        PasosA = PasosA + 1
        if ColumnaA < ColumnaE :
            ColumnaA = ColumnaA + 1
        else :
            if ColumnaA > ColumnaE :
                ColumnaA = ColumnaA - 1
        if FilaA < FilaE :
            FilaA = FilaA + 1
        else :
            if FilaA > FilaE :
                FilaA = FilaA - 1
    print("El estafador está en (", FilaE, ",", ColumnaE, ")")
    print("El agente está en (", FilaA, ",", ColumnaA, ")")
    input()
    Tiempo = Tiempo + 1
    if Tiempo == 70 :
        Sw = 0
        Estafador = "Escapó"
    if ColumnaA == ColumnaE and FilaA == FilaE :
        Sw = 0
        Estafador = "Atrapado"

if Estafador == "Escapó" :
    print("El estafador logró escapar")
if Estafador == "Atrapado" :
    print("El estafador ha sido capturado")
print("La persecución duró ", Tiempo, " segundos")
print("El estafador dió ", PasosE, " pasos")
print("El agente dió ", PasosA, " pasos")
input()
        
        

# No usa tablero, despliega movimientos como mensajes, codigo funcional
# NOTA: PENDIENTE