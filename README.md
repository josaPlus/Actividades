# Proyecto Django - Notas

Este proyecto fue desarrollado en Django para gestionar notas (crear, editar, eliminar y ver detalles).

---

## ⚙️ Creación del proyecto paso a paso

### 1️. Crear el proyecto principal

```bash
django-admin startproject Actividades
cd Actividades
```

### 2️. Crear la aplicación "notas"

```bash
python manage.py startapp notas
```

### 3️. Registrar la app en `settings.py`

Dentro de `Actividades/settings.py`, agrega en la lista de `INSTALLED_APPS`:

```python
'notas.apps.NotasConfig',
```

### 4️. Crear las migraciones iniciales

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️. Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6️. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Luego abre en tu navegador:
[http://127.0.0.1:8000/notas/](http://127.0.0.1:8000/notas/)

---

## Archivos HTML incluidos

* **lista.html** → muestra todas las notas y permite crear una nueva.
* **detalle.html** → muestra una nota individual con opciones de editar o eliminar.
* **formulario.html** → formulario para crear o editar notas.

Cada plantilla tiene su propio archivo CSS en la carpeta `static`.

---

Desarrollado con **Django 5.2.7** y **Python 3.12.**
