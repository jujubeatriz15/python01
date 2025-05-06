nomes =["daniel","julia","bruno","amora","manuel"]
senha =["354","872","364","635","546"]
senhas = input("Digite uma senha: ")
for i in range(len(nomes)):
   if senhas == senha[i]:
       print(f"login efetuado com sucesso {nomes[i]}.")