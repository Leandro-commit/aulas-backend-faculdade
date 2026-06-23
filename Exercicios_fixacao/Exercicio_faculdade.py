texto = "Bem-vindo a loja do Leandro Alves"
print(texto)
print("-" * len(texto))

valor = float(input("Entre com o valor do produto: "))
qtd = int(input("Entre com a quantiadde do produto: "))

soma = valor * qtd

if valor >= 2500 and valor < 6000:
    soma_com_desconto = soma - (soma * 0.04)
    print(f"Desconto de 4% concedido. Total com desconto: {soma_com_desconto:.2f}")
else:
    print(f"Total: {soma:.2f}")
