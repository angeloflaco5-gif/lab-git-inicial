
# from storage import  guardar_usuarios,cargar_usuarios
from users import login,registrar_usuario, mostrar_usuarios,obtener_todos_los_usuarios
from storage import crear_tabla_usuarios
from reports import REPORTES


def menu():
    print("\n==== MENU ====")
    print("1. registrar usuario")
    print("2. mostrar usuarios")
    print("3. login")
    print("4. reportes")
    print("0. salir")

def menu_reportes():
    print("\n ==== REPORTES ====")
    for clave, (nombre, funcion) in REPORTES.items():
        print(f"{clave}. {nombre}")
    opcion = input("selecione un reporte: ").strip()

    usuarios = obtener_todos_los_usuarios()

    if opcion in REPORTES:
        nombre, fn = REPORTES[opcion]
        resultado = function(usuarios)
        print(f"resultado: {resultado}")
    else:
        print("opcion no valida")




def main():
    crear_tabla_usuarios()

    while True:
        menu()
        opcion = input(">>").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            user = login(input("user: "),input("pass: "))
            if user:
                print(user.mensaje_bienvenido())
            else:
                print("credenciales incorrectas")
        elif opcion == "4":
            menu_reportes()
        elif opcion == "0":
            break
        else:
            print("opcion no valida")
            



if __name__ == "__main__":
    main()

