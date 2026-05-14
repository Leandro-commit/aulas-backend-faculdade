while True:
    num = int(input("Digite um número: "))
    print(f"TABUADA DO {num}:")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    while True:
        continuar = input("Deseja outra (s/n)? ").lower()
        if continuar in ("s", "n"):
            break
        else:
            print("Digite uma entrada válida!")
    if continuar == "n":
        print("Encerrando...")
        break
