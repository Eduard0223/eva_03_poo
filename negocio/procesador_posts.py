from servicios.api_posts import ApiPosts
from datos.crud_posts import guardar_posts, listar_posts
from auxiliares.constantes import DEFAULT_LIMIT

class ProcesadorPosts:
    @staticmethod
    def obtener_posts_guardar_y_listar(limit: int = DEFAULT_LIMIT):
        try:
            r = ApiPosts.get_posts()
            if r.status_code == 200:
                posts = r.json()
                guardar_posts(posts)
                return True, listar_posts(limit), "GET posts correcto. Guardado y consulta DB OK."

            if r.status_code == 404:
                return False, None, "GET posts falló: recurso no encontrado (404)."
            if r.status_code >= 500:
                return False, None, f"GET posts falló: error del servidor ({r.status_code})."

            return False, None, f"GET posts falló: status {r.status_code}."
        except Exception as e:
            return False, None, f"GET posts falló por excepción: {e}"
