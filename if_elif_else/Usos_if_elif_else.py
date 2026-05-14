# print("1. Maça\n2. Laranja\n3. Banana")
# print("-" * 30)

# produto = int(input("Qual opção você deseja? "))
# qtd = int(input("Quantas unidades? "))

# if produto == 1:
#     pagar = qtd * 2.30
#     print(f"Total a pagar: R$ {pagar}")


# elif produto == 2:
#     pagar = qtd * 3.60
#     print(f"Total a pagar: R$ {pagar}")

# elif produto == 3:
#     pagar = qtd * 1.85
#     print(f"Total a pagar: R$ {pagar}")

# else:
#     print("Produto inexistente!")

# ***VERSÃO MELHORADA***

print("1. Maça\n2. Laranja\n3. Banana")
print("-" * 30)

produto = int(input("Qual opção você deseja? "))
qtd = int(input("Quantas unidades? "))

if produto == 1:
    pagar = qtd * 2.30

elif produto == 2:
    pagar = qtd * 3.60

elif produto == 3:
    pagar = qtd * 1.85

else:
    print("Produto inexistente!")
    pagar = None  # evita erro

# só imprime se for válido
if pagar is not None:
    pagar_formatado = f"{pagar:.2f}".replace(".", ",")
    print(f"Total a pagar: R$ {pagar_formatado}")
