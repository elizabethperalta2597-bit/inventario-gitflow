# Funcionalidad: editar un producto (Update)
from flask import Blueprint, flash, redirect, render_template, request

from db import get_db
from utils import requiere_login, validar_producto

bp = Blueprint("editar", __name__)


@bp.route("/productos/<int:pid>/editar", methods=["GET", "POST"])
def editar(pid):
    if requiere_login():
        return redirect("/login")
    db = get_db()
    producto = db.execute("SELECT * FROM productos WHERE id = ?", (pid,)).fetchone()
    if producto is None:
        return redirect("/productos")
    errores = []
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        precio = request.form.get("precio", "")
        stock = request.form.get("stock", "")
        errores = validar_producto(nombre, precio, stock)
        if not errores:
            db.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                       (nombre.strip(), float(precio), int(stock), pid))
            db.commit()
            flash("Producto actualizado correctamente.")
            return redirect("/productos")
        producto = request.form
    return render_template("formulario.html", titulo="Editar producto", errores=errores,
                           producto=producto)
