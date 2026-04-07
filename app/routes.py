from flask import Blueprint, render_template, request, redirect
from .models import get_connection

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return "Backend funcionando"


@main.route("/doadores", methods=["GET", "POST"])
def cadastrar_doador():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cep = request.form["cep"]

        conn = get_connection()
        conn.execute(
            "INSERT INTO doadores (nome, email, cep) VALUES (?, ?, ?)",
            (nome, email, cep)
        )
        conn.commit()
        conn.close()

        return redirect("/doadores")

    return render_template("doadores.html")