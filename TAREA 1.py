import os
import colorama as cl
import time

from colorama.ansi import Back
cl.init(autoreset=False)
def pos(x,y):
    print("\033[" + str(x) + ";" + str(y) + "H", sep="", end="")
    return None
# print(cl.Back.GREEN)
os.system('cls')

fil = 1
col = 1
for fila in range(0,22):
    for columna in range(0,22):
        if fila == 0:
            if columna == 11:
                print(1, end=' ')
            elif columna == 21:
                print(2, end=' ')
            else:
                print(' ', end=' ')

        elif columna == 0:
            if fila == 11:
                print(' 1', end='')
            elif fila == 21:
                print(' 2',end='')
            else:
                print(' ', end=' ')

        if columna > 1 and fila == 1:
            print(col, end=' ')
            col += 1
            if col == 10:
                col = 0
        elif columna == 1 and fila > 1:
            print(fil, end=' ')
            fil += 1
            if fil == 10:
                fil = 0        
        elif columna != 0 and fila != 0:
            print('*', end=' ')
    print()
pos(5,5);print(cl.Back.CYAN+"A")
pos(7,13);print(cl.Back.CYAN+"B")
# input()
pos(23,1);input()
