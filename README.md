# 🚀 Projeto: Flask JWT API Data Exporter

Este projeto demonstra a construção de uma **API cliente-servidor** utilizando **Python** e **Flask**, com autenticação JWT. A API permite ao cliente ler dados e exportá-los em vários formatos, incluindo **TXT**, **JSON**, **YAML** e **XML**. 

## 📌 Visão Geral

O objetivo deste projeto é ilustrar a criação de uma API RESTful completa com Flask, mostrando como lidar com autenticação JWT e como exportar dados em diferentes formatos. O projeto é dividido em duas partes principais:

1. **Servidor API**: Fornece endpoints para autenticação e exportação de dados.
2. **Cliente**: Consome a API e realiza a exportação dos dados em diferentes formatos.

## 🛠️ Arquivos Principais

### 🗂️ **Servidor API**

- **[server.py](https://github.com/evolucaoit/flask_JWT-API-Data_Exporter/blob/main/server.py)**: O arquivo principal do servidor Flask, onde estão definidos os endpoints da API e a lógica de autenticação JWT. Este script gerencia as requisições e garante que somente usuários autenticados possam acessar os dados.

### 🔑 **Configuração de Login**

- **[login.json](https://github.com/evolucaoit/flask_JWT-API-Data_Exporter/blob/main/login.json)**: Arquivo contendo as credenciais de login para autenticação. Ele é utilizado pelo servidor para verificar a autenticidade das credenciais fornecidas pelo cliente.

### 🖥️ **Cliente**

- **[client.py](https://github.com/evolucaoit/flask_JWT-API-Data_Exporter/blob/main/client.py)**: O script cliente que se comunica com a API, autenticando-se com JWT e solicitando dados. Este arquivo também é responsável por exportar os dados recebidos em diferentes formatos.

### 📊 **Dados**

- **[data.json](https://github.com/evolucaoit/flask_JWT-API-Data_Exporter/blob/main/data.json)**: Arquivo JSON contendo os dados que serão expostos pela API. O cliente pode solicitar esses dados e exportá-los em diferentes formatos.

## 📜 Funcionalidades

- **Autenticação JWT**: Segurança e controle de acesso são gerenciados usando JWT, garantindo que apenas usuários autenticados possam acessar os dados.
- **Exportação de Dados**: Os dados podem ser exportados em vários formatos, incluindo TXT, JSON, YAML e XML, demonstrando a flexibilidade na manipulação e apresentação de dados.
- **API RESTful**: A arquitetura da API segue os princípios REST, facilitando a integração com outras aplicações e sistemas.

## 💡 Demonstração

Este projeto mostra minha capacidade de:

- **Construir APIs RESTful** com Flask e Python.
- **Implementar autenticação JWT** para garantir a segurança da aplicação.
- **Manipular e exportar dados** em múltiplos formatos (TXT, JSON, YAML e XML).
- **Desenvolver soluções completas** que integram cliente e servidor de forma eficiente.

Acompanhe este repositório para ver a evolução deste projeto e como diferentes tecnologias e práticas são aplicadas para resolver problemas reais.

## 📚 Referências e Leitura Adicional

- **[Documentação Flask](https://flask.palletsprojects.com/en/latest/)**: Para entender melhor o framework Flask.
- **[JWT - JSON Web Tokens](https://jwt.io/introduction/)**: Informações detalhadas sobre autenticação com JWT.

---

**Elias Andrade**
