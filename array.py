listaNomes = ['Pedro', 'Henrique', 'Carla', 'Samuel', 'Marcos']
nomeRequerido = 'Carla'
print(listaNomes[0])  # Acessa o primeiro elemento da lista
print(listaNomes[2])  # Acessa o terceiro elemento da lista
print(listaNomes[-1]) # Acessa o último elemento da lista
print ('__________________________________')

if nomeRequerido in listaNomes:
    print(f'{nomeRequerido} está na lista.')
else:
    print('O nome requerido não está na lista.')
