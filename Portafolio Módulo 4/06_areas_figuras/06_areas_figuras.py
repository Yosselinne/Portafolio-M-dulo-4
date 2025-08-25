import math

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def mostrar_menu():
    print("\n--- Calculadora de áreas ---")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una figura (1-5): ")
    if opcion == "1":
        lado = float(input("Ingresa el lado del cuadrado: "))
        print(f"Área del cuadrado: {area_cuadrado(lado):.2f}")
    elif opcion == "2":
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f}")
    elif opcion == "3":
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"Área del círculo: {area_circulo(radio):.2f}")
    elif opcion == "4":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        print(f"Área del triángulo: {area_triangulo(base, altura):.2f}")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
