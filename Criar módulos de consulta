

def buscar_posicao(fila, identificador):
 
    for index, pessoa in enumerate(fila):
        if isinstance(pessoa, dict):
            if pessoa.get("id") == identificador or pessoa.get("nome") == identificador:
                return index + 1
        else:
            if pessoa == identificador:
                return index + 1
    return -1


def consultar_situacao(fila, identificador):

    posicao = buscar_posicao(fila, identificador)
    
    if posicao == -1:
        return {
            "identificador": identificador,
            "status": "Não encontrado",
            "posicao": None,
            "mensagem": "A pessoa informada não está na fila."
        }
    
    if posicao == 1:
        mensagem = "É a vez da pessoa! Próxima a ser atendida."
    else:
        pessoas_a_frente = posicao - 1
        mensagem = f"Aguardando atendimento. Há {pessoas_a_frente} pessoa(s) à frente."
        
    return {
        "identificador": identificador,
        "status": "Na fila",
        "posicao": posicao,
        "pessoas_a_frente": posicao - 1,
        "mensagem": mensagem
    }

if __name__ == "__main__":
 
    fila_exemplo = ["Ana", "Carlos", "Beatriz", "João"]

    print("--- Teste 1: Buscar Posição ---")
    pos_carlos = buscar_posicao(fila_exemplo, "Carlos")
    print(f"Posição do Carlos: {pos_carlos}º lugar")

    print("\n--- Teste 2: Consultar Situação ---")
    situacao_ana = consultar_situacao(fila_exemplo, "Ana")
    print(f"Ana: {situacao_ana['mensagem']}")

    situacao_beatriz = consultar_situacao(fila_exemplo, "Beatriz")
    print(f"Beatriz: {situacao_beatriz['mensagem']}")

    situacao_lucas = consultar_situacao(fila_exemplo, "Lucas")
    print(f"Lucas: {situacao_lucas['mensagem']}")
