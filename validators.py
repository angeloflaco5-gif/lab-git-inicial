class validatioError(Exception):
    pass

def validar_username(username: str):
    username = username.strip()
    if not username.strip():
        raise validatioError("username vacio")
    if len(username) < 3:
        raise validatioError("usuario muy corto")


def validar_password(password: str):
    if len(password) < 6:
        raise validatioError("la contraseña debe tener al menos 6 carateres")


def validar_edad(edad: int):
    if edad < 13:
        raise validatioError("no se permiten menores de 13 años")
    if edad > 120:
        raise validatioError("edad fuera d rango")


def validar_horas(horas: int):
    if horas < 0 or horas >200:
        raise validatioError("horas invalidas")


