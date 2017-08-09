nao_confirmado_usuarios = ['astrogildo', 'antedegomon', 'chapeleiro maluco']
confirmado_usuarios = []

while nao_confirmado_usuarios:
    usuarios_atuais = nao_confirmado_usuarios.pop()

    print('Verificando usuários: ' + usuarios_atuais.title())
    confirmado_usuarios.append(usuarios_atuais)

print('\n Usuário confirmados:')
for x in confirmado_usuarios:
    print(x.title())

'''
usa o loop while nos usuários não confirmados e utiliza
o método do python .pop() para remover os últimos da lista
depois usa .append para adicionar na lista vaiz [] e usa o 
for para lista esses usuários confirmados.
'''
