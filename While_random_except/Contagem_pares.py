par = int(input("Digite um número par inicial: "))
while par % 2 != 0:
    print("Digite um número par!")
    par = int(input("Digite um número par inicial: "))

final = int(input("Digite o valor que deseja encerrar: "))

while par <= final:
    print(par)
    par = par + 2
