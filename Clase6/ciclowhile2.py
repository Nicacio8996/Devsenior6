menu = """
===Restaurante🥰El🤺Buen🩻Sabor🚘===
1. Amburguesa - 20.000
2. Pizza - 15.000
3. Ensalada - 4.500
4. Salchipapa - 5.000
5. Perro Caliente - 12.000
6. salir
"""


print(menu)
precios = {
    1: 20000,
    2: 15000,
    3: 4500,
    4: 5000,
    5: 12000
}
total_por_producto = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
suma_total = 0
opcion = 0
while opcion != 6:
    opcion = int(input("Ingresa una opción del menu: "))
    if opcion == 1:
        suma_total += precios[1]
        total_por_producto[1] += 1
        print("Has elegido Amburguesa🍔:")
    elif opcion == 2:
        suma_total += precios[2]
        total_por_producto[2] += 1
        print("Has elegido Pizza🍕")
    elif opcion == 3:
        suma_total += precios[3]
        total_por_producto[3] += 1
        print("Has elegido Ensalada🥬")
    elif opcion == 4:
        suma_total += precios[4]
        total_por_producto[4] += 1
        print("Has elegido salchipapa🍠")
    elif opcion == 5:
        suma_total += precios[5]
        total_por_producto[5] += 1
        print("Has elegido Perro Caliente🌭")
    elif opcion == 6:
        print(f"Has elegido Salir, Gracias por tu visita, vuelve pronto🥗")
        print("===DETALLE DE PRODUCTOS Y TOTAL A PAGAR===")
        print(f"Pediste🍔: {total_por_producto[1]} Amburguesas - ${total_por_producto[1] * precios[1]}")
        print(f"Pediste🍕: {total_por_producto[2]} Pizzas - ${total_por_producto[2] * precios[2]}")
        print(f"Pediste🥬: {total_por_producto[3]} Ensaladas - ${total_por_producto[3] * precios[3]}")
        print(f"Psediste🍠: {total_por_producto[4]} Salchipapas - ${total_por_producto[4] * precios[4]}")
        print(f"Pediste🌭: {total_por_producto[5]} Perros Calientes - ${total_por_producto[5] * precios[5]}")
        print("===PARA UN TOTAL DE=== ")
        print(f"${suma_total}")
        break
    else:
        print("Opción no valida. Por favor, elige una opcion del menú😱")
    print(menu)
        