# # Exemplo 1
# def omelete():
#     ovos = 12  # variável local


# # Programa principal
# omelete()
# print(ovos)  # escopo global

# ---------------------------------


# Exemplo 2
def omelete():
    print(ovos)  # escopo local


# Programa principal
ovos = 12  # variável global
omelete()
