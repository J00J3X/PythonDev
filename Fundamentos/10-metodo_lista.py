filmsList = ["Inception", "The Shawshan Redemption",
             "The Dark Knigth", "Interstellar"]

# 1 - Tamanho da Lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo índice 
print(filmsList.index("Interstellar"))

# 3 - Adicionar item ao final da lista
filmsList.append("The lord of the Rings")
print(filmsList)

#4 - Ordenar a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Interstellar")
print(filmsCopy)

#6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)