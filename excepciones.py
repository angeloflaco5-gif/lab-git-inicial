# try:
#     edad = int(input("ingrese su edad"))
# except ValueError:
#     print("la edad debe ser numero")
    
    
def registro_usuario(usuarios):
    print("debug inicial")
    try:
        username = input("username: ")
        print("username ingresado",username)
        if any(u["username"] ==  username for u in usuarios):
            print(u"username")
            print("usuario ya existente")
            return

        password = input("password: ")
        edad = int(input("edad: "))
        horas = int(input("horas:"))

        if edad  <= 0 or horas <= 0:
            print("el valor ingresado no es valido")
            return

        usuarios.append({
            "username": username,
            "password": password,
            "edad": edad,
            "horas": horas
    })
        
        print("usuario registrado con exito")
        
    except ValueError:
        print("datos invalido intente de nuevo")


usuarios_1 =  [{
        "username": "admin",
        "password": "admin123",
        "edad": 30,
        "horas": 5
    }]

print(registro_usuario(usuarios_1))



