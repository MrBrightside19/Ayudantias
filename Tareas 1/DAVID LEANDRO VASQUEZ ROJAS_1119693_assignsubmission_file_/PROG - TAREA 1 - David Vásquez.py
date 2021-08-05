#David Vásquez Rojas
#Profesor sé que era en grupo pero estuve sin internet por un poco más de \
#una semana y no pude coordinar con mi grupo. Disculpe los inconvenientes. 





import os
import sys
os.system("cls")
import random
from colorama import init, Fore, Back, Style
init()

#INICIO OCULTAR CURSOR PARPADEANTE
if os.name == 'nt': 
    import msvcrt 
    import ctypes 

    class _CursorInfo(ctypes.Structure): 
     _fields_ = [("size", ctypes.c_int), 
        ("visible", ctypes.c_byte)] 

def hide_cursor(): 
    if os.name == 'nt': 
     ci = _CursorInfo() 
     handle = ctypes.windll.kernel32.GetStdHandle(-11) 
     ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci)) 
     ci.visible = False 
     ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci)) 
    elif os.name == 'posix': 
     sys.stdout.write("\033[?25l") 
     sys.stdout.flush() 
hide_cursor()
#FIN OCULTAR CURSOR PARPADEANTE

def pos(x,y):
 print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
 return None


FilE = random.randrange(1,21)
ColE = random.randrange(1,21)
FilA = random.randrange(1,21)
ColA = random.randrange(1,21)
while abs(FilE - FilA) <= 2 and abs(ColE - ColA) <= 2 :
    FilA = random.randrange(1,21)
    ColA = random.randrange(1,21)  
Tiempo = 0
Sw = 0
ContE= 0
ContA = 0

print("                               1                             2")
print("    1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0")
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

while Sw == 0 :
    pos(FilE+2,ColE*3+2) ;print(Back.RED + Fore.WHITE + Style.BRIGHT, end = "E")
    pos(FilA+2,ColA*3+2) ;print(Back.BLUE + Fore.WHITE + Style.BRIGHT, end = "A")   
    Movim = random.randrange(0,2)
    print(Back.BLACK)
    input()
    pos(FilE+2,ColE*3+2) ;print(".")
    pos(FilA+2,ColA*3+2) ;print(".")
    Tiempo = Tiempo + 1
    pos(23,1) ; print ("Tiempo            :", Tiempo) 
    
    if Movim == 0 :
        ContE = ContE + 1
        
        if   (FilA < FilE) and (ColA < ColE) :
            FilE = FilE + 1
            ColE = ColE + 1
            
        elif (FilA > FilE) and (ColA < ColE) :
            FilE = FilE - 1
            ColE = ColE + 1
            
        elif (FilA < FilE) and (ColA > ColE) :
            FilE = FilE + 1
            ColE = ColE - 1
            
        elif (FilA > FilE) and (ColA > ColE) :
            FilE = FilE - 1
            ColE = ColE - 1
            
        elif (FilA == FilE) and (ColA > ColE) :
            ColE = ColE - 1
            
        elif (FilA == FilE) and (ColA < ColE) :
            ColE = ColE + 1
            
        elif (FilA > FilE) and (ColA == ColE) :
            FilE = FilE - 1
            
        elif (FilA < FilE) and (ColA == ColE) :
            FilE = FilE + 1
   
    
    if Movim == 1 :
        ContA = ContA + 1
        
        if (FilA < FilE) and (ColA < ColE) :
            FilA = FilA + 1 
            ColA = ColA + 1
            
        elif (FilA > FilE) and (ColA < ColE) :
            FilA = FilA - 1
            ColA = ColA + 1
            
        elif (FilA < FilE) and (ColA > ColE) :
            FilA = FilA + 1
            ColA = ColA - 1
            
        elif (FilA > FilE) and (ColA > ColE) :
            FilA = FilA - 1
            ColA = ColA - 1
            
        elif (FilA == FilE) and (ColA > ColE) :
            ColA = ColA - 1
            
        elif (FilA == FilE) and (ColA < ColE) :
            ColA = ColA + 1
            
        elif (FilA > FilE) and (ColA == ColE) :
            FilA = FilA - 1
            
        elif (FilA < FilE) and (ColA == ColE) :
            FilA = FilA + 1
            
    if (FilE < 1) or (FilE > 20) or (ColE < 1) or (ColE > 20) :
        FilE = random.randrange(1,21)
        ColE = random.randrange(1,21)
    
    pos(23,1) ; print ("Tiempo         : ", Tiempo , " segundos")
    pos(24,1) ; print ("Pasos estafador: ", ContE)
    pos(25,1) ; print ("Pasos agente   : ",ContA)
    
    if Tiempo == 70 :
        Sw = 1
        pos(27,1) ; print("El estafador logró escapar")
        pos(28,1) ; print("Presione Enter para finalizar...")
   
    if (FilA == FilE) and (ColA == ColE) :
        Sw = 1
        pos(27,1) ; print("El estafador fue atrapado")
        pos(28,1) ; print("Presione Enter para finalizar...")
        pos(FilA+2,ColA*3+2) ;print(Back.YELLOW + Fore.WHITE + Style.BRIGHT, end = "X")
input()


# Ejecucion funciona correctamente, codigo eficiente, cumple con los requisitos
# NOTA: 100