Proyecto de Programas en Python

Este repositorio contiene una serie de programas sencillos en Python para resolver tareas comunes. Cada programa está diseñado para ser interactivo, pidiendo datos al usuario y mostrando resultados en tiempo real. Los programas cubren temas como conversiones de unidades, operaciones matemáticas, gestión de contactos y más.

Programas Incluidos

Conversor de Unidades (01_conversor_unidades.py)

Convierte entre diferentes unidades de medida:

Temperatura: Celsius a Fahrenheit y viceversa.

Monedas: Pesos chilenos (CLP) a dólares estadounidenses (USD) y viceversa.

Longitudes: Metros a pies y viceversa.

Formulario de Registro de Usuario (02_formulario_usuario.py)

Recoge información del usuario: nombre, edad, altura y aceptación de términos.

Muestra un resumen de los datos ingresados junto con su tipo de variable.

Programa Númerico (03_programa_númerico.py)

Permite al usuario ingresar números y determina si son positivos, negativos o cero.

Ofrece la opción de ingresar más números o salir del programa.

Menú de Opciones: Tabla de Multiplicar y Factorial (04_bucles_for_while.py)

Presenta un menú interactivo para:

Generar la tabla de multiplicar de un número.

Calcular el factorial de un número utilizando un bucle while.

Agenda de Contactos (05_agenda_contactos.py)

Permite al usuario agregar, ver y gestionar una agenda de contactos:

Se almacenan contactos con nombre y teléfono.

El usuario puede agregar nuevos contactos o ver los contactos existentes.

Calculadora de Áreas de Figuras Geométricas (06_areas_figuras.py)

Calcula el área de diversas figuras geométricas:

Cuadrado, rectángulo, círculo y triángulo.

El usuario ingresa los datos necesarios y el programa calcula el área correspondiente.

Requisitos

Python 3.x

No se requieren librerías adicionales, excepto el módulo math en el programa de áreas.

Instrucciones de Uso

Clona o descarga el repositorio.

Ejecuta el archivo Python que desees usar.

Sigue las instrucciones del programa en la consola para interactuar con el sistema.

Ejemplos de Uso

Conversor de Unidades:

--- Elige un tipo de conversor ---
1. Conversor de temperatura
2. Conversor CLP y USD
3. Conversor metros y pies
4. Salir
Ingresa una opción: 1
Conversión de temperatura:
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
Elige una opción: 1
Ingresa temperatura en °C: 25
25.0°C = 77.00°F


Formulario de Usuario:

Formulario de registro

Nombre: Juan
Edad: 30
Altura (en metros): 1.75
¿Acepta los términos? (si/no): si

Resumen:
Nombre: Juan (tipo: str)
Edad: 30 (tipo: int)
Altura: 1.75 m (tipo: float)
Acepta términos: True (tipo: bool)


Programa Númerico:

Ingresa un número: 5
El número es positivo.
¿Quieres ingresar otro número? (si/no): si
Ingresa un número: -3
El número es negativo.
¿Quieres ingresar otro número? (si/no): no
Programa finalizado.


Menú de Opciones:

--- Menú Agenda ---
1. Agregar contacto
2. Mostrar agenda
3. Salir
Elige una opción: 1
Ingresa el nombre del contacto: Juan
Ingresa el teléfono del contacto: 123456789
Contacto Juan agregado.
¿Quieres agregar otro contacto? (si/no): no


Calculadora de Áreas:

--- Calculadora de áreas ---
1. Cuadrado
2. Rectángulo
3. Círculo
4. Triángulo
5. Salir
Elige una figura (1-5): 1
Ingresa el lado del cuadrado: 5
Área del cuadrado: 25.00

Notas

Cada programa es independiente y puede ejecutarse de manera autónoma.

Los programas interactúan con el usuario mediante la consola, pidiendo datos e imprimiendo resultados.

Si el usuario ingresa datos inválidos (como letras cuando se esperan números), el programa mostrará un mensaje de error y permitirá ingresar los datos nuevamente.
