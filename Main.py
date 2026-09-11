from time import sleep
import modulo_de_dados
import criar_funcao_de_fila

menu_decisao = ''
while menu_decisao != '0':
    sleep(1.0)
    menu = '''
    ╔═════════════════════════════════════════════════════════════════════╗
    ║ SISTEMA DE CONTROLE DE FILA - RU v1.0                               ║
    ╠═════════════════════════════════════════════════════════════════════╣
    ║ [1] Cadastrar [1.5] ver cadastros                                   ║
    ║ [2] Registrar Entrada na Fila (Com Checagem de Prioridade)          ║
    ║ [3] Realizar Atendimento / Registrar Refeição                       ║
    ║ [4] Relatório de Refeições Servidas por Turno                       ║
    ║ [5] Salvar e Carregar Dados do Arquivo (refeitorio.pkl / csv)       ║
    ║ [0] Sair do Sistema                                                 ║
    ╚═════════════════════════════════════════════════════════════════════╝
    '''
    print(menu)
    menu_decisao = input('digite a função: ').strip()

    if menu_decisao == '1':
        modulo_de_dados.modulo_de_dados()

    elif menu_decisao == '1.5':
        print(modulo_de_dados.lista_de_usuarios)

    elif menu_decisao == '2':
        a = input('Digite o nome do usuário: ')
        if a in modulo_de_dados.lista_de_usuarios:
            adicionarM = input("Digite a matrícula: ")
            adicionaH = int(input("Digite a hora de entrada: "))
            adicionarS = input("Digite o status: ")
            adicionarPr = input("Digite a prioridade: ")

            criar_funcao_de_fila.adicionar_usuario_e_ordenar(
                adicionarM, adicionaH, adicionarS, adicionarPr
            )
            print(criar_funcao_de_fila.fila)
        else:
            print("Usuário não encontrado nos cadastros.")
            
