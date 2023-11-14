#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
razao = int (input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(c, end= ' → ')
print('Acabou')


primeiro = int(input('Primeiro termo: '))
razao = int (input('Razão: '))