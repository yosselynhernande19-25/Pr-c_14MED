import re

def encontrar_palabras_minusculas(texto):
    
    palabras_encontradas = re.findall(r'\b[a-z]+\b', texto)

    return palabras_encontradas

texto_ejemplo = "Este es un Ejemplo de TEXTO con palabras en Minúsculas y MAYÚSCULAS."
palabras_en_minusculas = encontrar_palabras_minusculas(texto_ejemplo)

print("Palabras en minúsculas encontradas:", palabras_en_minusculas)
