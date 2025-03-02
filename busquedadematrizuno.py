# definir una de matriz
from enum import nonmember

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz,valor):
    # recorrer y buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j # retorna la posicion
    return None

# solicito el valor a buscar
numero_buscar=2

# llamo a la funciom
resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultodo del numero {numero_buscar} se encuentra en la posicion {resultado[0]}{resultado[1]} ")
else:
    print(f"el numero no se encontro en la matriz")






