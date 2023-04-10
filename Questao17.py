nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

num_impars = 0

for numero in nums:
    if int(numero) % 2 == 1:
        num_impars += int(numero)
 
print("A soma dos números impares da lista são:", num_impars)
