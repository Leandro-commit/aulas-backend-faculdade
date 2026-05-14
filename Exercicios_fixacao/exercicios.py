print("Digite uma mensagem que irei repetir para você!")
print('Para encerrar escreva "sair".')
texto = input("")
while texto != "sair":
    print(texto)
    texto = input("")
print("Encerrando o programa...")

####Verão alternativa####

print("Digite um mensagem que irei repetir para você!")
print('Para encerrar escreva "sair".')

while True:
    texto = input("")
    if texto == "sair":
        break
print("Encerrando o programa...")
