num = int(input("De que número sera la tabla de multiplicar: "))
iter = 0
while iter < 11:
    print(f"{num} * {iter} = {num*iter}")
    iter = iter + 1
# for iter in range(11):  
#     print(f"{num} * {iter} = {num*iter}")

# citricos = ["naranja", "limon", "toronja", "mandarina", "sidra", "lima"]
# for index,item in enumerate(citricos):
#     print(f"indice: {index}, producto: {item}")

# a = float(input("Dame a: "))
# b = float(input("Dame b: "))
# c = float(input("Dame c: "))
# if a > b and a > c:
#     mayor = a
# elif b > a and b > c:
#     mayor = b
# else:
#     mayor = c
# print(f"El mayor de {a}, {b} y {c} es : {mayor}")