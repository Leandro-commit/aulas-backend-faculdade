soma_idade = 0
for i in range(4):
    idade = int(input(f"Usuário {i+1}: Qual sua idade? "))
    soma_idade += idade
media = soma_idade / 4
print(f"A soma das idades é: {soma_idade}")
print(f"A média das idades é: {media:.1f}")
