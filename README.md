Aplicación de gestión de tareas

Desarrolla una aplicación web backend utilizando FastAPI para la gestión de una lista de tareas, aplicando de forma integral los conceptos de programación orientada a objetos en Python. La aplicación debe exponer múltiples endpoints REST con diferentes verbos HTTP (GET, POST, PUT, DELETE) y aplicar conceptos de encapsulamiento, abstracción y otros principios de POO. La persistencia de datos se realizará en memoria durante la ejecución de la aplicación. Una vez desarrollada, deberás desplegarla en localhost y crear un script de pruebas con la librería requests que valide el correcto funcionamiento de todos los endpoints, incluyendo casos de error.


- varios endopoints GET, PUT, ...
- persistencia de datos con sqlite
- script de pruebas, lanza requests a endpoints 

Se valora el uso de MVC

--- Modelo - db, crea tablas, SLQAlchemy




--- Vista - frontend





--- Controlador - endpoints, lógica de negocio

    - "/" GET todas las tareas
    - "/tareas" POST nueva tarea
    - "/tareas/{id}" PUT 
    - "/tareas/{id}" DELETE
    