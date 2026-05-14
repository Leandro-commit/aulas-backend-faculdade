for i in range(3):
    nome = input(f"Nome do aluno {i + 1}: ")

    n1 = float(input("Sua nota em mátematica: "))
    n2 = float(input("Sua nota em português: "))
    n3 = float(input("Sua nota em ciências: "))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        print(f"{nome} foi aprovado com média {media:.2f}")
    else:
        print(f"{nome} foi reprovado com média {media:.2f}")

    print("-" * 30)
