nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

soma = sum(nums)

print("A soma dos números é:", soma)
