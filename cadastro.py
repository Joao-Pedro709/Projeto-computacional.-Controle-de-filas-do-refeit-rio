def cadastrar():
    usuarios = []
    qntd_de_usuarios = 0

    while qntd_de_usuarios <= 0 or qntd_de_usuarios > 10:
        qntd_de_usuarios = int(input('Quantos usuários? (máximo 10): '))
        if qntd_de_usuarios > 10 or qntd_de_usuarios <= 0:
            print('Erro! Tente novamente.')

    while len(usuarios) < qntd_de_usuarios:
        listaAdd = input('Adicionar usuário: ').strip()
        while listaAdd == '':
            listaAdd = input('Nome inválido. Tente novamente: ').strip()
        usuarios.append(listaAdd)

    print('\nLista de alunos:')
    for usuario in usuarios:
        print(f'- {usuario}')

    return usuarios
    
