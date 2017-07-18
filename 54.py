frutas = ['laranja', 'uva', 'manga', 'morango']
frutas_amigos = frutas[:]
frutas.append('tomate')
frutas_amigos.append('pêra')

print("Frutas que eu gosto:")
for fruta in frutas:
    print(fruta.title())
print()
print('Frutas que meus amigos gosta:')
for fruta_amigo in frutas_amigos:
    print(fruta_amigo.title())