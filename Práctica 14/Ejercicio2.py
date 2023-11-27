import re

def buscar_fecha(cadena):
    
    patron_fecha = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

    resultado_busqueda = re.search(patron_fecha, cadena)

    return resultado_busqueda is not None

cadena_ejemplo = "Hoy es 26/11/2023 y mañana será 27/11/2023."
resultado = buscar_fecha(cadena_ejemplo)

print(resultado)  # Salida: True
