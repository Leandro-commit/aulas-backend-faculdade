numero = int(input("Qual número quer a tabuada: "))

print(f"TABUADA DO {numero}")

for i in range(1, 11):
    print(f"{numero} x {i} = {i * numero}")
