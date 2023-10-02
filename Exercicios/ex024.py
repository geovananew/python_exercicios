#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com SANTO

cidade = str(input('Nome da cidade: ')).strip()
print(cidade[:5].upper()== 'SANTO') #usa o :5 pois quer identificar se começa com santo ou seja entre as 5 primeiras letras