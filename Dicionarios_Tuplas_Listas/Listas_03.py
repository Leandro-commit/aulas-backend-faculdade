# Usando o range

mochila = ["Machado", "Camisa", "Bacon", "Abacate"]
for i in range(0, len(mochila)):
    for j in range(0, len(mochila[i])):
        print(mochila[i][j], end="")
    print()
