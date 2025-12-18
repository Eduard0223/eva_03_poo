from datos.conexion_db import conectar

def guardar_comments(comments: list[dict]) -> int:
    if not comments:
        return 0

    conn = conectar()
    cur = conn.cursor()
    try:
        sql = """
        INSERT INTO comments (id, postId, name, email, body)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          postId=VALUES(postId),
          name=VALUES(name),
          email=VALUES(email),
          body=VALUES(body)
        """
        data = [(c["id"], c["postId"], c["name"], c["email"], c["body"]) for c in comments]
        cur.executemany(sql, data)
        conn.commit()
        return cur.rowcount
    finally:
        cur.close()
        conn.close()

def listar_comments(limit: int = 10):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, postId, name, email, body FROM comments ORDER BY id LIMIT %s",
            (limit,)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def listar_comments_por_post(post_id: int, limit: int = 10):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, postId, name, email, body FROM comments WHERE postId=%s ORDER BY id LIMIT %s",
            (post_id, limit)
        )
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()
