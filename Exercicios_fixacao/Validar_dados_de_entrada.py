# valor = int(input("Digite um número: "))

# while valor <= 0:
#     print("Digite um número válido")
#     valor = int(input("Digite um número acima de 0: "))


while True:
    try:
        valor = int(input("Digite um número: "))

        if valor <= 0:
            print("Digite um número positivo")
            continue
        break

    except ValueError:
        print("Insira apenas números!")
        continue
