
#Creamos una variable que almacene nuestros datos de la lista
numeros = []

#Solicitamos al usuario una cantidad de números para ingresar
cantidad = int(input("Ingresa la cantidad de numeros que desea ingresar: "))

for i in range(cantidad):
    numero = int(input(f"Numero {i+1}: "))
    numeros.append(numero) #Añadimos los numeros a la lista

#Indice central
mitad = len(numeros) // 2

#Crear sublista de 2 elementos a partir de la mitad
sublista = numeros[mitad - 1:mitad + 1]

#En la lista original agrega los elementos de la lista al final de la misma.
duplicarlista = numeros.copy() # Esto duplica la lista
duplicarlista.extend(numeros) # .extend() repite la cadena deseada

#De la lista obtenida ordena los elementos de menor a mayor e imprime el resultado.
listaOrdenadaMenorMayor = sorted(numeros)

#Vuelve a ordenar sus elementos de mayor a menor e imprime su resultado.
listaOrdenadaMayorMenor = sorted(numeros, reverse=True)

#Escribe una función que devuelva el cubo de los elementos de la lista, e imprime el resultado.
def cubo_elementos(lista):
    return[x**3 for x in lista]
cubos = cubo_elementos(numeros)



#----------------IMPRESIONES--------------------------
#Imprimir la lista al final
print("Lista generada: ", numeros)
#Imprimir sublista de elementos
print("Sublista de la mitad de elementos: ", sublista)
#Imprimir lista con elementos de lista al final de lista.
print("Lista con numeros al final de la lista: ", duplicarlista)
#Imprimir la lista ordenada de menor a mayor
print(f"Lista ordenada de menor a mayor: {listaOrdenadaMenorMayor}")
#Imprimir la lista ordenada de mayor a menor
print(f"Lista ordenada de mayor a menor: {listaOrdenadaMayorMenor}")
#Imprimir el cubo de los elementos de la lista
print("Cubo de los elementos:", cubos)