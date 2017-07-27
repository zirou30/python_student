coberturas_disponiveis = ['cogumelos', 'azeitonas', 'pimentão verde',
                          'calabresa', 'abacaxi', '4 queijos']

pedidos_pessoas = ['cogumelos', 'batatas fritas', '4 queijos']

for pedidos in pedidos_pessoas:
    if pedidos in coberturas_disponiveis:
        print('Adicionado ' + pedidos + '.')
    else:
        print('Não temos ' + pedidos + '.')

print('Pizza Pronta')
