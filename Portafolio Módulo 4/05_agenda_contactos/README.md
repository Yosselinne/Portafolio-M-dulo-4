Agenda de Contactos

Este programa en Python permite gestionar una agenda de contactos de forma interactiva. Los usuarios pueden agregar nuevos contactos con su nombre y teléfono, ver todos los contactos almacenados, o salir del programa. Los datos se guardan en un diccionario para facilitar la consulta y modificación.

Funcionalidades

El programa tiene las siguientes opciones en su menú:

Agregar contacto: Permite agregar un nuevo contacto a la agenda. El programa solicita el nombre y el teléfono del contacto, y lo guarda en un diccionario.

Mostrar agenda: Muestra todos los contactos almacenados en la agenda. Si no hay contactos, el programa indica que la agenda está vacía.

Salir: Finaliza la ejecución del programa.

Requisitos

Python 3.x

Uso

Al ejecutar el programa, aparecerá un menú con tres opciones:

1: Agregar un nuevo contacto.

2: Ver todos los contactos almacenados en la agenda.

3: Salir del programa.

Al seleccionar la opción 1, el programa pedirá al usuario que ingrese el nombre y el teléfono del nuevo contacto. Luego, le preguntará si desea agregar otro contacto. Si responde "sí", el proceso se repite. Si responde "no", volverá al menú principal.

Al seleccionar la opción 2, el programa mostrará todos los contactos en la agenda. Si la agenda está vacía, se mostrará un mensaje indicándolo.

Si elige la opción 3, el programa finalizará.

Ejemplo de Uso
----- Menú Agenda -----
1. Agregar contacto
2. Mostrar agenda
3. Salir
Elige una opción: 1
Ingresa el nombre del contacto: Juan
Ingresa el teléfono del contacto: 123456789
Contacto Juan agregado.
¿Quieres agregar otro contacto? (si/no): si
Ingresa el nombre del contacto: Maria
Ingresa el teléfono del contacto: 987654321
Contacto Maria agregado.
¿Quieres agregar otro contacto? (si/no): no

----- Menú Agenda -----
1. Agregar contacto
2. Mostrar agenda
3. Salir
Elige una opción: 2

Agenda:
Juan: 123456789
Maria: 987654321

----- Menú Agenda -----
1. Agregar contacto
2. Mostrar agenda
3. Salir
Elige una opción: 3
¡Hasta luego!

Notas

Los contactos se almacenan en un diccionario donde el nombre del contacto es la clave y el número de teléfono es el valor.

El programa permite agregar contactos con el mismo nombre, pero siempre sobrescribirá el número de teléfono si se introduce el mismo nombre más de una vez.

Si la agenda está vacía, al elegir la opción de mostrar la agenda, el programa indicará que no hay contactos.