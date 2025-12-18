from servicios.api_posts import ApiPosts
from servicios.api_comments import ApiComments
from datos.crud_posts import guardar_posts, listar_posts
from datos.crud_comments import guardar_comments, listar_comments
from auxiliares.constantes import DEFAULT_LIMIT

class ProcesadorPostsComments:
    @staticmethod
    def obtener_posts_y_comments_guardar_y_listar(limit: int = DEFAULT_LIMIT):
        try:
            rp = ApiPosts.get_posts()
            if rp.status_code != 200:
                return False, None, _msg_http("GET posts", rp.status_code)

            rc = ApiComments.get_comments()
            if rc.status_code != 200:
                return False, None, _msg_http("GET comments", rc.status_code)

            posts = rp.json()
            comments = rc.json()

            guardar_posts(posts)
            guardar_comments(comments)

            resultado = {
                "posts": listar_posts(limit),
                "comments": listar_comments(limit)
            }

            return True, resultado, "GET correcto. Posts y comments guardados y consultados desde DB."

        except Exception as e:
            return False, None, f"Error en GET/DB: {e}"

def _msg_http(nombre: str, status_code: int) -> str:
    if status_code == 404:
        return f"{nombre} falló: recurso no encontrado (404)."
    if status_code >= 500:
        return f"{nombre} falló: error del servidor ({status_code})."
    return f"{nombre} falló: status {status_code}."
