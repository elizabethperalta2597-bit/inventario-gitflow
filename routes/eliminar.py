# Funcionalidad: eliminar un producto (Delete)
from flask import Blueprint, flash, redirect

from db import get_db
from utils import requiere_login

bp = Blueprint("eliminar", __name__)


@bp.route("/productos/<int:pid>/eliminar", methods=["POST"])
def eliminar(pid):
    if requiere_login():
        return redirect("/login")
    db = get_db()
    db.execute("DELETE FROM productos WHERE id = ?", (pid,))
    db.commit()
    flash("Producto eliminado correctamente.")
    return redirect("/productos")
