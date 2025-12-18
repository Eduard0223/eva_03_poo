import requests
from auxiliares.constantes import API_BASE, HTTP_TIMEOUT

class ApiComments:
    @staticmethod
    def get_comments():
        return requests.get(f"{API_BASE}/comments", timeout=HTTP_TIMEOUT)

    @staticmethod
    def post_comment(data: dict):
        return requests.post(f"{API_BASE}/comments", json=data, timeout=HTTP_TIMEOUT)

    @staticmethod
    def put_comment(comment_id: int, data: dict):
        return requests.put(f"{API_BASE}/comments/{comment_id}", json=data, timeout=HTTP_TIMEOUT)

    @staticmethod
    def delete_comment(comment_id: int):
        return requests.delete(f"{API_BASE}/comments/{comment_id}", timeout=HTTP_TIMEOUT)
