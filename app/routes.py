from flask import Blueprint, render_template, request, redirect, session
from .models import get_connection

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = get_connection()
        user = conn.execute(
            "SELECT * FROM usuarios WHERE email = ? AND senha = ?",
            (email, senha)
        ).fetchone()
        conn.close()

        if user:
            session["usuario_id"] = user["id"]
            session["tipo"] = user["tipo"]
            session["email"] = user["email"]
            session["nome"] = user["nome"]
            return redirect("/perfil")

        return "Login inválido"

    return render_template("login.html")


@main.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = get_connection()

        existente = conn.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,)
        ).fetchone()

        if existente:
            conn.close()
            return "Usuário já existe"

        conn.execute(
            "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, 'user')",
            (nome, email, senha)
        )
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("cadastro.html")


def verificar_login():
    return session.get("usuario_id") is not None


@main.route("/doadores", methods=["GET", "POST"])
def cadastrar_doador():
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cep = request.form.get("cep")
        rua = request.form.get("rua", "")
        numero = request.form.get("numero", "")
        complemento = request.form.get("complemento", "")
        bairro = request.form.get("bairro", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")
        descricao = request.form.get("descricao", "")

        usuario_id = session.get("usuario_id")

        conn.execute(
            """INSERT INTO doadores 
            (usuario_id, nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (usuario_id, nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao)
        )
        conn.commit()

    doadores = conn.execute("SELECT * FROM doadores").fetchall()
    conn.close()

    return render_template("doadores.html", doadores=doadores)


@main.route("/excluir/<int:id>")
def excluir_doador(id):
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()
    conn.execute("DELETE FROM doadores WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/doadores")


@main.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_doador(id):
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cep = request.form.get("cep")
        rua = request.form.get("rua", "")
        numero = request.form.get("numero", "")
        complemento = request.form.get("complemento", "")
        bairro = request.form.get("bairro", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")
        descricao = request.form.get("descricao", "")

        conn.execute(
            """UPDATE doadores 
            SET nome = ?, email = ?, cep = ?, rua = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, estado = ?, descricao = ?
            WHERE id = ?""",
            (nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao, id)
        )
        conn.commit()
        conn.close()

        return redirect("/doadores")

    doador = conn.execute(
        "SELECT * FROM doadores WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("editar.html", doador=doador)


@main.route("/perfil")
def perfil():
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()

    if session.get("tipo") == "admin":
        doacoes = conn.execute("SELECT * FROM doadores").fetchall()
    else:
        doacoes = conn.execute(
            "SELECT * FROM doadores WHERE usuario_id = ?",
            (session["usuario_id"],)
        ).fetchall()

    conn.close()

    return render_template("perfil.html", doacoes=doacoes)


@main.route("/relatorio")
def relatorio():
    if session.get("tipo") != "admin":
        return "Acesso negado"

    conn = get_connection()
    dados = conn.execute("""
        SELECT cep, COUNT(*) as total
        FROM doadores
        GROUP BY cep
    """).fetchall()
    conn.close()

    return render_template("relatorio.html", dados=dados)


@main.route("/logout")
def logout():
    session.clear()
    return redirect("/")