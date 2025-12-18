import hashlib

class Seguridad:
    @staticmethod
    def encriptar(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @staticmethod
    def verificar(password: str, hash_guardado: str) -> bool:
        return Seguridad.encriptar(password) == hash_guardado
