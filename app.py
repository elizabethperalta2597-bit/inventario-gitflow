# Aplicacion principal: crea Flask y registra automaticamente los modulos de routes/
import importlib
import pkgutil

from flask import Flask

import routes
from db import cerrar_db, init_db


def crear_app():
    app = Flask(__name__)
    app.secret_key = "clave-de-desarrollo"  # Solo para entorno de desarrollo
    app.teardown_appcontext(cerrar_db)
    # Registra cada archivo de routes/ que defina un blueprint llamado "bp"
    for _, nombre, _ in pkgutil.iter_modules(routes.__path__):
        modulo = importlib.import_module(f"routes.{nombre}")
        if hasattr(modulo, "bp"):
            app.register_blueprint(modulo.bp)
    return app


app = crear_app()

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
