import mysql.connector
from auxiliares.constantes import DB_CONFIG

def conectar():
    return mysql.connector.connect(**DB_CONFIG)
