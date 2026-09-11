import cadastro
lista_de_usuarios = []
def modulo_de_dados():

    usuarios = cadastro.cadastrar()

    for usuario in usuarios:
        lista_de_usuarios.append(usuario)

    print(lista_de_usuarios)
