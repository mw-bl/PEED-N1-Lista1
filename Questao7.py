palavras = input("Digite uma lista de palavras separandos-as por espaços: ")

palavras = palavras.split()

pg = ""

for palavra in palavras:
    
    if len(palavra) > len(pg):
        
        pg = palavra
        
print("A palavra mais longa é:", pg)
