nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida!")

elif nota <= 4.9:
    print("Reprovado")

elif nota <= 6.9:
    print("Recuperação")

elif nota <= 8.9:
    print("Aprovado")

elif nota <= 10:
    print("Excelente")
