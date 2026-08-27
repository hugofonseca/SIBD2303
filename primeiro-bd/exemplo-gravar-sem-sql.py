# EXEMPLO ELABORADO SEM SQL
#MVC
#Primeiro BD
# Variáveis
nome: str = ""
telefone: str = ""
sair: str = "N"
#model
def GravarDados(nome, telefone):
    linha=f"{nome},{telefone}\n"
    arquivo = open("data.csv","a+")
    arquivo.write(linha)
    arquivo.close()
#view

#controller
if(__name__=="__main__"):
    while sair != "S":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        GravarDados(nome, telefone)
        sair = input("Sair S/N: ")
        sair = sair.upper()