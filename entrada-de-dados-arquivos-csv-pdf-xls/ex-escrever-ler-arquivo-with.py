sair = "N"

while sair != "S":
    nome = input("Digite o nome: ")
    cargo = input("Digite o cargo: ")
    tel = input("Digite o telefone sem DDD: ")
    with open("ucam.csv", "a", encoding = "utf-8") as arquivo:
        arquivo.write(f"{nome},{cargo},{tel}\n")
    sair = input("Digite S p/ SAIR ou Enter p/ continuar: ")
    sair = sair.upper()
with open("ucam.csv", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print(f"Programa finalizado\n{conteudo}")