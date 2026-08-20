import os
import pickle

# ===================================================

# ===================================================
NOME_ARQUIVO = "dados_fila.pkl"

SITUACOES_FILA = [
    "Aguardando",
    "Em Preparo",
    "Pronto",
    "Atendido",
    "Cancelado"
]

dados = []

# ===================================================

# ===================================================
def carregar_dados():
    global dados
    if os.path.exists(NOME_ARQUIVO):
        try:
            with open(NOME_ARQUIVO, "rb") as arq:
                dados = pickle.load(arq)
        except Exception:
            dados = []
    else:
        dados = []

def salvar_dados():
    try:
        with open(NOME_ARQUIVO, "wb") as arq:
            pickle.dump(dados, arq)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

# ===================================================
# ===================================================
carregar_dados()
 
item_fila = {
    "cliente": "João",
    "refeicao": "Prato Feito - Frango",
    "status": SITUACOES_FILA[1]
}
 
dados.append(item_fila)
salvar_dados()

# ===================================================

# ===================================================
print("\n===================================")
print("     DADOS DO ATENDIMENTO ")
print("===================================")
print(f"Cliente:   {item_fila['cliente']}")
print(f"Refeição:  {item_fila['refeicao']}")
print(f"Situação:  {item_fila['status']}")
print("===================================\n")
