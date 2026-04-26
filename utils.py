from functools import reduce

#* Linea mas importante (el acumulador)
def promedio_campo(usuarios, campo):
    if not usuarios:
        return 0
    total = reduce(lambda acc, u: acc + u[campo], usuarios, 0)
    return total / len(usuarios)

class usuarioError(Exception):
    pass


