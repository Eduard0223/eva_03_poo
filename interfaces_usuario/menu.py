import re
import getpass

from negocio.seguridad import Seguridad
from datos.crud_usuarios import (
    crear_usuario,
    obtener_usuario_por_username,
    obtener_usuario_por_email
)
from negocio.procesador_posts_comments import ProcesadorPostsComments
from servicios.api_posts import ApiPosts
from servicios.api_comments import ApiComments
from auxiliares.constantes import DEFAULT_LIMIT



def mostrar_menu():
    print("""
1) Registro de usuarios
2) Login
3) GET: Obtener posts y comments desde API
4) POST: Crear (post o comment) en API
5) PUT: Actualizar (post o comment) en API
6) DELETE: Eliminar (post o comment) en API
0) Salir
""")

def _email_valido(email: str) -> bool:
    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(patron, email) is not None

def registrar_usuario():
    username = input("Username: ").strip()
    email = input("Email: ").strip()

    print("(La contraseña no se mostrará mientras escribes)")
    password = getpass.getpass("Password: ")

    if not username or not email or not password:
        print("Datos inválidos. Debe ingresar username, email y password.")
        return

    if not _email_valido(email):
        print("Email inválido. Ejemplo válido: usuario@correo.com")
        return

    try:
        # Validación extra (antes de insertar) para mensaje más claro
        if obtener_usuario_por_username(username):
            print("No se pudo registrar: el username ya existe.")
            return

        if obtener_usuario_por_email(email):
            print("No se pudo registrar: el email ya existe.")
            return

        password_hash = Seguridad.encriptar(password)
        crear_usuario(username, email, password_hash)
        print("Usuario registrado correctamente.")
    except Exception as e:
        print(f"No se pudo registrar el usuario: {e}")


def login() -> bool:
    username = input("Username: ").strip()

    print("(La contraseña no se mostrará mientras escribes)")
    password = getpass.getpass("Password: ")

    if not username or not password:
        print("Datos inválidos. Debe ingresar username y password.")
        return False

    try:
        row = obtener_usuario_por_username(username)
        if not row:
            print("Usuario no existe.")
            return False

        password_hash = row[3]  # id, username, email, password_hash
        if Seguridad.verificar(password, password_hash):
            print("Login correcto.")
            return True

        print("Credenciales incorrectas.")
        return False

    except Exception as e:
        print(f"Error en login: {e}")
        return False


def opcion_get_posts_comments():
    limit_str = input(f"Cantidad a mostrar desde DB (Enter = {DEFAULT_LIMIT}): ").strip()
    limit = DEFAULT_LIMIT
    if limit_str:
        try:
            limit = int(limit_str)
            if limit <= 0:
                limit = DEFAULT_LIMIT
        except ValueError:
            limit = DEFAULT_LIMIT

    ok, resultado, msg = ProcesadorPostsComments.obtener_posts_y_comments_guardar_y_listar(limit=limit)
    print(msg)
    if not ok:
        return

    posts = resultado["posts"]
    comments = resultado["comments"]

    print("\nPosts (DB):")
    for (pid, uid, title, _body) in posts:
        print(f"{pid} | userId={uid} | {title}")

    print("\nComments (DB):")
    for (cid, post_id, name, email, _body) in comments:
        print(f"{cid} | postId={post_id} | {name} | {email}")

def _elegir_tipo():
    print("\nSeleccione tipo de entidad:")
    print("1) Posts")
    print("2) Comments")
    op = input("Opción: ").strip()
    return op

def opcion_post():
    tipo = _elegir_tipo()

    if tipo == "1":
        title = input("title: ").strip()
        body = input("body: ").strip()
        user_id_str = input("userId: ").strip()

        if not title or not body or not user_id_str:
            print("Datos inválidos.")
            return

        try:
            user_id = int(user_id_str)
        except ValueError:
            print("userId debe ser un número.")
            return

        data = {"title": title, "body": body, "userId": user_id}
        try:
            r = ApiPosts.post_post(data)
            _mostrar_respuesta_http("POST posts", r.status_code, r)
        except Exception as e:
            print(f"Error POST posts: {e}")
        return

    if tipo == "2":
        post_id_str = input("postId: ").strip()
        name = input("name: ").strip()
        email = input("email: ").strip()
        body = input("body: ").strip()

        if not post_id_str or not name or not email or not body:
            print("Datos inválidos.")
            return

        try:
            post_id = int(post_id_str)
        except ValueError:
            print("postId debe ser un número.")
            return

        data = {"postId": post_id, "name": name, "email": email, "body": body}
        try:
            r = ApiComments.post_comment(data)
            _mostrar_respuesta_http("POST comments", r.status_code, r)
        except Exception as e:
            print(f"Error POST comments: {e}")
        return

    print("Opción inválida.")

def opcion_put():
    tipo = _elegir_tipo()

    if tipo == "1":
        post_id_str = input("ID del post a actualizar: ").strip()
        title = input("title nuevo: ").strip()
        body = input("body nuevo: ").strip()
        user_id_str = input("userId: ").strip()

        if not post_id_str or not title or not body or not user_id_str:
            print("Datos inválidos.")
            return

        try:
            post_id = int(post_id_str)
            user_id = int(user_id_str)
        except ValueError:
            print("ID y userId deben ser números.")
            return

        data = {"id": post_id, "title": title, "body": body, "userId": user_id}
        try:
            r = ApiPosts.put_post(post_id, data)
            _mostrar_respuesta_http("PUT posts", r.status_code, r)
        except Exception as e:
            print(f"Error PUT posts: {e}")
        return

    if tipo == "2":
        comment_id_str = input("ID del comment a actualizar: ").strip()
        post_id_str = input("postId: ").strip()
        name = input("name nuevo: ").strip()
        email = input("email nuevo: ").strip()
        body = input("body nuevo: ").strip()

        if not comment_id_str or not post_id_str or not name or not email or not body:
            print("Datos inválidos.")
            return

        try:
            comment_id = int(comment_id_str)
            post_id = int(post_id_str)
        except ValueError:
            print("IDs deben ser números.")
            return

        data = {"id": comment_id, "postId": post_id, "name": name, "email": email, "body": body}
        try:
            r = ApiComments.put_comment(comment_id, data)
            _mostrar_respuesta_http("PUT comments", r.status_code, r)
        except Exception as e:
            print(f"Error PUT comments: {e}")
        return

    print("Opción inválida.")

def opcion_delete():
    tipo = _elegir_tipo()

    if tipo == "1":
        post_id_str = input("ID del post a eliminar: ").strip()
        if not post_id_str:
            print("Debe ingresar un ID.")
            return
        try:
            post_id = int(post_id_str)
        except ValueError:
            print("El ID debe ser un número.")
            return

        try:
            r = ApiPosts.delete_post(post_id)
            _mostrar_respuesta_http("DELETE posts", r.status_code, r)
        except Exception as e:
            print(f"Error DELETE posts: {e}")
        return

    if tipo == "2":
        comment_id_str = input("ID del comment a eliminar: ").strip()
        if not comment_id_str:
            print("Debe ingresar un ID.")
            return
        try:
            comment_id = int(comment_id_str)
        except ValueError:
            print("El ID debe ser un número.")
            return

        try:
            r = ApiComments.delete_comment(comment_id)
            _mostrar_respuesta_http("DELETE comments", r.status_code, r)
        except Exception as e:
            print(f"Error DELETE comments: {e}")
        return

    print("Opción inválida.")

def _mostrar_respuesta_http(nombre: str, status_code: int, response):
    if status_code in (200, 201):
        print(f"{nombre} correcto. Status {status_code}.")
        try:
            print("Respuesta JSON:")
            print(response.json())
        except Exception:
            print("Respuesta sin JSON.")
        return

    if status_code == 404:
        print(f"{nombre} falló: recurso no encontrado (404).")
        return

    if status_code >= 500:
        print(f"{nombre} falló: error del servidor ({status_code}).")
        return

    print(f"{nombre} falló: status {status_code}.")
