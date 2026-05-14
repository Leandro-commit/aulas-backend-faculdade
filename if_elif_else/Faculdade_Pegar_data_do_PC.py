from datetime import datetime

nasc = int(input("Em que ano você nasceu? "))
ano = datetime.now().year

if nasc >= ano:
    print("Ano inválido")
else:
    idade = ano - nasc
    print("Sua idade é", idade)

if idade >= 18:
    print("Você já pode tirar habilitação!")
else:
    print("Menores de 18 anos não podem tirar habilitação!")
