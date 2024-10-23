#Practica 2

cadenaTexto = input("Ingresa una cadena de texto: ")

#1. Escribe una función que devuelva verdadero o falso si la primera letra de la cadena de texto es Mayuscula
def esMayuscula(cadena):
    if cadena[0].isupper(): # Verificar si la primera letra es mayúscula
        return True
    else:
        return False

resultado1 = esMayuscula(cadenaTexto)  

#2. Escribe una función que cuente las palabras que forman la cadena de texto.  
def contadorPalabras(cadena):
    totalPalabras = cadena.split() #Divide una cadena en una lista de palabras.
    return len(totalPalabras) #Cuenta el número de elementos en lista.

resultado2 = contadorPalabras(cadenaTexto)

#3. Escribe una función que reciba como argumento la cadena de texto y regrese una lista con las palabras que la forman.
def listaPalabras(cadena):
    return cadena.split()

resultado3 = listaPalabras(cadenaTexto)

#4. Escribe una función que regrese la cadena de texto invertida.
def invertirCadena(cadena):
    return cadena[::-1]

resultado4 = invertirCadena(cadenaTexto)

#5. Escribe una función que regrese la cadena original con la última letra de cada palabra en mayuscula.
def ultimaLetraMayuscula(cadena):
    palabras = cadena.split() #Dividimos la cadena en palabras
    resultado = []
    
    for palabra in palabras:
        nuevaPalabra = palabra[:-1] + palabra[-1].upper()
        resultado.append(nuevaPalabra)
    
    return ' '.join(resultado)
    #return ' '.join([palabra[:-1] + palabra[-1].upper() for palabra in cadena.split()])


resultado5 = ultimaLetraMayuscula(cadenaTexto)

#----------------IMPRESIONES--------------------------------------------
#1-Verificador de primer letra
print(f"\n¿La cadena comienza en mayuscula? {resultado1}")

#2-Contador de palabras
print(f"Total de palabras en la cadena: {resultado2}")

#3-Separador de palabras
print(f"Lista de palabras: {resultado3}")

#4-Invertir la cadena
print(f"Cadena invertida: {resultado4}")

#5-Ultima palabra en mayuscula
print(f"Ultima letra de cada palabra en mayuscula: {resultado5}")
