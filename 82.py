idade = 12
if idade < 4:
    preco = 0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
else:
    preco = 5
print('Seu custo de admissão e R$' + str(preco) + '.')

'''
Foi adicionado mais bloco de instrução elif
para idades abaixo de 65. Se caso a idade for maior
que 18 e menor que 65 o bloco e executado, caso a idade
seja acima de 65 executa o último bloco else.
'''