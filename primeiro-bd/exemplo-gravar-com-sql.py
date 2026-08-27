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
        sql_inserir="INSERT INTO clientes (nome, telefone) VALUES ('"+nome+"','"+telefone+"')"
        conexao.execute(sql_inserir)
        # pesquisar pra que serve o commit, situação rollback cartao nao passa ao realizar compra online
        conexao.commit()
        # fechar conexão
        conexao.close()
        print("insert bem sucedido")
    except sqlite3.Error as e:
        print("erro de dados, verifique")

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
        #inserir registro
        sql_imprimir="SELECT * FROM clientes"
        conexao.execute(sql_imprimir)
        #ler os registros retornados
        registros = cursor.fetchall()
        # garantir que tudo vai ser executado
        conexao.commit()
        # fechar conexão
        conexao.close()
        print("select deu certo")
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