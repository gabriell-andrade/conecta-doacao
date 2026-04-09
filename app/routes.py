from flask import Blueprint, render_template, request, redirect, session, url_for
from .models import get_connection
import os
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def verificar_login():
    return session.get("usuario_id") is not None


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload_foto", methods=["POST"])
def upload_foto():
    if not verificar_login():
        return redirect("/login")
    
    if 'foto' not in request.files:
        return redirect("/perfil")
    
    file = request.files['foto']
    
    if file.filename == '':
        return redirect("/perfil")
    
    if file and allowed_file(file.filename):
        filename = secure_filename(f"user_{session['usuario_id']}_{file.filename}")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        conn = get_connection()
        conn.execute(
            "UPDATE usuarios SET foto_perfil = ? WHERE id = ?",
            (f"/static/uploads/{filename}", session['usuario_id'])
        )
        conn.commit()
        conn.close()
        
        session['foto_perfil'] = f"/static/uploads/{filename}"
    
    return redirect("/perfil")


@main.route("/login", methods=["GET", "POST"])
def login():
    erro = None

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
            session["sobrenome"] = user["sobrenome"]
            session["foto_perfil"] = user["foto_perfil"]

            return redirect("/")
        else:
            return redirect("/login?erro=1")

    return render_template("login.html")


@main.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
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
            """INSERT INTO usuarios 
            (nome, sobrenome, email, senha, tipo, foto_perfil) 
            VALUES (?, ?, ?, ?, 'user', NULL)""",
            (nome, sobrenome, email, senha)
        )
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("cadastro.html")


@main.route("/doadores", methods=["GET", "POST"])
def cadastrar_doador():
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()

    if request.method == "POST":
        nome = f"{session.get('nome')} {session.get('sobrenome')}"
        email = session.get("email")
        cep = request.form.get("cep")
        rua = request.form.get("rua", "")
        numero = request.form.get("numero", "").strip()
        complemento = request.form.get("complemento", "")
        bairro = request.form.get("bairro", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")
        descricao = request.form.get("descricao", "")
        usuario_id = session.get("usuario_id")

        if not numero or numero.upper() == "S/N":
            numero = "S/N"

        conn.execute(
            """INSERT INTO doadores 
            (usuario_id, nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao, status) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pendente')""",
            (usuario_id, nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao)
        )
        conn.commit()
        conn.close()
        
        return render_template("doadores.html", sucesso="Cadastro de doação realizada com sucesso. Obrigado!")

    conn.close()
    return render_template("doadores.html")


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
        numero = request.form.get("numero", "").strip()
        complemento = request.form.get("complemento", "")
        bairro = request.form.get("bairro", "")
        cidade = request.form.get("cidade", "")
        estado = request.form.get("estado", "")
        descricao = request.form.get("descricao", "")

        if not numero or numero.upper() == "S/N":
            numero = "S/N"

        conn.execute(
            """UPDATE doadores 
            SET nome = ?, email = ?, cep = ?, rua = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, estado = ?, descricao = ?
            WHERE id = ?""",
            (nome, email, cep, rua, numero, complemento, bairro, cidade, estado, descricao, id)
        )
        conn.commit()
        conn.close()

        return redirect("/perfil")

    doador = conn.execute(
        "SELECT * FROM doadores WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("editar.html", doador=doador)


@main.route("/excluir_doador/<int:id>")
def excluir_doador(id):
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()
    conn.execute("DELETE FROM doadores WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/perfil")


@main.route("/excluir_doacao/<int:id>")
def excluir_doacao(id):
    if not verificar_login():
        return redirect("/login")
    
    if session.get("tipo") != "admin":
        return "Acesso negado"
    
    conn = get_connection()
    conn.execute("DELETE FROM doadores WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect("/perfil")


@main.route("/perfil")
def perfil():
    if not verificar_login():
        return redirect("/login")

    conn = get_connection()

    cidade = request.args.get("cidade", "")
    cep = request.args.get("cep", "")
    nome = request.args.get("nome", "")

    if session.get("tipo") == "admin":
        query = "SELECT * FROM doadores WHERE 1=1"
        params = []
    else:
        query = "SELECT * FROM doadores WHERE usuario_id = ?"
        params = [session["usuario_id"]]

    if cidade:
        query += " AND cidade LIKE ?"
        params.append(f"%{cidade}%")
    if cep:
        query += " AND cep LIKE ?"
        params.append(f"%{cep}%")
    if nome:
        query += " AND nome LIKE ?"
        params.append(f"%{nome}%")

    doacoes = conn.execute(query, params).fetchall()
    conn.close()

    return render_template("perfil.html", doacoes=doacoes)


@main.route("/relatorio")
def relatorio():
    if session.get("tipo") != "admin":
        return "Acesso negado"

    conn = get_connection()
    
    cep = request.args.get("cep", "").replace("-", "")
    cidade = request.args.get("cidade", "")
    status = request.args.get("status", "")
    
    query = "SELECT * FROM doadores WHERE 1=1"
    params = []
    
    if cep:
        query += " AND REPLACE(cep, '-', '') LIKE ?"
        params.append(f"%{cep}%")

    if cidade:
        query += " AND cidade = ?"
        params.append(cidade)

    if status:
        query += " AND status = ?"
        params.append(status)
    
    query += " ORDER BY id DESC"
    
    doacoes = conn.execute(query, params).fetchall()

    cidades = conn.execute(
        "SELECT DISTINCT cidade FROM doadores ORDER BY cidade"
    ).fetchall()

    conn.close()

    return render_template("relatorio.html", doacoes=doacoes, cidades=cidades)


@main.route("/editar_status/<int:id>", methods=["POST"])
def editar_status(id):
    if session.get("tipo") != "admin":
        return "Acesso negado"
    
    novo_status = request.form.get("status")
    
    conn = get_connection()
    conn.execute("UPDATE doadores SET status = ? WHERE id = ?", (novo_status, id))
    conn.commit()
    conn.close()
    
    return redirect("/relatorio")


@main.route("/excluir_relatorio/<int:id>")
def excluir_relatorio(id):
    if session.get("tipo") != "admin":
        return "Acesso negado"
    
    conn = get_connection()
    conn.execute("DELETE FROM doadores WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect("/relatorio")


@main.route("/logout")
def logout():
    session.clear()
    return redirect("/")