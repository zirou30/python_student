def qualquercoisa_com_br(primeiro_nome, ultimo_nome, nome_do_meio=''):  #cria a funcao com 3 argumentos
    if nome_do_meio: #Se a funcao tiver o nome do meio executa o bloco abaixo
        nome_completo = primeiro_nome + ' ' + nome_do_meio + ' ' + ultimo_nome
    else:   #Caso não tenha executa este bloco
        nome_completo = primeiro_nome + ' ' + ultimo_nome
    return nome_completo.title()    #retorna a variavel nome_completo

nome = qualquercoisa_com_br('poucas trancas', 'racha cuca') #chama a funcao com apenas 2 argumentos
print(nome) #mostra na tela

nome = qualquercoisa_com_br('quase nada', 'chapolin', 'seu madruga')    #chama a funcao com os 3 argumentos
print(nome) #mostra na tela
