import modulo_de_dados

fila = [[], []] #primeira lista pra quem é do grupo prioritario, e a segunda pra quem não é, já que na lista a prioridade é booleana

def adicionar_usuario_e_ordenar(matricula, hora_entrada, status, prioridade):
    if prioridade == "1":
        fila[0].append([matricula, hora_entrada, status, prioridade])
        fila[0].sort(key=lambda x: x[1])
    else:
        fila[1].append([matricula, hora_entrada, status, prioridade])
        fila[1].sort(key=lambda x: x[1])
    
    arquivo_fila = open('fila_espera.txt', 'w')
    arquivo_fila.write(str(fila))
    arquivo_fila.close()
    
    print(fila)
    
