print("Bem vindo(a) ao convertedor de dinheiro!")
dinheiro = float(input("Quantos você tem na carteira? R$"))
cotacao = 5.13
dolar = dinheiro / cotacao
real_formatado = f"{dinheiro:.2f}".replace(".", ",")
dolar_formatado = f"{dolar:.2f}".replace(".", ",")
print(f"Com R${real_formatado} você pode comprar US${dolar_formatado}")

# Eu poderia simplesmente colocar cotacao = dinheiro / 5.13
