Menú de Opciones: Tabla de Multiplicar y Factorial

Este programa en Python ofrece un menú interactivo que permite realizar dos operaciones matemáticas básicas: generar la tabla de multiplicar de un número y calcular el factorial de un número. El usuario puede seleccionar una de las opciones del menú y obtener los resultados correspondientes.

Funcionalidades

El programa presenta dos opciones principales:

Tabla de Multiplicar: El programa genera la tabla de multiplicar de un número proporcionado por el usuario, desde el 1 hasta el 10.

Calculadora de Factorial: El programa calcula el factorial de un número ingresado por el usuario utilizando un bucle while. También maneja el caso de números negativos, ya que el factorial no está definido para ellos.

El programa sigue ejecutándose hasta que el usuario elija salir.

Requisitos

Python 3.x

Uso

Al ejecutar el programa, aparecerá un menú con las siguientes opciones:

1: Tabla de multiplicar.

2: Calculadora de factorial.

3: Salir del programa.

Si el usuario elige la opción para la tabla de multiplicar, se le pedirá un número y se mostrará la tabla de multiplicar de ese número, desde el 1 hasta el 10.

Si el usuario elige la opción para calcular el factorial, se le pedirá un número, y el programa calculará su factorial utilizando un bucle while.

Si el usuario elige salir (opción 3), el programa finalizará.

Ejemplo de Uso
--- Menú de opciones ---
1. Tabla de multiplicar
2. Calculadora de factorial
3. Salir
Selecciona una opción: 1
Ingresa un número para la tabla de multiplicar: 5

Tabla del 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

--- Menú de opciones ---
1. Tabla de multiplicar
2. Calculadora de factorial
3. Salir
Selecciona una opción: 2
Ingresa un número para calcular su factorial: 4
El factorial de 4 es 24

--- Menú de opciones ---
1. Tabla de multiplicar
2. Calculadora de factorial
3. Salir
Selecciona una opción: 3
¡Hasta luego!

Notas

Si el usuario ingresa un valor no válido (por ejemplo, un texto cuando se espera un número entero), el programa mostrará un mensaje de error y le pedirá un nuevo valor.

El cálculo del factorial no se realiza para números negativos, ya que el factorial solo está definido para enteros no negativos.