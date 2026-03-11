A = int(input("Dame tu edad: "))
while A < 0:
    A = int(input("Dame tu edad: "))
if A < 3:
    print("Eres un bebe")
elif A < 12:
    print("Eres un niño")
elif A < 24:
    print("Eres un adolecente")
elif A < 60:
    print("Eres un adulto")
else:
    print("Eres un viejito")