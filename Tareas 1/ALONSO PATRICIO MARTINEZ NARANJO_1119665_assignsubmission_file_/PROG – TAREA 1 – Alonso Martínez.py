
# Carlos Henriquez
# Alonso Martínez
# Jetro Vásquez
# Juan Vásquez







import os
os.system("cls")
import colorama
from colorama import init, Fore, Back, Style
init()
import random
random.randint(1,20)

XEstaf = random.randint(1,20) #Ubicar personajes
YEstaf = random.randint(1,20)
XPoli = random.randint(1,20)
YPoli = random.randint(1,20)
NumEsta = 0
NumPoli = 0
XMapMin = 1
YMapMin = 1
XMapMax = 20
YMapMax = 20
XNumP = XEstaf + 2 #Distancia
YNumP =  YEstaf + 2
XNumN = XEstaf - 2
YNumN =  YEstaf - 2

print("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
print(" 1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 2  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 3  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 4  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 5  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 6  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 7  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 8  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print(" 9  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("10  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("11  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("12  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("13  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("14  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("15  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("16  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("17  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("18  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("19  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")
print("20  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .")









while  XNumN <= XPoli <= XNumP and YNumN <= YPoli <= YNumP: 
    XPoli = random.randint(1,20)
    YPoli = random.randint(1,20)

#print("Posición del estafador:", XEstaf,",",YEstaf)
#print("Posición del policía:", XPoli,",",YPoli)

def pos(x,y): #Tablero en x,y
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None
   
 




#pos(22,1) #Indicador de posicion para agente y estafador
#print("Posición del estafador:", XEstaf,",",YEstaf)
#pos(23,1)
#print("Posición del policía:", XPoli,",",YPoli)


Juego = 0
Tiempo = 0
SwMov   = 0
MovEstaf = 0
MovPoli = 0

while Juego == 0: 
    pos(XEstaf+1,YEstaf*3+2); print(Back.RED, end="") #Posicion grafica de los personajes
    print("E") 
    pos(XPoli+1,YPoli*3+2); print(Back.CYAN, end="")
    print("A"); print(Back.BLACK, end="")
    input()
    Emov = random.randint(0,
                          1)
    SwMov = Emov
    pos(XEstaf+1,YEstaf*3+2)
    print(".") 
    pos(XPoli+1,YPoli*3+2)
    print(".")
   
    
    
    if Emov == 0 :
        if  XMapMin  <= XPoli < XEstaf and YMapMin <= YPoli < YEstaf:
            XEstaf = XEstaf + 1
            YEstaf = YEstaf +1 

        elif  XEstaf < XPoli <= XMapMax and  YEstaf < YPoli <= YMapMax:
            XEstaf = XEstaf - 1
            YEstaf = YEstaf - 1

        elif  XMapMin  <= XPoli < XEstaf and YEstaf < YPoli <= YMapMax:
            XEstaf = XEstaf + 1
            YEstaf = YEstaf - 1

        elif XEstaf < XPoli <= XMapMax and YMapMin <= YPoli < YEstaf:
            XEstaf = XEstaf - 1
            YEstaf = YEstaf + 1
            
        elif  XMapMin  <= XPoli < XEstaf:
             XEstaf = XEstaf + 1
          
            
        elif YMapMin <= YPoli < YEstaf :
            YEstaf = YEstaf + 1
          
        elif  XEstaf < XPoli <= XMapMax:
            XEstaf = XEstaf - 1      
                   
        else:
            YEstaf < YPoli <= YMapMax
            YEstaf = YEstaf - 1
         
            
    if Emov == 1 :
        if  XMapMin  <= XEstaf < XPoli and YMapMin <= YEstaf < YPoli:
           XPoli = XPoli - 1 #abajo a la izq
           YPoli = YPoli - 1 
           
        elif  XPoli < XEstaf <= XMapMax and  YPoli < YEstaf <= YMapMax:
           XPoli = XPoli + 1 #arriba- derecha
           YPoli = YPoli + 1
           
        elif  XMapMin  <= XEstaf < XPoli and YPoli < YEstaf <= YMapMax:
           XPoli = XPoli - 1 # arriba a la izq
           YPoli = YPoli + 1
           
        elif XPoli < XEstaf <= XMapMax and YMapMin <= YEstaf < YPoli:
           XPoli = XPoli + 1 # abajo a la derec
           YPoli = YPoli - 1
           
           
        elif  XMapMin  <= XEstaf < XPoli:
           XPoli = XPoli - 1 
           
           
           
        elif YMapMin <= YEstaf < YPoli:
           YPoli = YPoli - 1
           
           
        elif  XPoli < XEstaf <= XMapMax:
           XPoli = XPoli + 1    
           
           
        else: 
           YPoli < YEstaf <= YMapMax
           YPoli = YPoli + 1
           
        
     
    
    
    if Emov == 0:
        MovEstaf = MovEstaf + 1
        pos(26,22)
        print("El estafador a dado: ", MovEstaf, "pasos")
    elif Emov == 1:
        MovPoli = MovPoli + 1
        pos(27,22)
        print("El agente a dado: ", MovPoli, "pasos")
    
    
    
    if XEstaf == 0 or XEstaf == 21 or YEstaf == 0 or YEstaf == 21:
        XEstaf = random.randint(1,20)
        YEstaf = random.randint(1,20)    
    if XPoli == 21: 
        XPoli = 1       
    if XPoli == 0: 
        XPoli = 20 
    if YPoli == 0: 
        YPoli = 20      
    if YPoli == 21: 
        YPoli = 1               
            
    Tiempo = Tiempo + 1
    pos(24,22)
    print("Tiempo:", Tiempo, 'segundos')
    if Tiempo == 70 : 
        Juego = 1
        pos(29,22)
        print ("El estafador logro escapar")
    if XPoli == XEstaf and YPoli == YEstaf :
        Juego = 1
        pos(30,22)
        print('El agente logro atrapar al estafador.')
        
        
    if (XEstaf+1,YEstaf*3+2) == (XPoli+1,YPoli*3+2): 
        pos(XEstaf+1,YEstaf*3+2);print(Back.GREEN, end="");print("X");print(Back.BLACK, end="")
   
   

input()

# Ejecucion impecable, puntero inicial en fila 19, nada que entorpezca el desarrollo, 
# tablero desarrollado en base de 'prints' no es muy eficiente.
# NOTA?: 100
