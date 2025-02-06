import json

class Ventanillas:
    def __init__(self):
        try:
            with open("Usuarios.json", "r") as archivo:
                self.diccionario = json.load(archivo)
        except FileNotFoundError:
            self.diccionario = {}
            self.guardar_datos()

    def guardar_datos(self):
        with open("Usuarios.json", "w") as archivo:
            json.dump(self.diccionario, archivo, indent=4)

    def obtener_cola(self):
        return list(self.diccionario.items())

    def eliminar_ticket(self, matricula):
        if matricula in self.diccionario:
            del self.diccionario[matricula]
            self.guardar_datos()
            print(f"¡El ticket '{matricula}' ha sido eliminado!")
        else:
            print(f"El ticket '{matricula}' no existe.")

# Diccionarios de usuarios por sector
Cajas = {"cajas1": "CA196", "cajas2": "CA997", "cajas3": "CA775", "cajas4": "CA446"}
Servicio_Estudiantil = {"SE1": "SE123", "SE2": "SE223", "SE3": "SE779", "SE4": "SE336"}
Servicio_Becario = {"BECA": "BECA1"}

def procesar_ticket(usuario, ventanillas):
    cola = ventanillas.obtener_cola() 
    if not cola:
        print("No hay tickets en la cola.")
        return

    # Determinar a qué sector pertenece el usuario
    if usuario in Cajas:
        usuario_sector = "Cajas"
    elif usuario in Servicio_Estudiantil:
        usuario_sector = "Servicios Escolares"
    elif usuario in Servicio_Becario:
        usuario_sector = "Becas"
    else:
        print("Usuario no reconocido.")
        return

    # Recorrer la cola para buscar el primer ticket del sector del usuario
    ticket_encontrado = False
    for matricula, ticket in cola:
        # Identificar el sector del ticket según su prefijo
        if ticket.startswith("SE"):
            sector_ticket = "Servicios Escolares"
        elif ticket.startswith("C"):
            sector_ticket = "Cajas"
        elif ticket.startswith("B"):
            sector_ticket = "Becas"
        else:
            print(f"Error: El ticket '{ticket}' tiene un sector desconocido.")
            continue  # Se omite el ticket con sector desconocido

        if sector_ticket == usuario_sector:
            print(f"Procesando ticket de {sector_ticket}: Matrícula {matricula} - Ticket {ticket}")
            ventanillas.eliminar_ticket(matricula)
            print("¡Ticket procesado y eliminado exitosamente!")
            ticket_encontrado = True
            break  # Se sale del ciclo al procesar el primer ticket válido

    if not ticket_encontrado:
        print("No tienes tickets para atender en este momento.")

def iniciar_sesion():
    while True:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario in Cajas and contraseña == Cajas[usuario]:
            return usuario
        elif usuario in Servicio_Estudiantil and contraseña == Servicio_Estudiantil[usuario]:
            return usuario
        elif usuario in Servicio_Becario and contraseña == Servicio_Becario[usuario]:
            return usuario
        else:
            print("Usuario o contraseña incorrectos.")

# Ejecución del programa
ventanillas = Ventanillas()
usuario_autenticado = iniciar_sesion()
procesar_ticket(usuario_autenticado, ventanillas)
