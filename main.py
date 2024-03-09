from pusp import PUSP

# Crear instancia de la plataforma
pusp = PUSP()

# Menú de la plataforma
while True:
    print("\nPlataforma Universitaria de Servicios y Préstamos (PUSP)")
    print("1. Registrar Usuario")
    print("2. Alquilar Recurso")
    print("3. Pagar Servicio")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        pusp.registrar_usuario()
    elif opcion == 2:
        pusp.alquilar_recurso()
    elif opcion == 3:
        pusp.pagar_servicio()
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")

print("¡Gracias por usar PUSP!")
