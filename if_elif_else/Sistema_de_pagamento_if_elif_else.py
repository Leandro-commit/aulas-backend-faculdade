compra = float(input("Valor da compra: ").replace(",", "."))
print("-" * 30)
print("Aceitamos as seguintes formas de pagamento:")
print("-" * 30)
print("1. Dinheiro/Pix -> 10% de desconto")
print("-" * 30)
print("2. Cartão à vista -> 5% de desconto")
print("-" * 30)
print("3. Cartão parcelado:\n\nAté 2x -> Sem juros\n3x ou mais -> 20% de juros")
print("-" * 30)


pgt = int(input("Selecione a forma de pagamento: "))

if pgt < 1 or pgt > 3:
    print("Opção inválida!")


elif pgt == 1:
    desconto = compra * 0.10

elif pgt == 2:
    desconto = compra * 0.05

elif pgt == 3:
    parcelas = int(input("Quantas parcelas: "))
    if parcelas <= 2:
        print("Sem juros!")
        compra_replace = f"{compra:.2f}".replace(".", ",")
        print(f"Valor total: R$ {compra_replace}")
    else:
        desconto = compra * 0.20
        acrescimo = compra + desconto
        desconto_replace = f"{desconto:.2f}".replace(".", ",")
        acrescimo_replace = f"{acrescimo:.2f}".replace(".", ",")
        print(f"Juros aplicado: R$ {desconto_replace}")
        print(f"Valor total: R$ {acrescimo_replace}")

if pgt > 0 and pgt <= 2:
    valor_final = compra - desconto

    desconto_replace = f"{desconto:.2f}".replace(".", ",")
    valor_replace = f"{valor_final:.2f}".replace(".", ",")
    print(f"Desconto: R$ {desconto_replace}")
    print(f"Total a pagar: R$ {valor_replace}")
