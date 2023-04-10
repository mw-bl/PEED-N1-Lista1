nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

num_mn5 = [ ]

for numero in nums:
    if float(numero) < 5:
        num_mn5.append(numero)
 
print("Os números menores que 5 da lista são:", num_mn5)
