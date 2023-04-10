nums = input("Digite uma lista de números separando-os por espaços: ")

nums = nums.split()

nums = [int(numero) for numero in nums]

mnum = nums[0]

for numero in nums:
    if numero < mnum:
        mnum = numero
        
print("O menor número da lista é:", mnum)
