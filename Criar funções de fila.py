
fila = []


def adicionar_usuario_e_ordenar(matricula,hora_entrada,status,prioridade):
    
    usuario = {
        "matricula": matricula,
        "hora_entrada": hora_entrada,
        "status": status,
        "prioridade": prioridade 
    }
    
    fila.append(usuario)
    fila.sort(key=lambda usuario: (not usuario["prioridade"], usuario["hora_entrada"]))
    print(fila)



while True:
    adicionarM= input("digite a matrícula")
    adicionarH= input("digite a hora de entrada")
    adicionarS= input("digite o status")
    adicionarPr= int(input("digite a prioridade"))
    adicionar_usuario_e_ordenar(adicionarM,adicionarH,adicionarS, adicionarPr)
