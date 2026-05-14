n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador ( +| - | * | / ): ")

if operador not in ["+", "-", "*", "/"]:
    print("Operador inválido")
elif operador == "+":
    conta = n1 + n2
elif operador == "-":
    conta = n1 - n2
elif operador == "*":
    conta = n1 * n2
elif operador == "/":
    if n2 == 0:
        print("Erro: Divisão por zero")
    else:
        conta = n1 / n2

print("O resultado é", int(conta) if conta == int(conta) else conta)
