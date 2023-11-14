#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre
# a media de idade do grupo
#qual é o nome do homem mais velho
# quantas mulheres têm menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range (1,5):
    print('f---- {p}ª PESSOA ----')
    nome = str (input('Nome: ')).strip() #strip serve para tirar os espaços
    idade = int (input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 +=1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos')
print(f'O homem maus velho tem {maioridadehomem} anos e se chama {nome}')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos')