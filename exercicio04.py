from biblioteca import estoque

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor unitario: "))
quantidade = int(input("quantos tem?: "))

print(estoque(nome,quantidade,valor))
