from app.models import get_connection

conn = get_connection()
conn.execute("""
INSERT INTO usuarios (nome, email, senha, tipo)
VALUES ('Admin', 'admin@admin.com', '123', 'admin')
""")
conn.commit()
conn.close()

print("Admin criado!")