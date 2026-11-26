# Funcionalidad: crear un producto (Create)
from flask import Blueprint, flash, redirect, render_template, request

from db import get_db
from utils import requiere_login, validar_producto

bp = Blueprint("crear", __name__)


@bp.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo():
    if requiere_login():
        return redirect("/login")
    errores = []
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        precio = request.form.get("precio", "")
        stock = request.form.get("stock", "")
        errores = validar_producto(nombre, precio, stock)
        if not errores:
            db = get_db()
            db.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                       (nombre.strip(), float(precio), int(stock)))
            db.commit()
            flash("Producto creado correctamente.")
            return redirect("/productos")
    return render_template("formulario.html", titulo="Nuevo producto", errores=errores,
                           producto=request.form)
