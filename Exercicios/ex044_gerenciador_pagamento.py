#elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#[1] à vista dinheiro/cheque: 10% de desconto;
#[2] à vista no cartão: 5% de desconto;
#[3] em até 2x no cartão: preço normal;
#[4] 3x ou mais no cartão: 20% de juros

preço = float(input('Qual é o preço do produto? '))
print('''FORMA DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2X no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2X de R${parcela:.2f} SEM JUROS')
elif opcao ==4:
    total = preço + (preço * 20/100)
    qtdparc = int(input('Quantas parcelas?'))
    parcela = total / qtdparc
    print(f'Sua compra será parcelada em {qtdparc}X de R${parcela:.2f} COM JUROS' )
else:
    print('Opçao de pagamento inválida. Tente novamente!')
print(f'sua compra de R${preço} vai custar R${total} no final')

