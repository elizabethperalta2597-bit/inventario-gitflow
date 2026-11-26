# Funcionalidad: inicio y cierre de sesion
from flask import Blueprint, redirect, render_template, request, session

bp = Blueprint("auth", __name__)

# Credenciales del usuario de prueba
USUARIO = "admin"
CLAVE = "Admin123!"


@bp.route("/")
def inicio():
    # La pagina principal lleva a la lista de productos
    return redirect("/productos")


@bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "")
        if not usuario or not clave:
            error = "Usuario y contrasena son obligatorios."
        elif usuario == USUARIO and clave == CLAVE:
            session["usuario"] = usuario
            return redirect("/productos")
        else:
            error = "Credenciales incorrectas."
    return render_template("login.html", error=error)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
