# Funciones de apoyo: validaciones y control de sesion
from flask import session


def requiere_login():
    # True si el usuario NO ha iniciado sesion
    return "usuario" not in session


def validar_producto(nombre, precio, stock):
    # Devuelve una lista de errores (vacia si los datos son validos)
    errores = []
    nombre = (nombre or "").strip()
    if not nombre:
        errores.append("El nombre es obligatorio.")
    elif len(nombre) > 50:
        errores.append("El nombre no puede tener mas de 50 caracteres.")
    try:
        p = float(precio)
        if p <= 0 or p > 999999:
            errores.append("El precio debe ser mayor que 0 y no mayor que 999999.")
    except (TypeError, ValueError):
        errores.append("El precio debe ser un numero valido.")
    try:
        s = int(stock)
        if s < 0 or s > 10000:
            errores.append("El stock debe estar entre 0 y 10000.")
    except (TypeError, ValueError):
        errores.append("El stock debe ser un numero entero.")
    return errores
