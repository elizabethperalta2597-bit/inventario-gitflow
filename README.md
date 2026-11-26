# Inventario de productos (CRUD) - Git Flow

Proyecto CRUD de inventario hecho con Flask y SQLite para la Tarea 3 (Git y Git Flow).

## Ejecutar
```
pip install -r requirements.txt
python app.py
```
Abrir http://127.0.0.1:5000 - usuario `admin`, contrasena `Admin123!`

## Estructura
- `app.py` crea la aplicacion y registra automaticamente cada modulo de `routes/`
- `db.py` conexion a la base de datos SQLite
- `utils.py` validaciones y control de sesion
- `routes/` una funcionalidad por archivo (login, crear, listar, editar, eliminar)
- `templates/` plantillas HTML

## Flujo de ramas (Git Flow)
- `main`: version estable
- `qa`: pruebas de calidad
- `dev`: integracion del desarrollo
- `feature/*`: una rama por funcionalidad; cada una se integra a `dev`, `qa` y `main` con Pull Requests
