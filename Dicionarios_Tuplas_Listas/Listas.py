mochila = ["Machado", "Camisa", "Bacon", "Abacate"]

print("Lista: ", mochila)

# MANIPULANDO LISTAS

mochila.append("Ovos")  # Adiciona no final da lista

print("Lista: ", mochila)

mochila.insert(1, "Canivete")  # Insere na posição informada, insere no índice 1
print("Lista: ", mochila)

# PARA DELETAR

del mochila[1]  # Deleta o índice informado
print("Lista: ", mochila)

mochila.remove("Ovos")  # Deleta o dado informado
print("Lista: ", mochila)
