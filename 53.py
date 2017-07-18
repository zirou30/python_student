lista = ['terra', 123, 'carro', 'moto']
nova_lista = lista
lista.append('pentest')

print(lista)
print(nova_lista)

'''
Foi feito a cópia fiel da lista origem em nova_lista
ambas recebem o mesmo valor pois se adicionando com
append na lista origem logo a nova_lista também receberá 
o mesmo valor é vice-versa.
'''