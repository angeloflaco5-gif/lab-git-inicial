def usuarios_mayores(usuarios):
    return [u for u in usuarios if u.es_mayor_de_edad()]

def promedio_edades_obj(usuarios):
    if not usuarios:
        return 0
    return  sum(u.edad for u in usuarios) / len(usuarios)

def usuarios_intensivos_obj(usuarios):
    return [u for u in usuarios if u.es_usuario_intensivo()]

#? REPORTES
REPORTES = {
    "1": ("Promedio de edades", promedio_edades_obj),
    "2": ("Usuarios mayores de edad", usuarios_mayores),
    "3": ("Usuarios intensivos", usuarios_intensivos_obj)
}