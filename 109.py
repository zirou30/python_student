vazio = []

for x in range(30):
    atributos = {'cor': 'verde', 'pontos': 2, 'velocidade': 'lento'}
    vazio.append(atributos)

for a in vazio[0:3]:
    if a['cor'] == 'verde':
        a['cor'] = 'preto'
        a['pontos'] = 7
        a['velocidade'] = 'rápido'

for a in vazio[0:5]:
    print(a)

'''
Criado a condição if na linha 8 o loop for
percorrer condição sendo Treu ele faz as alterações
da linha 8 até a 11
'''