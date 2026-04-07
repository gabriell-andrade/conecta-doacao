from flask import Blueprint, render_template, request, redirect
from .models import get_connection

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return "Backend funcionando 🚀"


@main.route("/doadores", methods=["GET", "POST"])
def cadastrar_doador():
    conn = get_connection()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cep = request.form.get("cep")
        rua = request.form.get("rua", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")

        conn.execute(
            """INSERT INTO doadores 
            (nome, email, cep, rua, cidade, estado) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (nome, email, cep, rua, cidade, estado)
        )
        conn.commit()

    doadores = conn.execute("SELECT * FROM doadores").fetchall()
    conn.close()

    return render_template("doadores.html", doadores=doadores)


@main.route("/excluir/<int:id>")
def excluir_doador(id):
    conn = get_connection()
    conn.execute("DELETE FROM doadores WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/doadores")


@main.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_doador(id):
    conn = get_connection()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cep = request.form.get("cep")
        rua = request.form.get("rua", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")

        conn.execute(
            """UPDATE doadores 
            SET nome = ?, email = ?, cep = ?, rua = ?, cidade = ?, estado = ?
            WHERE id = ?""",
            (nome, email, cep, rua, cidade, estado, id)
        )
        conn.commit()
        conn.close()

        return redirect("/doadores")

    doador = conn.execute(
        "SELECT * FROM doadores WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("editar.html", doador=doador)