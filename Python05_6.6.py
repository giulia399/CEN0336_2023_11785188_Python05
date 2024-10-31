#!/usr/bin/python
#Criando um dicionario com minhas coisas favoritas

fav_dict = {
     "livro": "Harry Potter e o cálice de fogo",
     "som": "O grilo",
     "arvore":"amoreira"
}

#adicionar um novo organismo em fav_dict

fav_dict['organismo'] = 'Cachorro'
fav_thing = 'organismo'

#Imprima as chaves de comando

print ("As chaves de comando:", list(fav_dict.keys()))

#Solicitaçãopara escolher uma chave

fav_thing = input("Escolher uma chave do dicionário: ")

# Verificando se a chave existe e imprimindo o valor correspondente
if fav_thing in fav_dict:
    print(f"O valor de '{fav_thing}' é: {fav_dict[fav_thing]}")
else:
    print("Chave não encontrada.")

