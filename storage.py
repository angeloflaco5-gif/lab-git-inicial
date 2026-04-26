# GUARDAR Y LEER LOS DATOS
# import json 
# import os

# FILE = "users.json"

# def cargar_usuarios():
#     if not os.path.exists(FILE):#? si la ruta o el archivo (file) no existe?
#         return []#? retorna una lista vacia
#     try:
#         with open(FILE, "r",encoding= "utf-8") as f: #?  read es Modo Lectura (encoding="utf-8")()
#             data = json.load(f)#* asignarle los datos (los usuarios) a data
#             if  isinstance(data, list):
#                 return data
#             return []
#     except (json.JSONDecodeError, OSError):
#             return []  #? Carga el archivo
    
# def guardar_usuarios(usuarios):
#     with open(FILE, "w") as f:
#         json.dump(usuarios, f, indent=4)

#?==== usuariso sqlite ====
import sqlite3
from validators import validar_horas
# from utils import usuarioError

DB = "usuarios.db"

def conectar():
    return sqlite3.connect(DB)

def crear_tabla_usuarios():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(    
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT,
                edad INTEGER,
                horas INTEGER
            )
            """)
        conn.commit()

def insertar_usuario(username,password,edad,horas):
    try:
        with conectar() as conn:
            conn.execute(
                "INSERT INTO usuarios(username, password, edad, horas) VALUES(?, ?, ?, ?)",
                (username, password, edad, horas)
            )
            conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("usuario duplicado")
    
    except sqlite3.OperationalError:
        raise RuntimeError("error interno con la base de datos")
    
    except sqlite3.OperationalError:
        raise RuntimeError("base de datos dañada")
    
    except sqlite3.OperationalError:
        raise RuntimeError("error interno con la base de datos")


def actualizar_horas(username, horas):
    validar_horas(horas)
    
    with conectar() as conn:
        conn.execute("""
                    UPDATE usuarios
                    SET horas = ?
                    WHERE username = ?
                    """,(horas, username))
        conn.commit()
        
        if conn.cursor.rowcount == 0:
            raise ValueError("usuario no encontrado, no se encontro nada")
        
def eliminar_usuario(username):
    with conectar() as conn:
        conn.execute("""
            DELETE usuarios
            WHERE usernane = ?
        """,(username))
        

def listar_usuarios_db():
    try:
        with conectar() as conn:
            cursor = conn.execute(
                "SELECT id, username, password, edad, horas FROM usuarios" 
                )
            return cursor.fetchall()
    except sqlite3.OperationalError as e:
        raise RuntimeError ("error en la base de datos",e) 

def obtener_fila_por_username(username):
    with conectar() as conn:
        cursor = conn.execute(
            "SELECT id, username, password, edad, horas FROM usuarios WHERE username = ?"
            (username,)
        )
        return cursor.fetchone
    
