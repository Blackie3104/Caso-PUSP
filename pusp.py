from usuario import Usuario
from recurso import Recurso
from pago import Pago
import datetime

class PUSP:
    def __init__(self):
        self.usuarios = []
        self.recursos = [Recurso("Computadora", "Tecnología"), Recurso("Bicicleta", "Transporte")]
        self.pagos = []

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")

        # Validar información
        if not nombre or not correo or not contraseña:
            print("Error: Todos los campos son obligatorios.")
            return

        for usuario in self.usuarios:
            if usuario.correo == correo:
                print("Error: El correo electrónico ya está registrado.")
                return

        # Crear cuenta de usuario
        usuario = Usuario(nombre, correo, contraseña)
        self.usuarios.append(usuario)
        print("¡Usuario registrado correctamente!")

    def alquilar_recurso(self):
        if not self.usuarios:
            print("Error: No hay usuarios registrados.")
            return

        print("Recursos disponibles:")
        for i, recurso in enumerate(self.recursos, 1):
            print(f"{i}. {recurso.nombre} - {recurso.tipo} - {'Disponible' if recurso.disponible else 'No disponible'}")

        opcion = int(input("Seleccione el número de recurso que desea alquilar: "))
        if opcion < 1 or opcion > len(self.recursos):
            print("Error: Opción inválida.")
            return

        recurso = self.recursos[opcion - 1]
        if not recurso.disponible:
            print("Error: El recurso seleccionado no está disponible.")
            return

        fecha_alquiler = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        recurso.disponible = False
        print(f"¡{recurso.nombre} alquilado correctamente para el {fecha_alquiler}!")

    def pagar_servicio(self):
        if not self.usuarios:
            print("Error: No hay usuarios registrados.")
            return

        print("Servicios disponibles para pagar:")
        servicios = ["Comida en la cafetería", "Materiales de papelería"]
        for i, servicio in enumerate(servicios, 1):
            print(f"{i}. {servicio}")

        opcion = int(input("Seleccione el número de servicio que desea pagar: "))
        if opcion < 1 or opcion > len(servicios):
            print("Error: Opción inválida.")
            return

        cantidad = float(input("Ingrese la cantidad a pagar: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor que cero.")
            return

        fecha_pago = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pago = Pago(servicios[opcion - 1], cantidad, fecha_pago)
        self.pagos.append(pago)
        print(f"¡Pago de {cantidad} por {pago.servicio} realizado correctamente el {fecha_pago}!")
