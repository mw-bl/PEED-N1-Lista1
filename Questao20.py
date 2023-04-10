nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

nums.sort(reverse=True)
 
print("A lista em ordem decrescente é:", nums)
