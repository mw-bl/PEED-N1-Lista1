nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

numg = ""

for numero in nums:
    
    if len(numero) > len(numg):
        
        numg = numero
        
print("O maior número é:", numg)
