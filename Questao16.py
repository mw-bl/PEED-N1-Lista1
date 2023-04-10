nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

num_pars = 0

for numero in nums:
    if int(numero) % 2 == 0:
        num_pars += int(numero)
 
print("A soma dos números pares da lista são:", num_pars)
