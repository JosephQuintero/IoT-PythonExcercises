#Escribe el código necesario para capturar una cadena de texto y definir una función para que determinar si es una dirección de correo electrónico valida.
import re

# Capturar la cadena de texto
correo = input("\nIngresa una dirección de correo electrónico: ")

# Función para validar si la cadena es una dirección de correo electrónico válida
def es_correo_valido(cadenaCorreo):
    # Expresión regular para validar el correo
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Verificar si la cadena cumple con el patrón de un correo válido
    if re.match(patron, cadenaCorreo):
        return True
    else:
        return False

# ----------------IMPRESION--------------------------
resultado = es_correo_valido(correo)
print(f"El correo es válido: {resultado}")