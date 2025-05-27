-- Arquivo: criar_tabela_clientes.sql

-- Criação do banco de dados (opcional)
CREATE DATABASE IF NOT EXISTS sistema_clientes;
USE sistema_clientes;

-- Criação da tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    endereco TEXT,
    cidade VARCHAR(50),
    estado VARCHAR(2),
    cep VARCHAR(10),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);