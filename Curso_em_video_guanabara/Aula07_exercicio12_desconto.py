preco = float(input("Qual o valor do produto: R$").replace(",", "."))
desconto = preco * 0.20
preco_final = preco - desconto
print(f"O preço com desconto de 20% será de R$ {preco_final:.2f}".replace(".", ","))

# Temos esse jeito de fazer também:

preço = float(input("qual o preço do produto? R$").replace(",", "."))
novo = preço - (preço * 50 / 100)
valor_formatado = f"{novo:.2f}".replace(".", ",")
print(f"O produto com desconto de 50% custará R$ {valor_formatado}")
