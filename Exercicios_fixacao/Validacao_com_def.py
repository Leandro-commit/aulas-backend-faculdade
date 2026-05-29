# Função para validar o tamanho de uma string
def validar(texto, minimo, maximo):

    # len() conta quantos caracteres existem no texto
    tamanho = len(texto)

    # Verifica se o tamanho está entre o mínimo e o máximo
    if minimo <= tamanho <= maximo:
        return True
    else:
        return False


# Entrada de dados do usuário
texto = input("Digite um texto: ")

minimo = int(input("Digite o tamanho mínimo: "))
maximo = int(input("Digite o tamanho máximo: "))


# Chamando a função
resultado = validar(texto, minimo, maximo)


# Exibindo o resultado
if resultado:
    print("String válida!")
else:
    print("String inválida!")
