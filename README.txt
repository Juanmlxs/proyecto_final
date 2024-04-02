
Gestor de Tareas con FastAPI y SQLAlchemy
Este proyecto consiste en una API RESTful para gestionar tareas utilizando FastAPI como framework web y SQLAlchemy como ORM para interactuar con una base de datos SQLite.

Instalación
Clona el repositorio desde Git:
bash

git clone https://github.com/Juanmlxs/proyecto_final.git
Accede al directorio del proyecto:
bash

cd tu_repositorio
Instala las dependencias utilizando pip:
bash

pip install -r requirements.txt
Configuración de la Base de Datos
La configuración de la base de datos se encuentra en el archivo config/database.py. Se utiliza SQLite como motor de base de datos.

Ejecución de la Aplicación
Para ejecutar la aplicación, simplemente ejecuta el siguiente comando en la raíz del proyecto:

bash
uvicorn main:app --reload
Esto iniciará el servidor web en localhost en el puerto 8000 de forma predeterminada. Puedes acceder a la documentación de la API visitando http://localhost:8000/docs en tu navegador.

Estructura del Proyecto
config/database.py: Configuración de la base de datos.
models/tareas.py: Definición del modelo SQLAlchemy para la tabla de tareas.
schemas/tareas.py: Esquema Pydantic para las tareas.
services/tareas.py: Servicios para realizar operaciones CRUD en las tareas.
main.py: Punto de entrada de la aplicación FastAPI.
requirements.txt: Archivo que lista las dependencias del proyecto.
