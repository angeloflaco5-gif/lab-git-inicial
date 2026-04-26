## corregir reporte 2 y 3 usuario intensivos y mayores de edad no muestra los usuarios solo muestra edad y horas
** METODOS ESPECIALES **
__str__() -> represenatcion para el usuraio final
__repr__() -> representacio para el developer (debug)
__eq__() -> comparar usuarios
__len__() -> retorne horas o edad
__bool__() -> si el usurio esa activo
__gt__() -> 


def __gt__(self, other):
    return self.horas > other

usuarios_ordenados = sorted(usuarios)

def nivel_actividad(self):
    if self.horas >= 50:
        return "Ultra activo"
    elif self.horas >= 25:
        return "Activo"
    else:
        return "casual"

@property
def edad_en_meses(self):
    return self.edad * 12

def check_password(self, pwd):
    return self.__password