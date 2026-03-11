while True:
    try:
        num = int(input("Dame un número: "))
        inverso = 1 / num
        break  
    except ValueError:
        print("Por favor introduce un número entero")
    except ZeroDivisionError:
        print("El cero no es una opción válida")
    except:
        print("Hubo un error")

print(f"El inverso de {num} es {inverso}")

# while True:
#     try:
#         num = int(input("De que número sera la tabla de multiplicar: "))
#         break
#     except ValueError:
#         print("Por favor introduce un número entero")
# iter = 0
# while iter < 11:
#     print(f"{num} * {iter} = {num*iter}")
#     iter = iter + 1