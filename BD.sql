CREATE DATABASE gerenciamento;
USE gerenciamento;

CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  telefone VARCHAR(20),
  endereco VARCHAR(150),
  cidade VARCHAR(100),
  estado VARCHAR(2),
  cep VARCHAR(10)
);