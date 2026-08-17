lista = []
while len(lista) < 10:
    listaAdd = str(input('adicionar usuario: '))
    if listaAdd != '':
        lista.append(listaAdd)
    else:
        while listaAdd == '':
            listaAdd = str(input('tente novamente: '))
print('lista de alunos')
for contador in range(10):
    print(f'{lista[contador]}, ', end='')