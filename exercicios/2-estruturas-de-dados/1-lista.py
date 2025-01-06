# Crie uma lista apenas com elementos numéricos
idades = [1, 3, 4, 6, 7, 11]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = [1, "oi", False, 1.09, 2j, 4, "Loren"]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_mista)
print(lista_mista[0])
print(lista_mista[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_mista[0:-1:2])

# Remova da lista o último item
lista_mista.pop()

# Insira na lista um novo item
lista_mista.append("Izzie")

# Remova da lista um item específico
lista_mista.remove("Izzie")
print(lista_mista)