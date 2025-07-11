# Função de potência de um número
power = lambda num: num ** 2

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0

# Função que divide um número por outro
div_num = lambda x, y: x / y

# Função que invete uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(div_num(10,2))
print(div_num(60,2))
print(reverse_string("Python"))
print(reverse_string("C#"))

# Funcionalidades relacionadas aos filmes:
movies_list = ["Titanic", "The GodFather","Inception"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 5.0, 8.5],
    "Inception": [6.5, 7.0, 10.0],
}

# Função para calcular a média de avaliações de um filme

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

# Função que verifia se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list

# Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"

print(f"Média de Avaliação do filme Titanic: {average_rating('Titanic')}")
print(f"Inception está na lista? {check_movie('Inception')}")
print(f"{recommend_movie('Inception')}")