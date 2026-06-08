mochila = ("Machado", "Camisa", "Bacon", "Abacate")

print(mochila[0])  # print do Elemento 1 - Índice 0
print(mochila[2])  # print do Elemento 3 - Índice 2
print(mochila[0:2])  # print dos elementos 1 e 2 - Índice 0 e 1
print(mochila[2:])  # print dos elementos a partir do índice 2
print(mochila[-1])  # print do último, sendo da direita pra esquerda

for item in mochila:
    print(f"Na minha mochila tem: {item}")
