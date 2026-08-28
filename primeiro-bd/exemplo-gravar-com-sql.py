#MVC
#Primeiro BD
import sqlite3
# Variáveis
nome: str = ""
telefone: str = ""
sair: str = "N"
#model
def GravarDados(nome, telefone):
    try:
        #criar bd se ñ existe e abrir bd
        conexao=sqlite3.connect("dados.db")
        #criar cursos (ponteiro) p/ criar, acessar tabelas
        cursor=conexao.cursor()
        #criar tabela clientes
        sql_criar_tabela = """
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(60),
            telefone VARCHAR(40)
        );
        """
        #executar cursor
        cursor.execute(sql_criar_tabela)
        print("create bem sucedido")
        #inserir registro
        sql_inserir="""INSERT INTO clientes (nome, telefone)
        VALUES (?, ?)"""
        cursor.execute(sql_inserir, (nome, telefone))
        # pesquisar pra que serve o commit, situação rollback cartao nao passa ao realizar compra online
        print("Linhas afetadas:", cursor.rowcount)
        conexao.commit()
        # fechar conexão
        cursor.execute("SELECT COUNT(*) FROM clientes")
        print("Total:", cursor.fetchone()[0])
        conexao.close()
    except sqlite3.Error as e:
        print("Erro:",e)

def ImprimirTabela():
    try:
        #criar bd se ñ existe e abrir bd
        conexao=sqlite3.connect("dados.db")
        #criar cursos (ponteiro) p/ criar, acessar tabelas
        cursor=conexao.cursor()
        #criar tabela clientes
        sql_criar_tabela = """
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(60),
            telefone VARCHAR(40)
        );
        """
        #executar cursor
        cursor.execute(sql_criar_tabela)
        #ler os registros retornados
        sql_imprimir="SELECT * FROM clientes"
        cursor.execute(sql_imprimir)
        print("select deu certo")
        registros = cursor.fetchall()
        print("\n--- CLIENTES ---")
        print("Quantidade:", len(registros))
        for registro in registros:
            print(f"ID: {registro[0]} | Nome: {registro[1]} | Telefone: {registro[2]}")
        # fechar conexão
        conexao.close()
    except sqlite3.Error as e:
        print("erro de dados, verifique",e)

#view

#controller
while sair != "S":
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    GravarDados(nome, telefone)
    sair = input("Sair S/N I-Imprimir: ")
    sair = sair.upper()
    if (sair=="I"):
        ImprimirTabela()
        sair = input("Sair S/N: ")
        sair = sair.upper()