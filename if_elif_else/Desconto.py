compra = float(input("Valor da compra: ").replace(",", "."))

desconto = 0

if compra <= 0:
    print("Não há compras!")

elif compra <= 100:
    print("Compras até R$ 100,00 não tem desconto!")

elif compra <= 200:
    desconto = compra * 0.10
    print("Desconto de 10% aplicado!")

else:
    desconto = compra * 0.20
    print("Desconto de 20% aplicado!")

if compra > 0:
    valor_final = compra - desconto

    desconto_formatado = f"{desconto:.2f}".replace(".", ",")
    valor_formatado = f"{valor_final:.2f}".replace(".", ",")

    print(f"Desconto: R$ {desconto_formatado}")
    print(f"Total a pagar: R$ {valor_formatado}")
