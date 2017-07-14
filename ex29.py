carros = ['bmw', 'land-rover', 'porsche', 'ferrari']
print('Vendedor - Seja bem vindo\n')

print('Comprador - Quantos carros tem na concessionária?')
print('Vendedor - Atualmente possuímos %s' %(len(carros)) + ' carros\n')

print('Comprador - Quais são os carros?')
print('Vendedor - Os carros são: {}\n'.format(carros).title())

print('Comprador - Eu gostei do desse {}'.format(carros[2]))
print('Comprador - Qual o preço dele?')
print('Vendedor - Ele está barato apenas R$500.000 hahaha')