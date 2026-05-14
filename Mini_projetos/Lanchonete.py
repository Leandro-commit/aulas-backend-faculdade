print("Olá, o que deseja comprar:")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Café R$ 4,00")
print("4 - Suco R$ 6,00")
print("5 - SAIR")

total = 0

while True:
    escolha = int(input("Qual item gostaria de comprar: "))

    if escolha == 5:
        print("Volte sempre...")
        break

    elif escolha not in (1, 2, 3, 4):
        print("Produto inválido.")
        continue

    qtd = int(input("Quantas unidades: "))

    if escolha == 1:
        preco = 5
    elif escolha == 2:
        preco = 7
    elif escolha == 3:
        preco = 4
    else:
        preco = 6

    total += qtd * preco

print(f"Total do pedido: R$ {total}")
