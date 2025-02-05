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

Cajas = {"cajas1": "CA196", "cajas2": "CA997", "cajas3": "CA775", "cajas4": "CA446"}
Servicio_Estudiantil = {"SE1": "SE123", "SE2": "SE223", "SE3": "SE779", "SE4": "SE336"}
Servicio_Becario = {"BECA": "BECA1"}

def procesar_ticket(usuario, ventanillas):
    cola = ventanillas.obtener_cola() 
    
    if not cola:
        print("No hay tickets en la cola.")
        return
    
    matricula, ticket = cola[0] 
    
    if ticket.startswith("SE"):
        sector = "Servicios Escolares"
    elif ticket.startswith("C"):
        sector = "Cajas"
    elif ticket.startswith("B"):
        sector = "Becas"
    else:
        print("Error: Sector desconocido.")
        return
    
    if (usuario in Cajas and sector == "Cajas") or \
       (usuario in Servicio_Estudiantil and sector == "Servicios Escolares") or \
       (usuario in Servicio_Becario and sector == "Becas"):
        print(f"Procesando ticket de {sector}: {matricula} - {ticket}")
        ventanillas.eliminar_ticket(matricula)
        print("¡Ticket procesado y eliminado exitosamente!")
    else:
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

ventanillas = Ventanillas()
usuario_autenticado = iniciar_sesion()
procesar_ticket(usuario_autenticado, ventanillas)