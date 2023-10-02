#desenvolva um programa que pergunte a distância de uma viagem em km
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
#e R$0,45 para viagens mais longas

viagem = float(input('Qual a distância da viagem: '))
#p1 = 200 *0.5
if viagem <=200:
    print(f'o valor da passagem será R${viagem * 0.5:.2f}')
else:
    print(f'o valor da passagem será R${viagem * 0.45:.2f}')