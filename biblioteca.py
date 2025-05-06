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
def contavogais(texto):
    cont = 0
    vogais = "aeiouAEIOU"
    for x in range(len(texto)):
        if texto[x] in vogais:
            cont = cont + 1
    print(cont)
def estoque(produto, quantidade, valorUnitario):
    valorTotal = quantidade*valorUnitario
    print(valorTotal)
def numero(num):
    if num!= 0:
        if num > 0:
            return "P"
        else:
            return "N"
    else:
        return "Z"

def soma(a, b):
    result= a + b
    print(result)
def somacom_maisnumeros(*a):
    for x in range(len(a)):
        soma = soma+[x]
        print(soma)