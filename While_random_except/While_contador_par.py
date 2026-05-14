inicial = int(input("Qual o valor deseja iniciar a contagem? "))
final = int(input("Qual valor deseja encerrar a contagem? "))

x = inicial
while x <= final:
    # Abaixo vamos verificar se o número é par
    if x % 2 == 0:
        print(x)  # Print dentro do if
    x = x + 1
