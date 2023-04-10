nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

numpar = [ ]

for numero in nums:
    if numero % 2 == 0:
        numpar.append(numero)
        
print("O número par da lista é:", numpar)
