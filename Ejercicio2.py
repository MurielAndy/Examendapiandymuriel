clientes = {} 


try:
    with open("clientes.txt", "r") as archivo:
        for linea in archivo:
            nombre, suscrito = linea.strip().split(",")
            clientes[nombre] = suscrito == "True"
except FileNotFoundError:
    pass 

while True:
    print("\nMenú:")
    print("1) Añadir cliente")
    print("2) Consultar estado de suscripción")
    print("3) Mostrar todos los clientes")
    print("4) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        suscripcion = input("¿Está suscrito? (si/no): ").strip().lower()

        if suscripcion == "si":
            clientes[nombre] = True
        elif suscripcion == "no":
            clientes[nombre] = False
        else:
            print("Opción no válida. Solo se acepta 'si' o 'no'.")