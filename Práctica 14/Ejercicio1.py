import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')

    
    coincidencia = patron.match(cadena)

    
    return bool(coincidencia)


print(es_codigo_empleado_valido("EMP123"))  # True
print(es_codigo_empleado_valido("EMP456"))  # True
print(es_codigo_empleado_valido("EMP7890"))  # False
print(es_codigo_empleado_valido("ABC123"))  # False
