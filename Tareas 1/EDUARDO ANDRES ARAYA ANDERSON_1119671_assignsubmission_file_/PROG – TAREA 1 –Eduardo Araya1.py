# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 21:17:01 2021
@author: Eduardo Andres Araya Anderson
"""

import os
import time
os.system('cls')

from random import randint as azar
from colorama import init, Fore, Back
init()

tiempo = 0 
tiempopasos=0
counter = 0
estafador_col = azar(1,20)
estafador_fil = azar(1,20)
agente_col = azar(1,20)
agente_fil = azar(1,20)
pasos_agente=0
pasosagente=0
pasos_estafador=0 

#-> Que haya una distancia de 2 pasos entre Agente y Estafador
while estafador_col <= (agente_col + 2) and estafador_col >= (agente_col - 2) or \
    estafador_fil <= (agente_fil + 2) and estafador_fil >= (agente_fil - 2):
    
    estafador_col = azar(1,20)
    estafador_fil = azar(1,20)
    

def pos(x,y):
    
  return "\033[" + str(x) + ";" + str(y) + "H"

 #-> Mide el Tiempo de Proceso del Programa en 70sgdos
timeout = int(time.time() + 70)

for Contador in range(timeout):
  
 #-> Aqui incia con el Movimiento del Agente y el Estafador  
   print(pos(estafador_col,estafador_fil) + "E", end='')
   print(pos(agente_col,agente_fil) +"A",end='')
   input()
  

 #-> Proceso de condiciones tanto para el Agente y Estafador
   if agente_col>estafador_col or agente_fil>estafador_fil:  
          agente_fil=agente_fil-1
          agente_col=agente_col-1 
          
          pasos_agente=pasos_agente+1

          estafador_col = azar(1,20)
          estafador_fil = azar(1,20)

          pasos_estafador=pasos_estafador+1
          
   if agente_col<estafador_col or agente_fil<estafador_fil:
          agente_fil=agente_fil+1
          agente_col=agente_col+1
          
          pasos_agente=pasos_agente+1

          estafador_col = azar(1,20)
          estafador_fil = azar(1,20)
          
          pasos_estafador=pasos_estafador+1

   if agente_col==estafador_col and agente_fil>estafador_fil :
          agente_fil=agente_fil-1
                    
          pasos_agente=pasos_agente+1

          estafador_col = azar(1,20)
          estafador_fil = azar(1,20)
          pasos_estafador=pasos_estafador+1

         
   if agente_col==estafador_col and agente_fil<estafador_fil :
          agente_fil=agente_fil+1

          pasos_agente=pasos_agente+1
          
          pasos_estafador=pasos_estafador+1      
   
   if agente_fil==estafador_fil and agente_col>estafador_col :
          agente_col=agente_col-1
          
          pasos_agente=pasos_agente+1

          estafador_col = azar(1,20)
          estafador_fil = azar(1,20) 
          pasos_estafador=pasos_estafador+1     
   
   if agente_fil==estafador_fil and agente_col<estafador_col :
          agente_col=agente_col+1

          pasos_agente=pasos_agente+1

          estafador_col = azar(1,20)
          estafador_fil = azar(1,20)      
          pasos_estafador=pasos_estafador+1

   if estafador_col>=20 or estafador_fil>=20:
          estafador_col = azar(1,20)
          estafador_fil = azar(1,20)
          pasos_estafador=pasos_estafador+1  
   
   if agente_col>=20:

           agente_col=1
           pasos_agente=pasos_agente+1
           
   elif  agente_fil>=20:
            agente_fil=1
            pasos_agente=pasos_agente+1

 #-> Cuando el Estafador es Capturado
   if agente_col == estafador_col and agente_fil == estafador_fil:
         print(pos(36,59)," El estafador ha sido capturado")
         break       
   else:   
   #-> Estafador Logra Escapar        
       tiempo=tiempo+1   
       if tiempo==70:
         print(pos(36,59), "El estafador logro escapar", "tiempo total",tiempo,"segundos" )
         break
   
   
   pasosagente=pasos_agente
   pasosestafador=pasos_estafador

   tiempopaso=float(pasosagente+pasosestafador)*60/60

   os.system('cls')
   print(pos(31,59),"tiempo transcurrido", format(tiempopaso),"segundos")
   print(pos(33,61),"Pasos del Agente", pasosagente)
   print(pos(34,62),"Pasos del Estafador", pasosestafador)


# Tiempo mal implementado, tablero no visualizado, interfaz desordenada,
# no se detiene en 70 seg 
#NOTA: PENDIENTE