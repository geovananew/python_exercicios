#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('preço do produto: R$'))
novo = preco - (preco*5/100)
print(f'o produto de R${preco} com o desconto de 5% ficará R${novo}')