archivo = "listado_de_precios.txt"

while True:
    print("\nMenú:")
    print("1) Añadir producto")
    print("2) Mostrar listado de precios")
    print("3) Consultar precio de un producto")
    print("4) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio sin IVA: ")

        precio = float(precio) 
        precio_con_iva = precio * 1.21 
        precio_con_iva = round(precio_con_iva, 2) 

        f = open(archivo, "a") 
        f.write(nombre + "," + str(precio_con_iva) + "\n") 
        f.close() 

        print("Producto guardado.")

    elif opcion == "2":
        f = open(archivo, "r") 
        lineas = f.readlines() 
        f.close() 

        print("\nListado de productos con IVA:")
        for linea in lineas:
            print(linea.strip())

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a buscar: ")

        f = open(archivo, "r") 
        lineas = f.readlines() 
        f.close