mercado = []

nome = input("Nome do item: ")
qtd = int(input("Quantidade: "))
valor = float(input("Valor: "))
mercado.append([nome, qtd, valor])
print(mercado)


# Forma mais moderna de adicionar a lista:

# frutas = {"Nome": nome, "Quantidade": qtd, "Valor": valor}
# mercado.append(frutas)
# print(f"Nome: {frutas['Nome']}\nQuantidade: {frutas['Quantidade']}\nValor: {frutas['Valor']}")

soma = 0
print("Lista de compras:")
print("-" * 20)
print("item | quantidade | valor unitário | total do item")
for item in mercado:
    print("{} | {} | {} | {}".format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print("-" * 20)
print(f"Total a ser pago: {soma}")
