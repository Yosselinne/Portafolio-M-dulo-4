Formulario de Registro de Usuario

Este programa en Python permite crear un formulario de registro básico para que el usuario ingrese su nombre, edad, altura y acepte los términos. Después de recibir los datos, el programa muestra un resumen con la información ingresada, junto con el tipo de cada dato.

Funcionalidades

El formulario solicita los siguientes datos al usuario:

Nombre: El nombre completo del usuario.

Edad: La edad del usuario, ingresada como un número entero.

Altura: La altura del usuario en metros, como un número decimal (float).

Aceptación de términos: El usuario debe responder si acepta los términos, ingresando "si" o "no".

El programa muestra los datos ingresados junto con su tipo de variable.

Requisitos

Python 3.x

Uso

Al ejecutar el programa, se solicitarán los siguientes datos:

Nombre del usuario.

Edad del usuario (en números enteros).

Altura del usuario (en metros).

Confirmación de si acepta los términos (respondiendo "si" o "no").

Una vez completado, el programa mostrará un resumen con los datos ingresados y el tipo de cada uno (por ejemplo, str, int, float).

Ejemplo de Uso
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

Notas

El programa verifica que el usuario ingrese los datos correctamente. Si el usuario introduce un valor incorrecto o no válido (por ejemplo, texto cuando se espera un número), el programa lanzará un error y terminará su ejecución.

La respuesta sobre los términos será interpretada como un valor booleano (True o False), donde "si" es True y "no" es False.