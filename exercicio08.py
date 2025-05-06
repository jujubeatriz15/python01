nomes =["","","","",""]
senhas =["","","","",""]
for i in range(len(nomes)):
   nomes[i] = input("Digite um nome: ")
for x in range(len(senhas)):
   senhas[x] = input("Digite uma senha: ")
for y in range(len(nomes)):
   print(y, nomes[y], senhas[y])