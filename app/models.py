import sqlite3

DATABASE = "database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            email TEXT UNIQUE,
            senha TEXT,
            tipo TEXT,
            foto_perfil TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS doadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            nome TEXT,
            email TEXT,
            cep TEXT,
            rua TEXT,
            numero TEXT,
            complemento TEXT,
            bairro TEXT,
            cidade TEXT,
            estado TEXT,
            descricao TEXT,
            status TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    conn.commit()
    conn.close()