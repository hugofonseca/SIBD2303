sair = "N"

while sair != "S":
    nome = input("Digite o nome: ")
    tel = input("Digite o telefone: ")
    # Gravar dados
    arquivo = open("dados.csv", "a+")
    arquivo.write(f"{nome},{tel}\n")
    arquivo.close
    sair = input("Digite S para SAIR ou Enter p/ continuar ")
    sair = sair.upper()
print("Programa finalizado")
