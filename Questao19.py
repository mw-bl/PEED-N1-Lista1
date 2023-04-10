nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

nums.sort()
 
print("A lista em ordem crescente é:", nums)
