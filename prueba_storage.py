# import sqlite3

# DB = "usuarios.db"

# def conectar():
#     return sqlite3.connect(DB)

# def crear_tabla_usuarios():
#     with conectar() as conn:
#         conn.execute("""
#             CREATE TABLE IF NOT EXISTS usuarios(    
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT UNIQUE,
#                 password TEXT,
#                 edad INTEGER,
#                 horas INTEGER
#             )
#                     """)
        

# def insertar_usuario(username,password,edad,horas):
#     with conectar() as conn:
#         conn.execute(
#             "INSERT INTO usuarios(username, password, edad, horas) VALUES(?, ?, ?, ?)",
#             (username, password, edad, horas)
#         )

# def obtener_usuario(username, password):
#     with conectar() as conn:
#         cursor = conn.execute(
#             "SELECT * FROM usuarios WHERE username = ? AND password = ?",
#             (username, password)
#         )
#         return cursor.fetchone()

#* como funciona sqlite 
#*SELECT -> selecionar | from(de)
#*INSERT -> insertar | to or into
#*CREATE -> crear
#*UPDATE -> actualizar
#*DELETE -> eliminar | WHERE (donde)

#? tipos de datos
#*
#*
#*
#*
#*
#*
#*
#*
#*
#*  (*)-> todo