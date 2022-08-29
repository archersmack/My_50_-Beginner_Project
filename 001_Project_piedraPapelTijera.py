# El juego piedra, papel o tijera le pregunta al usuario que escoja una de las 3 opciones (piedra,
# papel o tijera) y se enfrenta con una de las 3 opciones que de forma aleatoria escoja "Serena" La computadora.
# Se jugara por rondas de 10 y luego se preguntara si desea seguir jugando o salir.

def menu_option():  # Funcion para mostrar menu de opciones
    print('''
    ------------------------------------------------------
    Escoje el número de alguna de las siguientes opciones:
        1. Piedra    2. Papel    3. Tijera
    ''', end = "Opcion elegida: ")

def convertirEnteroPCeleccion():
    if computer_option == 'PIEDRA':
        PC_option = 1
    elif computer_option == 'PAPEL':
        PC_option = 2
    elif computer_option == 'TIJERA':
        PC_option = 3
    return PC_option

########### Cuerpo del Algoritmo ##############

import random
import time

options = ['PIEDRA', 'PAPEL', 'TIJERA'] ## Lista con las 3 opciones
puntaje_PC = 0
puntaje_Human = 0

print('''
Bienvenido al clásico juego de piedra, papel y tijera.
------------------------------------------------------
Vamos a jugar hasta que alguno gane cinco (5) rondas.
   Ganará quien mayor cantidad de rondas gane.
     Vamos a jugar. Let´s go!!!!!!!!!!!!!!
''')
time.sleep(1.5)
nombre_jugador = input("Mi nombre es Serena y voy a jugar contigo. Cuál es tu nombre? ").upper()

while puntaje_Human != 5 and puntaje_PC != 5:
    menu_option()  # A traves de una funcion se muestra el menú de opciones
    while True:    # Se verifica que solamente use los números 1, 2 o 3
        user_option = input()
        if user_option == "1" or user_option == "2" or user_option == "3":
            break
        else:
            print('Digite solamente el número 1, 2 o 3.') # Si escoge una opcion diferente pide que ingrese una opcion hasta que elija 1, 2 o 3
    
    user_option = int(user_option)
    computer_option = random.choice(options)
    print(f"Escogiste la opcion {options[user_option-1]} y Serena escogió {computer_option}.")
    time.sleep(1.5)

    if user_option == 1:
        if convertirEnteroPCeleccion() == 1:
            print("*********** EMPATE ***********", end= " ")
            time.sleep(1.5)
            print("Punto para ninguno.")
            time.sleep(1.5)
        elif convertirEnteroPCeleccion() == 2:
            print("**** PAPEL envuelve PIEDRA ****", end= " ")
            time.sleep(1.5)
            print("Punto para Serena.")
            time.sleep(1.5)            
            puntaje_PC += 1
        elif convertirEnteroPCeleccion() == 3:
            print("**** PIEDRA rompe TIJERA ****", end= " ")
            time.sleep(1.5)
            print(f"Punto para {nombre_jugador}.")
            time.sleep(1.5)
            puntaje_Human += 1

    if user_option == 2:
        if convertirEnteroPCeleccion() == 1:
            print("**** PAPEL envuelve PIEDRA ****", end= " ")
            time.sleep(1.5)
            print(f"Punto para {nombre_jugador}.")
            time.sleep(1.5)
            puntaje_Human += 1
        elif convertirEnteroPCeleccion() == 2:
            print("*********** EMPATE ***********", end= " ")
            time.sleep(1.5)
            print("Punto para ninguno.")
            time.sleep(1.5)
        elif convertirEnteroPCeleccion() == 3:
            print("**** TIJERA corta PAPEL ****", end= " ")
            time.sleep(1.5)
            print("Punto para Serena.")
            time.sleep(1.5)
            puntaje_PC += 1

    if user_option == 3:
        if convertirEnteroPCeleccion() == 1:
            print("**** PIEDRA rompe TIJERA ****", end= " ")
            time.sleep(1.5)
            print("Punto para Serena.")
            time.sleep(1.5)
            puntaje_PC += 1
        elif convertirEnteroPCeleccion() == 2:
            print("**** TIJERA corta PAPEL ****", end= " ")
            time.sleep(1.5)
            print(f"Punto para {nombre_jugador}.")
            time.sleep(1.5)
            puntaje_Human += 1
        elif convertirEnteroPCeleccion() == 3:
            print("*********** EMPATE ***********", end= " ")
            time.sleep(1.5)
            print("Punto para ninguno.")
            time.sleep(1.5)
            
    print(f"Puntos para Serena: {puntaje_PC}  -  Puntos para {nombre_jugador}: {puntaje_Human}\n")
    time.sleep(1.5)

if puntaje_Human > puntaje_PC:
    print("===================================")
    print("=                                 =")
    print(f"=  Felicidades!!! Ganó {nombre_jugador}  =")
    print("=                                 =")
    print("===================================\n")
else:
    print("===================================")
    print("=                                 =")
    print("= Perdiste!!! Ganó Serena =")
    print("=                                 =")
    print("===================================\n")

print("Vuelve pronto a jugar PIEDRA, PAPEL o TIJERA")