nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

prodto = 1

for numero in nums:
    prodto *= int(numero)
 
print("O produto dos números, é:", prodto)
