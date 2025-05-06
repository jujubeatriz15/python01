nums = ["","","","",""]
for i in range(len(nums)):
   nums[i] = int(input("digite os numeros: "))
print(nums)
numero = int(input("digite um numero para procurar: "))
cont = 0
for x in range(len(nums)):
   if numero == nums[x]:
       cont += 1
print(f"encontrei o {numero} que aparece {cont} vezes")