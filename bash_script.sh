#!/bin/bash

# Mostra o diretório atual
echo "Você está no diretório: $(pwd)"

# Gera uma lista com detalhes do conteúdo da pasta HOME
ls -la ~ > lista_HOME.txt

# Imprime a data atual na tela
echo "Data atual: $(date)"
