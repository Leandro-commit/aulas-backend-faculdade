def moeda(valor):
    return f"{valor:.2f}".replace(".", ",")


compra = float(input("Digite o valor da compra: R$ ").replace(",", "."))
print("-" * 30)
print("\nE. Eletrônicos")
print("V. Vestuário")
print("A. Alimentos\n")

categoria = input("Qual a categoria do produto? ").upper()

if categoria == "E":
    if compra <= 100:
        desconto = compra * 0.05
        print("Categoria: Eletrônicos")
        print("Faixa: Até R$ 100,00")
        print("Desconto: 5%")

    elif compra <= 500:
        desconto = compra * 0.10
        print("Faixa: de R$ 100,00 à R$ 500,00")
        print("Desconto: 10%")

    else:
        desconto = compra * 0.20
        print("Faixa: Acima de R$ 500,00")
        print("Desconto: 20%")
    print(f"Valor do desconto: R$ {moeda(desconto)}")
    print(f"Valor final: R$ {moeda(compra - desconto)}")

elif categoria == "V":
    if compra <= 100:
        desconto = compra * 0
        print("Categoria: Vestuário")
        print("Faixa: Até R$ 100,00")
        print("Sem desconto!")

    elif compra <= 500:
        desconto = compra * 0.05
        print("Categoria: Vestuário")
        print("Faixa: De R$ 100,00 à R$ 500,00")
        print("Desconto: 10%")

    else:
        desconto = compra * 0.10
        print("Categoria: Vestuário")
        print("Faixa: Acima de R$ 500,00")
        print("Desconto: 10%")
    print(f"Valor do desconto: R$ {moeda(desconto)}")
    print(f"Valor final: R$ {moeda(compra - desconto)}")

elif categoria == "A":
    if compra <= 100:
        desconto = compra * 0.02
        print("Categoria: Alimentos")
        print("Faixa: Até R$ 100,00")
        print("Desconto: 2%")
    elif compra <= 500:
        desconto = compra * 0.05
        print("Categoria: Alimentos")
        print("Faixa: De R$ 100,00 à R$ 500,00")
        print("Desconto: 5%")
    else:
        desconto = compra * 0.08
        print("Categoria: Alimentos")
        print("Faixa: Acima de R$ 500,00")
        print("Desconto: 8%")
    print(f"Valor do desconto: R$ {moeda(desconto)}")
    print(f"Valor final: R$ {moeda(compra - desconto)}")

else:
    print("Opção inválida")
