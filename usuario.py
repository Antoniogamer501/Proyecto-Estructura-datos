import json
import random as r
import re
import os
import time

while True:

    class Usuario:
        def __init__(self):
            try:
                with open("Usuarios.json", "r") as archivo:
                    self.diccionario = json.load(archivo)
            except FileNotFoundError:
                self.diccionario = {}


        def MatriculaUsuario(self):
            try:
                print("Opcion 1: Cajas\nOpcion 2: Becas\nOpcion 3: Servicios escolares")
                aDonde = int
                while aDonde ==  int:
                    try:
                        aDonde = int (input("Escoge una opcion: "))
                    except ValueError:
                        print("Error no se selecciono una opcion correcta")
                
                TicketFinal = None

                while TicketFinal is None or TicketFinal in self.diccionario.values():
                    match aDonde:
                        case 1:
                            ticket = r.randint(1000, 9999)
                            TicketFinal = f"C{ticket}"
                        case 2:
                            ticket = r.randint(1000, 9999)
                            TicketFinal = f"B{ticket}"
                        case 3:
                            ticket = r.randint(1000, 9999)
                            TicketFinal = f"SE{ticket}"
                        case _:
                            print("Opcion no encontrada")
                            while aDonde !=  int:
                                try:
                                    aDonde = int (input("Escoge una opcion: "))
                                    break
                                except ValueError:
                                    print("Error no se selecciono una opcion correcta")

                while True:
                        matriculasreg={28385, 29438, 69696, 21783, 29509}
                        matricula = input("Ingrese su matricula: ")
                        if re.fullmatch(r"\d+", matricula) and int(matricula) in matriculasreg:
                            if matricula in self.diccionario:
                                print("matricula ya registrada")
                                return
                            else:
                                break
                        else:
                            print("La matricula debe de ser numeros y debe de estar registrada por la institución")

                self.diccionario[matricula] = TicketFinal

                with open("Usuarios.json", "w") as archivo:
                    json.dump(self.diccionario, archivo, indent=4)
                    print(f"Matricula del Usuario {matricula}, Ticket {TicketFinal}")
            except Exception as e:
                print(f"Error: {e}")
                return
    def limpiar_consola():
        # Si el sistema operativo es Windows, utiliza 'cls', sino utiliza 'clear'
        os.system('cls' if os.name == 'nt' else 'clear')

    usuario = Usuario()

    usuario.MatriculaUsuario()
    
    time.sleep(3)
    limpiar_consola()
            
            
                    
                    
