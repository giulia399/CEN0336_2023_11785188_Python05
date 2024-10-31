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

fav_thing = input("Digite a chave que você deseja alterar: ")
if fav_thing in fav_dict:
    novo_valor = input(f"Digite o novo valor para {fav_thing}: ")
    fav_dict[fav_thing] = novo_valor
    print(f"Valor atualizado para {fav_thing}: {fav_dict[fav_thing]}")
else:
    print("Chave não encontrada.")
