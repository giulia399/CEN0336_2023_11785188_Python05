
#Crie um conjunto usando as duas sintaxes diferentes para criar um conjunto, 
#myset = set() e myset2 = {}. Qual é a diferença? Importa como você cria o conjunto?
#!/usr/bin/python

# Criação dos conjuntos
mySet = set('ATGTGGG')  # Conjunto criado a partir de uma string
mySet2 = {'ATGCCT'}     # Conjunto criado usando a sintaxe literal

print("mySet:", mySet)
print("mySet2:", mySet2)


#Resposta 

resposta = (
    "Ao criar conjuntos, é importante usar set() se você deseja iniciar um conjunto vazio "
    "ou se você está criando um conjunto a partir de um iterável, e {} se você já estiver fornecendo elementos."
)

print(resposta)

