0
ingresos = []
gastos = []

opcion = 0 

while opcion != 5:
    print("\n=== CALCULADORA DE INGRESOS Y GASTOS ===")
    print("1. Añadir ingreso")
    print("2. Añadir gasto")
    print("3. Mostrar balance total")
    print("4. Mostrar listado de movimientos")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        cantidad = float(input("Introduce el importe del ingreso: "))
        ingresos.append(cantidad)
        print("Ingreso registrado correctamente.")

    elif opcion == 2:
        cantidad = float(input("Introduce el importe del gasto: "))
        gastos.append(cantidad)
        print("Gasto registrado correctamente.")

    elif opcion == 3:
        total_ingresos = sum(ingresos)
        total_gastos = sum(gastos)
        balance = total_ingresos - total_gastos

        print("\n--- BALANCE ---")
        print("Total ingresado:", total_ingresos)
        print("Total gastado:", total_gastos)
        print("Balance final:", balance)

    elif opcion == 4:
        print("\n--- LISTA DE INGRESOS ---")
        for i in ingresos:
            print(i)

        print("\n--- LISTA DE GASTOS ---")
        for g in gastos:
            print(g)

    elif opcion == 5:
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Inténtalo de nuevo.")


