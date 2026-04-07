from flask import Blueprint, render_template, request, redirect
from .models import get_connection

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return "Backend funcionando"


@main.route("/doadores", methods=["GET", "POST"])
def cadastrar_doador():
    conn = get_connection()

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cep = request.form["cep"]

        conn.execute(
            "INSERT INTO doadores (nome, email, cep) VALUES (?, ?, ?)",
            (nome, email, cep)
        )
        conn.commit()

    doadores = conn.execute("SELECT * FROM doadores").fetchall()
    conn.close()

    return render_template("doadores.html", doadores=doadores)