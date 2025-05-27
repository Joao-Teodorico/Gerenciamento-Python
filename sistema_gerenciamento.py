import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Conectar ao banco
def conectar_banco():
    conexao = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )
    return conexao

# Inserir um cliente
def adicionar_cliente(nome, email, telefone, endereco, cidade, estado, cep):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO clientes (nome, email, telefone, endereco, cidade, estado, cep)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        dados = (nome, email, telefone, endereco, cidade, estado, cep)
        cursor.execute(sql, dados)
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")
    finally:
        cursor.close()
        conexao.close()
