nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

num_m10 = [ ]

for numero in nums:
    if float(numero) > 10:
        num_m10.append(numero)
       
print("Os números maiores que 10 da lista são:", num_m10)
