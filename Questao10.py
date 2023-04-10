nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [float(numero) for numero in nums]

soma = sum(nums)
media = soma / len(nums)

print("A média dos números é: ", media)
