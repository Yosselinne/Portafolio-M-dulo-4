print("Formulario de registro\n")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura (en metros): "))
acepta = input("¿Acepta los términos? (si/no): ").strip().lower() == "si"

print("\nResumen:\n")
print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
print(f"Edad: {edad} (tipo: {type(edad).__name__})")
print(f"Altura: {altura} m (tipo: {type(altura).__name__})")
print(f"Acepta términos: {acepta} (tipo: {type(acepta).__name__})")
