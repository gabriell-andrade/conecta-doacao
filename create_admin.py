from app.models import get_connection

conn = get_connection()

admin = conn.execute(
    "SELECT * FROM usuarios WHERE email = ?",
    ("admin@admin.com",)
).fetchone()

if admin:
    print("Admin já existe!")
else:
    conn.execute("""
        INSERT INTO usuarios (nome, sobrenome, email, senha, tipo)
        VALUES (?, ?, ?, ?, ?)
    """, ("Admin", "Sistema", "admin@admin.com", "123", "admin"))
    
    conn.commit()
    print("Admin criado com sucesso!")

conn.close()