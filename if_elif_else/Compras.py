compra = float(input("Digite o valor da compra: ").replace(",", "."))

if compra <= 100:
    print("Desculpe! Compras até R$ 100,00 não tem direito a desconto!")

elif compra <= 200:
    desconto = compra * 10 / 100  # Ou ''Compra * 0.20''
    desconto_formatado = f"{desconto:.2f}".replace(".", ",")
    valor_final = compra - desconto
    valor_formatado = f"{valor_final:.2f}".replace(".", ",")
    print("Você obteve um desconto de 10%")
    print(f"Desconto em cima do valor: R$ {desconto_formatado}")
    print(f"Valor final da compra: R$ {valor_formatado} ")

else:
    desconto = compra * 20 / 100
    desconto_formatado = f"{desconto:.2f}".replace(".", ",")
    valor_final = compra - desconto
    valor_formatado = f"{valor_final:.2f}".replace(".", ",")
    print("Você obteve um desconto de 20%")
    print(f"Desconto em cima do valor: R$ {desconto_formatado}")
    print(f"Valor final da compra: R$ {valor_formatado}")
