#TODO MANEJAR USUARIOS
#TODO {"username": str, "password": str, "edad": int, "horas": int}
from storage import insertar_usuario, listar_usuarios_db, obtener_fila_por_username
from validators import validar_username, validar_password, validar_edad, validar_horas, validatioError
from models import Usuario
from security import hash_password, check_password

def registrar_usuario():
    print("registrar usuario")
    
    try:
        username = input("username : ").strip()
        password = input("password : ").strip()
        edad =int(input("edad: "))
        horas = int(input("horas: "))
        
        validar_username(username)
        validar_edad(edad)
        validar_horas(horas)
        validar_password(password)
        
        password = hash_password(password)
        insertar_usuario(username, password, edad, horas)
        print("usuario registrado con exito")
        
    except (ValueError, validatioError) as e:
        print("error: ", e)
        
    except Exception as e:
        print("error inesperado", e)


def obtener_todos_los_usuarios():
    filas = listar_usuarios_db()
    return [Usuario(f[0], f[1], f[2], f[3], f[4]) for f in filas]


def mostrar_usuarios():
    usuarios = obtener_todos_los_usuarios()
    if not usuarios:
        print("no hay usuarios regstrados")
        return 

    print("=== lista de usuarios ===")
    for u in usuarios:
        # __str__
        print(u)



def login(username, password):
    fila = obtener_fila_por_username(username)
    if not fila:
        return None
    
    u = Usuario(fila[0, fila[1], fila[2], fila[3],fila[4]])
    
    if check_password(password, u.get_password_hash()):
        return u

    return None



def obtener_lista_por_usuario(username):
    fila = obtener_fila_por_username(username)
    if not fila:
        return None
    return Usuario(fila[0], fila[1], fila[2], fila[3], fila[4])