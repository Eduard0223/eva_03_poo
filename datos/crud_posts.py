from datos.conexion_db import conectar

def guardar_posts(posts: list[dict]) -> int:
    if not posts:
        return 0

    conn = conectar()
    cur = conn.cursor()
    try:
        sql = """
        INSERT INTO posts (id, userId, title, body)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          userId=VALUES(userId),
          title=VALUES(title),
          body=VALUES(body)
        """
        data = [(p["id"], p["userId"], p["title"], p["body"]) for p in posts]
        cur.executemany(sql, data)
        conn.commit()
        return cur.rowcount
    finally:
        cur.close()
        conn.close()

def listar_posts(limit: int = 10):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, userId, title, body FROM posts ORDER BY id LIMIT %s",
            (limit,)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def obtener_post_por_id(post_id: int):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, userId, title, body FROM posts WHERE id=%s",
            (post_id,)
        )
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
