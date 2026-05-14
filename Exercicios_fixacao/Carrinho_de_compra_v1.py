print("Olá, o que deseja comprar:")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Café R$ 4,00")
print("4 - Suco R$ 6,00")
print("5 - SAIR")

total = 0
while True:
    escolha = int(input("Qual item gostaria de comprar: "))

    if escolha == 1:
        qtd = int(input("Quantas unidades: "))
        total = total + qtd * 5.00

    elif escolha == 2:
        qtd = int(input("Quantas unidades: "))
        total = total + qtd * 7.00

    elif escolha == 3:
        qtd = int(input("Quantas unidades: "))
        total = total + qtd * 4.00

    elif escolha == 4:
        qtd = int(input("Quantas unidades: "))
        total = total + qtd * 6.00

    elif escolha == 5:
        print("Volte sempre...")
        break

    else:
        print("Produto inválido. Selecione outro. ")

print(f"\nTotal do pedido: {total}")
