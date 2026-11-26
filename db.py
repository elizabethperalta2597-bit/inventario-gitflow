# Conexion a la base de datos SQLite
import os
import sqlite3
from flask import g

# Ruta de la base de datos (se puede cambiar con la variable DB_PATH)
DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "inventario.db"))


def get_db():
    # Abre una conexion por peticion y la guarda en g
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


def cerrar_db(_error=None):
    # Cierra la conexion al terminar la peticion
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    # Crea la tabla de productos si no existe
    db = sqlite3.connect(DB_PATH)
    db.execute(
        "CREATE TABLE IF NOT EXISTS productos ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nombre TEXT NOT NULL,"
        "precio REAL NOT NULL,"
        "stock INTEGER NOT NULL)"
    )
    db.commit()
    db.close()
