idade = int(input("Qual sua idade? "))

while idade > 0:
    sexo = input("Qual seu sexo (F ou M)? ").upper()
    while sexo not in ("F", "M"):
        print("Sexo inválido!")
        sexo = input("Qual seu sexo (F ou M)? ").upper()

    if sexo == "F":
        print(f"Boa noite, senhora, sua idade é {idade}.")
    else:
        print(f"Boa noite, senhor, sua idade é {idade}.")
    idade = int(input("Qual sua idade? "))

print("Idade negativa. Encerrando...")
