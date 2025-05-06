n = int(input("digite um numero: "))
a = [""]
b = [""]
soma = [""]
for x in range(n):
   a[x] = int(input("Digite um valor: "))
for y in range(n):
   b[y] = int(input("Digite um valor: "))
for s in range(n):
   soma[s] = a[s] + b[s]
print(soma)