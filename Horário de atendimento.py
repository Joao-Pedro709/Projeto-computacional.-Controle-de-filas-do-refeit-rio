horario_atendimento = ["6:00-7:00", "11:00-13:00", "15:00-16:00", "18:00-20:00"]

while True:
    escolha = input('''Qual turno voce deseja ver?
[1] Manhã
[2] Meio dia
[3] Tarde
[4] Noite
''')

    if escolha == "1":
        print(f"Manhã: {horario_atendimento[0]}")
        break

    elif escolha == "2":
        print(f"Meio dia: {horario_atendimento[1]}")
        break

    elif escolha == "3":
        print(f"Tarde: {horario_atendimento[2]}")
        break

    elif escolha == "4":
        print(f"Noite: {horario_atendimento[3]}")
        break

    else:
        print("Opção inválida!")
