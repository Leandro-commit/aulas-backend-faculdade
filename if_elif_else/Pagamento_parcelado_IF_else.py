def moeda(valor):
    return f"{valor:.2f}".replace(".", ",")


valor = float(input("Qual o valor da compra: "))
print("-" * 30)
print("1. Pagamento à vista -> Desconto 5%")
print("2. Pagamento em 3x -> Sem acréscimo")
print("3. Pagamento em 5x -> Acréscimo de 2%")
print("4. Pagamento em 10x -> Acréscimo de 8% \n")
pgt = int(input("Selecione a forma de pagamento: "))
print("-" * 30)

if pgt == 1:
    total = valor - (valor * 0.05)
    print(f"Valor original: {moeda (valor)}")
    print(f"Valor com desconto: {moeda (total)}")

elif pgt == 2:
    total = valor / 3
    print(f"Valor total: {moeda(valor)}")
    print(f"Valor parcelado: 3x de {moeda(total)}")

elif pgt == 3:
    total = valor + (valor * 0.02)
    parcela = total / 5
    print(f"Valor total: {moeda(total)}")
    print(f"Valor parcelado: 5x de {moeda (parcela)}")

elif pgt == 4:
    total = valor + (valor * 0.08)
    parcela = total / 10
    print(f"Valor total: {moeda (total)}")
    print(f"Valor parcelado: 10x de {moeda(parcela)}")

else:
    print("A opção escolhida é inválida")
