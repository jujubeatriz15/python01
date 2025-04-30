texto = "o rato roeu a roupa do rei de roma"
cont = 0
vogais= "aeiouAEIOU"
for x in range(len(texto)):
    if texto[x] in vogais:
       cont = cont+1
print(cont)