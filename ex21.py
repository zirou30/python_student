pessoas = ['João', 'Renata', 'Maria']

print('' + pessoas[2] + ' você nào pagou a conta, teremos que ti retirar')
pessoas[2] = 'Gabriela'

mesa = input('Você quer se juntar a mesa:')
if mesa == 'sim':
    print(pessoas)

print('' + pessoas[0] + ' você não pagou a conta, teremos que ti retirar')
pessoas[0] = 'Gabriel'
if mesa == 'sim':
    print(pessoas)