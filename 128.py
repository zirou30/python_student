resposta = {}

while True:
    nome = input("Qual o seu nome? ")
    respostas = input('Qual montanha você gostaria de escalar?')

    resposta[nome] = respostas

    continuar = input('Outra pessoa gostaria de responder? (sim / não)').replace('ã', 'a')
    if continuar == 'nao':
        break

for chave, valor in resposta.items():
    print(chave.title() + ' gostaria de escalar no ' + valor.title() + '.')
