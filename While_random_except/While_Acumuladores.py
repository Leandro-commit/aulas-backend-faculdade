soma = 0
cont = 1
while cont <= 5:
    x = float(input(f"Digite a {cont}a nota: "))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f"Média final: {media}")
