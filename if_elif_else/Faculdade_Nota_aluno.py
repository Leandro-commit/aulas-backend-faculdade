nome01 = input("Qual seu nome? ")
nota01 = float(input("Sua nota em matématica: "))
nota02 = float(input("Sua nota em português: "))
nota03 = float(input("Sua nota em ciências: "))

media = (nota01 + nota02 + nota03) / 3

if media >= 7:
    print(f"{nome01}, sua média foi {media:.2f} e você foi aprovado!")
else:
    print(f"{nome01}, sua média foi {media:.2f} e você foi reprovado!")
