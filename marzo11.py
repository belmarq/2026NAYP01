def solicitar_dimensiones(numero_matriz):
    while True:
        try:
            filas = int(input(f"Ingrese el número de filas de la matriz {numero_matriz}: "))
            columnas = int(input(f"Ingrese el número de columnas de la matriz {numero_matriz}: "))
            if filas <= 0 or columnas <= 0:
                print("Las dimensiones deben ser números positivos.")
                continue
            return filas, columnas
        except ValueError:
            print("Por favor ingrese números enteros válidos.")

def solicitar_matriz(filas, columnas, numero_matriz):
    matriz = []
    print(f"\nIngrese los datos de la matriz {numero_matriz}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Elemento [{i}][{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Por favor ingrese un número válido.")
        matriz.append(fila)
    return matriz

def multiplicar_matrices(matriz1, matriz2):
    filas1, columnas1 = len(matriz1), len(matriz1[0])
    filas2, columnas2 = len(matriz2), len(matriz2[0])
    
    resultado = []
    for i in range(filas1):
        fila = []
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print([f"{valor:.2f}" for valor in fila])

# Programa principal
filas1, columnas1 = solicitar_dimensiones(1)
filas2, columnas2 = solicitar_dimensiones(2)

if columnas1 != filas2:
    print(f"\nError: No se pueden multiplicar. Las columnas de la matriz 1 ({columnas1}) deben ser iguales a las filas de la matriz 2 ({filas2}).")
else:
    matriz1 = solicitar_matriz(filas1, columnas1, 1)
    matriz2 = solicitar_matriz(filas2, columnas2, 2)
    
    resultado = multiplicar_matrices(matriz1, matriz2)
    
    print(f"\nResultado de la multiplicación ({filas1}x{columnas2}):")
    mostrar_matriz(resultado)