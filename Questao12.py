nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

numimpar = [ ]

for numero in nums:
    if numero % 2 == 1:
        numimpar.append(numero)
        
print("O número impar da lista é:", numimpar)
