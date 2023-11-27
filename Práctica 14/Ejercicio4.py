import re

def encontrar_ocurrencias(texto, palabra):
    
    iterador_coincidencias = re.finditer(r'\b{}\b'.format(re.escape(palabra)), texto, re.IGNORECASE)

    ubicaciones_ocurrencias = [coincidencia.span() for coincidencia in iterador_coincidencias]

    return ubicaciones_ocurrencias


texto_ejemplo = "Este es un ejemplo de texto. La palabra ejemplo aparece varias veces en este ejemplo."
palabra_buscada = "ejemplo"

ocurrencias = encontrar_ocurrencias(texto_ejemplo, palabra_buscada)
print(f"Ubicaciones de la palabra '{palabra_buscada}': {ocurrencias}")
