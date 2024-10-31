#!/usr/bin/python
# Definindo os conjuntos A e B
set_a = {3, 14, 15, 9, 26, 5, 35}
set_b = {60, 22, 14, 0, 9}

# Operações com conjuntos
intersecao = set_a.intersection(set_b)
diferenca = set_a.difference(set_b)
uniao = set_a.union(set_b)
diferenca_simetrica = set_a.symmetric_difference(set_b)

# Exibindo os resultados
print("Interseção:", intersecao)
print("Diferença (A - B):", diferenca)
print("União:", uniao)
print("Diferença Simétrica:", diferenca_simetrica)
