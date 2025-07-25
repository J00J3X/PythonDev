filmInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imbRating": 9.9,
    "genre": ["Sci-fi", "Action", "Thriller"]
}
print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recupear um elemento do dicionário 
print(filmInception["genre"])
print(filmInception.get("imbdRating"))

# 2 - Buscar apenas as chaves do dicionário 
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionário 
print(filmInception.values())

# 4 - Buscar itens do dicionário com chave e valor
print(filmInception.items())

#5 - Adicionar itens no dicionário 
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# 6 - Atualizar itens no dicionário 
filmInception.update({"omdbRating":8.7})
print(filmInception)

# 7 - Remover item no dicionário 
filmInception.pop("director")
print(filmInception)
