usuarios = ['paulo', 'renan', 'carlos', 'roger']
horario_atendimento = ["manhã",'meio dia','tarde','noite']

usuarios_manha = [usuarios[i] for i in range(len(usuarios)) if horario_atendimento[i] == 'manhã']
usuarios_meiodia = [usuarios[i] for i in range(len(usuarios)) if horario_atendimento[i] == 'meio dia']
usuarios_tarde = [usuarios[i] for i in range(len(usuarios)) if horario_atendimento[i] == 'tarde']
usuarios_noite = [usuarios[i] for i in range(len(usuarios)) if horario_atendimento[i] == 'noite']
print(f'''
usuarios manhã = {usuarios_manha[0]}
usuarios meio dia = {usuarios_meiodia[0]}
usuarios tarde = {usuarios_tarde[0]}
usuarios noite = {usuarios_noite[0]}
''')
