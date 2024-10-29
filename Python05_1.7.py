#!/usr/bin/python
# Criando um dicionário com minhas coisas favoritas

fav_dict = {
    "livro": "Harry Potter e o Cálice de Fogo",
    "som": "O Grilo",
    "arvore": "Amoreira"
}

# Adicionar um novo organismo em fav_dict
fav_dict['organismo'] = 'Cachorro'
fav_thing = 'organismo'
print(f"O organismo favorito é: {fav_dict[fav_thing]}")

# Alterando o valor do organismo
if fav_thing in fav_dict:  # Verificar se a chave existe
    fav_dict[fav_thing] = 'Pinguim'  # Trocar o valor para 'Pinguim'

# Mostra o novo valor do organismo
print(f"O novo organismo favorito é: {fav_dict[fav_thing]}")

# Imprimindo todo o dicionário
print("\nConteúdo do dicionário:")
for key, value in fav_dict.items():
    print(f"{key}: {value}")


