# Libreria
import random
import time

# Variables
Continuar = True
terminar = False
seguir_jugando = True

# Funciones
def Menu ():
    print("""
                                                            
 ------------------------------------------                 ▄▄   ▄▄   ▄▄   ▄▄        
|           | HUNDIR LA FLOTA |           |                 ▒▒   ▒▒   ▒▒   ▒▒         
|           |-----------------|           |               ▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄        
|------------ Menu del juego -------------|             ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄     
| 0. -------- Instruciones ---------------|     ▀██████████████████████████████████████▄ 
| 1. -------- Comenzar el juego ----------|       ▀███████████████████████████████████▀
| 2. -------- Finalizar el juego ---------|         ▀██████████████████████████████▀
|-----------------------------------------|     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     
|____________ By Luis María ______________|     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
                                                                                                  
""")

def limpiar():
    print ("\n"*50)

def imagen(): 
    print("""
                    ▄▄   ▄▄   ▄▄   ▄▄        
                    ▒▒   ▒▒   ▒▒   ▒▒         
                  ▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄        
                ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ 
        ▀██████████████████████████████████████▄
          ▀███████████████████████████████████▀
            ▀██████████████████████████████▀
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒▒▒▒ HUNDIR LA FLOTA ▒▒▒▒▒▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)

def imagen_despedida():
    print("""
      Gracias por jugar, hasta pronto. 👋🏼👋🏼 
                    ▄▄   ▄▄   ▄▄   ▄▄        
                    ▒▒   ▒▒   ▒▒   ▒▒         
                  ▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄        
                ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ 
        ▀██████████████████████████████████████▄
          ▀███████████████████████████████████▀
            ▀██████████████████████████████▀
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒▒▒▒ HUNDIR LA FLOTA ▒▒▒▒▒▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)

# Clases
class Barco():
    def __init__(self):
        self.tocado = 0
        self.horizontal =[]
        self.columna=[]
        self.navega = True # Variable de control. 

    def Nuevo(self,ho,ve):
        self.columna.append(ve)
        self.horizontal.append(ho)

    def tocado(self):
        self.tocado += 1 
        if self.tocado >= 5:
            time.sleep(2)
            print("Felicidades has ganado!!! 👏👏👏 🥇🏆")
            return self.tocado
            self.navega = False  # En caso de que no "navegue" ningún barco el programa termina.

class Tablero():
    def __init__(self):                
        self.flota = Barco()
        self.lista = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]] # Creamos una matriz (una lista de listas)
        horizontal = random.randrange(4)
        vertical = random.randrange(2) +2

        for y in range(3):
            vertical -= 1
            self.lista[horizontal][vertical] = "1" # Si existe un barco en la posicion de la matriz se mostrará el tablero con un "1"
            self.flota.Nuevo(horizontal, vertical)

        horizontal2 = random.randrange(4)     
        self.flota2= Barco()

        if (horizontal2 == horizontal):
            if (horizontal == 5):
                horizontal2 -= random.randrange(3)
            else:
                horizontal2 +=1

        vertical2 = random.randrange(2) +2

        for y in range(3):
            vertical2 -= 1
            self.lista[horizontal2][vertical2] = "0" # Si no existe barco en la posicion de la matriz esa posición se mostrará el tablero con un "0"
            self.flota2.Nuevo(horizontal2, vertical2)
            

class Juego(): # Pedimos el nombre a los dos jugadores y se les pide coordenada (X,Y) el programa comprueba si en la lista existen los barcos y muestra un mensaje por pantalla
    def __init__(self):
        self.marco_juego = Tablero()
        print("Mostrando tablero")
        print(self.marco_juego.lista)
        time.sleep(1.5)
        limpiar()
        while (self.marco_juego.flota.navega == True and self.marco_juego.flota2.navega == True ):
                    time.sleep(1)
                    print(J1 + " escoja una casilla")
                    time.sleep(2)
                    imagen()
                    X = int(input("Introduce una coordenada para el eje X. Valores válidos del 1-5: "))
                    Y = int(input("Introduce una coordenada para el eje Y. Valores válidos del 1-5: "))

                    if (X == self.marco_juego.flota2.horizontal[0]):
                        if (Y in self.marco_juego.flota2.columna):
                            time.sleep(2)
                            print(J1 + " ha tocado un barco ⛵️💥 ")
                            self.marco_juego.flota2.tocado
                        else:
                            time.sleep(2)
                            print(J1 + " ha disparado al agua ⛵️🌊 ")
                    else:
                        time.sleep(2)
                        print(J1 + " ha disparado al agua ⛵️🌊 ")
                    time.sleep(2)
                    limpiar()

                    print(J2 + " escoja una casilla") 
                    time.sleep(2)
                    imagen()           
                    X = int(input("Introduce una coordenada para el eje X. Valores válidos del 1-5: "))
                    Y = int(input("Introduce una coordenada para el eje Y. Valores válidos del 1-5: "))

                    if (X == self.marco_juego.flota.horizontal[0]):
                        if (Y in self.marco_juego.flota.columna):
                            time.sleep(2)
                            print(J2 + " ha tocado un barco ⛵️💥 ")
                            self.marco_juego.flota.tocado
                        else:
                            time.sleep(2)
                            print(J2 + " ha disparado al agua ⛵️🌊 ")
                    else:
                        time.sleep(2)
                        print(J2 + " ha disparado al agua ⛵️🌊 ")
                    time.sleep(2)
                    limpiar()

# Menú del Juego
while Continuar:
    Menu()
    opcion = input("Elige una opción: ")
    time.sleep(2)

    # Jugar
    if opcion == "1":
        time.sleep(1)
        imagen()
        print("Cargando")
        time.sleep(1)
        limpiar()
        imagen()
        print("Cargando.")
        time.sleep(1)
        limpiar()
        imagen()
        print("Cargando..")
        time.sleep(1)
        limpiar()
        imagen()
        print("Cargando...")
        time.sleep(1)
        limpiar()
        imagen()
        print("Cargando....")
        imagen()
        time.sleep(1)
        limpiar()

        print("""
        """)
        imagen()
        J1 = input("Escoge el nombre del J1: ")
        time.sleep(2)
        J2 = input("Escoge el nombre del J2: ")
        time.sleep(2)
        print("Buena suerte a " + J1 + " y " + J2 + " 🤞🏻🤞🏻🤞🏻")
        time.sleep(3)
        limpiar()
        Juego1 = Juego()


       

    # Cerrar el juego
    elif opcion == "2":
        imagen_despedida()
        print("Se está cerrando el juego")
        time.sleep(2)
        limpiar()
        imagen_despedida()
        print("Se está cerrando el juego.")
        time.sleep(2)
        limpiar()
        imagen_despedida()
        print("Se está cerrando el juego..")
        time.sleep(2)
        limpiar()
        imagen_despedida()
        print("Se está cerrando el juego...")
        time.sleep(2)
        limpiar()
        imagen_despedida()
        time.sleep(8)
        limpiar()
        Continuar = False

    # Instrucciones
    elif opcion == "0":
        time.sleep(2)

        print("""
        - Objetivos:
        Desarrollar el juego “Hundir la Flota” mediante el lenguaje de programación Python, utilizando las herramientas de control y estructuras vistas en clase.
        - Características:
        El programa cuenta con un tablero en dos dimensiones de 5x5.
        Los barcos se posicionan aleatoriamente.
        El programa pide al jugador 1 y 2 la posicion y le dice si ha dañado un barco.
        Continua el juego hasta que alguno haya destruido los barcos.
        Después de acabar el juego, se debe permitir reiniciar el juego, sin cerrar el
        programa.
        Para salir pulsa 99.
        """)

        opcion = input("Elige una opción: ")

    elif opcion == "99":
        time.sleep(1.5)
        Menu()

    # Control
    else:
        print("Elige una opcion valida ")
        print("Valores numéricos validos, (0 1 2 99)")
        
     
    # @luismdelacy