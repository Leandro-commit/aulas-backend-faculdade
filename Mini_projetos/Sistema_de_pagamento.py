def moeda(valor):
    return f"{valor:.2f}".replace(".", ",")


# Entrada do valor da compra
while True:
    try:
        compra = float(input("Insira o valor da compra: ").replace(",", "."))
        break
    except ValueError:
        print("Digite um valor válido! (ex: 100 ou 99,90)")

print("-" * 30)
print("Aceitamos as seguintes formas de pagamento:")
print("-" * 30)
print("1. Dinheiro/Pix -> 10% de desconto")
print("2. Cartão à vista -> 5% de desconto")
print("3. Cartão parcelado:")
print("   Até 2x -> Sem juros")
print("   3x ou mais -> 20% de juros")
print("-" * 30)

while True:
    try:
        pgt = int(input("Selecione a forma de pagamento: "))
        if pgt in [1, 2, 3]:
            break
        else:
            print("Escolha 1, 2 ou 3.")
    except ValueError:
        print("Digite um número válido!")

if pgt == 1:
    desconto = compra * 0.10
    valor_final = compra - desconto
    print(f"Desconto: R$ {moeda(desconto)}")
    print(f"Valor total: R$ {moeda(valor_final)}")

elif pgt == 2:
    desconto = compra * 0.05
    valor_final = compra - desconto
    print(f"Desconto: R$ {moeda(desconto)}")
    print(f"Valor total: R$ {moeda(valor_final)}")

elif pgt == 3:
    while True:
        try:
            parcelas = int(input("Em quantas parcelas? "))
            if parcelas > 0:
                break
            else:
                print("Digite um número de parcelas válido!")
        except ValueError:
            print("Digite um número inteiro!")

    if parcelas <= 2:
        print("Sem juros!")
        print(f"Valor total: R$ {moeda(compra)}")
    else:
        juros = compra * 0.20
        total = compra + juros
        print(f"Juros aplicado: R$ {moeda(juros)}")
        print(f"Valor total: R$ {moeda(total)}")
