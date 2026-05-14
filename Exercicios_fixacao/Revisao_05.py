pin = 5050

while True:
    try:
        entrada = int(input("Digite a senha correta: "))

        if entrada == pin:
            print("Acesso permitido...")
            break
        else:
            print("Errado!")

    except ValueError:
        print("Digite apenas números!")
