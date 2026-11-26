# Funcionalidad: listar productos (Read)
from flask import Blueprint, redirect, render_template

from db import get_db
from utils import requiere_login

bp = Blueprint("listar", __name__)


@bp.route("/productos")
def productos():
    if requiere_login():
        return redirect("/login")
    filas = get_db().execute("SELECT * FROM productos ORDER BY id DESC").fetchall()
    return render_template("productos.html", productos=filas)
