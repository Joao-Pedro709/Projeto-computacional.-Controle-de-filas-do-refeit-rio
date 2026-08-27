
fila = [[],[]]#primeira lista pra quem é do grupo prioritario, e a segunda pra quem não é, já que na lista a prioridade é booleana


def adicionar_usuario_e_ordenar(matricula,hora_entrada,status,prioridade):
    if prioridade == "1":
        fila[0].append([matricula,hora_entrada,status,prioridade])
        fila[0].sort(key=lambda x: x[1])#o sort usa o segundo elemento da sublista pra organizar em ordem de chegada
    else:
        fila[1].append([matricula,hora_entrada,status,prioridade])
        fila[1].sort(key=lambda x: x[1])
    print(fila)

   
while True:
    adicionarM= input("digite a matrícula")
    adicionarH= int(input("digite a hora de entrada"))
    adicionarS= input("digite o status")
    adicionarPr= input("digite a prioridade")
    adicionar_usuario_e_ordenar(adicionarM,adicionarH,adicionarS, adicionarPr)