import requests
from auxiliares.constantes import API_BASE, HTTP_TIMEOUT

class ApiPosts:
    @staticmethod
    def get_posts():
        return requests.get(f"{API_BASE}/posts", timeout=HTTP_TIMEOUT)

    @staticmethod
    def post_post(data: dict):
        return requests.post(f"{API_BASE}/posts", json=data, timeout=HTTP_TIMEOUT)

    @staticmethod
    def put_post(post_id: int, data: dict):
        return requests.put(f"{API_BASE}/posts/{post_id}", json=data, timeout=HTTP_TIMEOUT)

    @staticmethod
    def delete_post(post_id: int):
        return requests.delete(f"{API_BASE}/posts/{post_id}", timeout=HTTP_TIMEOUT)
