ingressos = int(input("Quantos ingressos deseja? "))

total = 0
soma_idades = 0

for i in range(ingressos):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    soma_idades += idade  # soma todas as idades

    if idade < 3:
        preco = 0
    elif idade <= 12:
        preco = 15
    else:
        preco = 30

    total += preco

# cálculo da média
idade_media = soma_idades / ingressos

print(f"Total de ingressos: {ingressos}")
print(f"Média de idade: {idade_media:.2f}")
print(f"Total a pagar: R$ {total}")
