#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

num = int(input('Digite o número que quer ver a tabuada: '))
for c in range(1,11):
    print(f'{c}X{num} = {c*num}')