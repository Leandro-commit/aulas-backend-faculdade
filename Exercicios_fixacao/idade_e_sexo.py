idade = int(input("Qual sua idade? "))

while idade > 0:
    sexo = input("Qual seu sexo (F ou M?) ").upper()

    if sexo == "M":
        print(f"Boa noite, senhor. Sua idade é {idade}.")
    elif sexo == "F":
        print(f"Boa noite, senhora. Sua idade é {idade}.")
    idade = int(input("Qual sua idade? "))
print("Idade negativa, encerrando...")
