from datos.conexion_db import conectar

def crear_usuario(username: str, email: str, password_hash: str) -> None:
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO usuarios(username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def obtener_usuario_por_username(username: str):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, username, email, password_hash FROM usuarios WHERE username=%s",
            (username,)
        )
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def obtener_usuario_por_email(email: str):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, username, email, password_hash FROM usuarios WHERE email=%s",
            (email,)
        )
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
