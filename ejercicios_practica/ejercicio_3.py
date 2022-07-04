# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función ordenar
def ordenar(lista):
    lista_menor_mayor = sorted(lista)

    return lista_menor_mayor

def ordenar_reverse(lista):
    lista_mayor_menor = sorted(lista, reverse= True)
    return lista_mayor_menor
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 10, 8, 12, 6]

    # Alumno: Crear la función "ordenar"

    # Generar una una nueva funcion que se llame "ordenar",
    # que utilizaremos para odernar la lista de numeros.
    # Debe recibir 1 parámetro que es la lista de números
    # y retornar la nueva lista ordenada (igual a lo visto en clase)

    # Dentro de la función puede ordenar la lista
    # usando la funciones nativas de Python "sorted"

    # Luego de crear la función invocarla en este lugar:

    lista_ordenada = ordenar(numeros)

    lista_ordenada_reverse = ordenar_reverse(numeros)

    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar:
    print(lista_ordenada)
    print(lista_ordenada_reverse)
    print("terminamos")
