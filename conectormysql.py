import mysql.connector

def conectarDB():
    conector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="skyroute"
        )
    cursor = conector.cursor()
    return conector, cursor
