import Criar_funcao_de_fila
import Situacoes_da_fila
import Modulos_de_consulta

Situacoes_da_fila.carregar_dados()

us1 = Criar_funcao_de_fila.adicionar_usuario_e_ordenar(
    "1",
    "08:00",
    "Aguardando",
    1
)

us2 = Criar_funcao_de_fila.adicionar_usuario_e_ordenar(
    "2",
    "08:10",
    "Aguardando",
    0
)

fila = Criar_funcao_de_fila.fila

posicao = Modulos_de_consulta.buscar_posicao(
    fila,
    "1"
)

print(f"Posição do usuário 1:  {posicao}   ")

situacao = Modulos_de_consulta.consultar_situacao(
    fila,
    "1"
)

print(situacao["texto"])
