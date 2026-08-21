import os
caminho = os.path.join(os.path.dirname(os.path.realpath(__file__)), "familia.txt")
with open(caminho, "r") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        if "livia" in linha:
            print(f"Termo encontrado na linha {i+1}: {linha.strip()}")
