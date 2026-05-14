valor = int(input("Digite o valor: "))

cont100 = valor // 100
valor = valor % 100

cont50 = valor // 50
valor = valor % 50

cont20 = valor // 20
valor = valor % 20

cont10 = valor // 10
valor = valor % 10

cont5 = valor // 5
valor = valor % 5

cont2 = valor

print(f"Cédulas de R$ 100,00 usadas: {cont100}")
print(f"Cédulas de R$ 50,00 usadas: {cont50}")
print(f"Cédulas de R$ 20,00 usadas: {cont20}")
print(f"Cédulas de R$ 10,00 usadas: {cont10}")
print(f"Cédulas de R$ 5,00 usadas: {cont5}")
print(f"Cédulas de R$ 2,00 usadas: {cont2}")
