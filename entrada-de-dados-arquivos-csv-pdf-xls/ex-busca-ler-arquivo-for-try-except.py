import os
sair = "N"
#while sair != "S":
x = input("Digite o nome do arquivo: ")
for extensao in ["csv", "txt"]:
    try:
        nome = f"{x}.{extensao}"
        caminho = os.path.join(os.path.dirname(os.path.realpath(__file__)), nome)
        with open(caminho, "r") as arquivo:
            print(f"OK, buscarei por: {nome} no caminho:\n\t{caminho}\n")
            conteudo = arquivo.read()
            print(conteudo)
            break
    except FileNotFoundError:
        pass

else:
    print("Erro: Nenhum csv, txt foi encontrado")