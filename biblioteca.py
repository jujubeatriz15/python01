def imprimenome(nome):
    print(f"Nome: {nome}")
def solicitarnome():
    nome = input("Digite seu nome: ")
    return nome
def piramide(num):
    for x in range(1, num+1,1):
        for i in range(0,x):
            print(x ,end =" ")
        print()