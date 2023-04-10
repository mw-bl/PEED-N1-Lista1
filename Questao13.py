palavras = input("Digite uma lista de palavras separando-as por espaços: ")

palavras = palavras.split()

palavra_a = [ ]

for palavra in palavras:
    if palavra[0] == "a":
        palavra_a.append(palavra)

print("Palavras que começam com a:", palavra_a)
