# EVA_03_POO – Consumo de API y Persistencia de Datos (Posts y Comments)

## Descripción
Este proyecto corresponde a la **Evaluación Unidad 3** de la asignatura **Programación Orientada a Objetos**, y consiste en una aplicación de consola desarrollada en **Python**, que implementa una arquitectura modular por capas para el consumo de una API externa y la persistencia de datos en una base de datos relacional.

La aplicación trabaja con el grupo de datos **publicaciones con comentarios (posts y comments)** obtenidos desde la API pública **JSONPlaceholder**.

---

## Arquitectura del Proyecto
El proyecto está organizado siguiendo principios de **modularización y separación de responsabilidades**, distribuyendo la lógica en los siguientes módulos:

- **auxiliares**: constantes y configuraciones generales.
- **servicios**: consumo de la API externa (GET, POST, PUT, DELETE).
- **negocio**: procesamiento de datos y reglas de negocio, incluyendo encriptación.
- **datos**: acceso y persistencia de datos en base de datos MySQL.
- **modelos**: definición de clases del dominio (Usuario, Post, Comment).
- **interfaces_usuario**: interacción con el usuario mediante menú por consola.
- **main.py**: punto de entrada de la aplicación.

Esta estructura permite un código más mantenible, escalable y alineado con los conceptos de la Programación Orientada a Objetos.

---

## API Utilizada
Se utiliza la API pública **JSONPlaceholder**:

- Posts: https://jsonplaceholder.typicode.com/posts  
- Comments: https://jsonplaceholder.typicode.com/comments  

Las operaciones implementadas son:
- GET: obtención de datos desde la API.
- POST: creación de recursos.
- PUT: actualización de recursos.
- DELETE: eliminación de recursos.

---

## Base de Datos
La persistencia de datos se realiza utilizando **MySQL**, a través de **WAMPServer**.

### Base de datos
- Nombre: `evaluacion_u3_poo`

### Tablas
- `usuarios`: almacenamiento de usuarios de la aplicación.
- `posts`: respaldo de publicaciones obtenidas desde la API.
- `comments`: respaldo de comentarios asociados a publicaciones.

La tabla `comments` mantiene una relación con `posts` mediante la clave foránea `postId`.

---

## Seguridad
El sistema implementa **encriptación de contraseñas** utilizando el algoritmo **SHA-256**.

- Las contraseñas **no se almacenan en texto plano**.
- En el proceso de login, la contraseña ingresada se vuelve a encriptar y se compara con el hash almacenado.
- Para el ingreso de contraseñas en consola se utiliza la librería estándar `getpass`, evitando que el texto sea visible.

---

## Funcionalidades
La aplicación permite:

1. Registro de usuarios con contraseña encriptada.
2. Inicio de sesión (login).
3. Obtención de posts y comments desde la API y almacenamiento en la base de datos.
4. Consulta de datos almacenados en la base de datos.
5. Creación de posts y comments mediante POST.
6. Actualización de posts y comments mediante PUT.
7. Eliminación de posts y comments mediante DELETE.
8. Manejo básico de errores HTTP (404, 500 y otros).

---

## Requisitos
- Python 3.x
- WAMPServer (MySQL activo)
- Base de datos creada previamente (`evaluacion_u3_poo`)
- Librerías indicadas en `requirements.txt`

---

## Instalación
Instalar las dependencias del proyecto:

pip install -r requirements.txt

## Ejecución
python main.py

## Observaciones
Este proyecto fue desarrollado respetando los lineamientos entregados para la evaluación, aplicando conceptos de Programación Orientada a Objetos, modularización, seguridad básica y consumo de servicios web.
