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
print (fav_dict[fav_thing])

#Imprima as chaves de comando

print ("As chaves de comando:", list(fav_dict.keys()))

#Solicitaçãopara escolher uma chave

fav_thing = input("Escolher uma chave do dicionário: ")

#Alterando o valor do organismo

if fav_thing in fav_dict:
   fav_dict['organismo'] = 'Pinguim'


   #Novo valor
   novo_valor = input(f"Digite o novo valor para '{fav_thing}': ")

 fav_dict[fav_thing] = novo_valor
   print(f"Valor atualizado para '{fav_thing}': {fav_dict[fav_thing]}")

else:
   print (f"A chave '{fav_thing}' não existe no dicionário.")
