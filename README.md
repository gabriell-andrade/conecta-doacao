# 🧡 Conecta-Doação

Sistema web para gestão de doações desenvolvido em Python com Flask.

------------------------------------------------------------------------

## 📌 Sobre o projeto

O **Conecta-Doação** é uma aplicação criada para auxiliar instituições
assistenciais (como a APAE) no controle e organização de doações.

O sistema automatiza o cadastro de doadores, organiza informações de
endereço e facilita a gestão de dados através de uma interface web
simples e funcional.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   ✅ Cadastro de doadores\
-   ✅ Listagem de doadores\
-   ✅ Edição de dados\
-   ✅ Exclusão de registros\
-   ✅ Integração com API ViaCEP\
-   ✅ Preenchimento automático de endereço\
-   ✅ Armazenamento em banco SQLite

------------------------------------------------------------------------

## 🛠️ Tecnologias utilizadas

-   Python\
-   Flask\
-   SQLite\
-   HTML\
-   JavaScript (Fetch API)\
-   ViaCEP API

------------------------------------------------------------------------

## 🧠 Arquitetura

O projeto segue uma estrutura modular:

    app/
     ├── __init__.py
     ├── routes.py
     ├── models.py
     └── templates/

-   **routes.py** → rotas da aplicação\
-   **models.py** → acesso ao banco de dados\
-   **templates/** → interface HTML

------------------------------------------------------------------------

## ⚙️ Como executar o projeto

### 1. Clone o repositório

``` bash
git clone https://github.com/seu-usuario/conecta-doacao.git
cd conecta-doacao
```

------------------------------------------------------------------------

### 2. Crie o ambiente virtual

``` bash
python -m venv venv
venv\Scripts\activate
```

------------------------------------------------------------------------

### 3. Instale as dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4. Execute a aplicação

``` bash
python run.py
```

------------------------------------------------------------------------

### 5. Acesse no navegador

    http://127.0.0.1:5000/doadores

------------------------------------------------------------------------

## 🌐 Integração com ViaCEP

Ao inserir um CEP válido, o sistema consulta automaticamente a API
ViaCEP e preenche:

-   Rua\
-   Cidade\
-   Estado

------------------------------------------------------------------------

## 📊 Estrutura do banco

Tabela: `doadores`

-   id\
-   nome\
-   email\
-   cep\
-   rua\
-   numero\
-   complemento\
-   cidade\
-   estado

------------------------------------------------------------------------

## 👨‍💻 Autores

Projeto desenvolvido como parte do **Projeto Integrador (UNIVESP)**.

-   Adriana Mayumi Chagas
-   Gabriel Andrade de Medeiros
-   Karla Giovana Soares Olimpio
-   Lucas Bonilha Grasser de Sousa
-   Jefferson Alves Correia
-   José Marcondes dos Santos
-   Tiago Augusto Olimpio Macena
-   Vitor Ferreira Rodrigues de Miranda


------------------------------------------------------------------------

## 📄 Licença

Este projeto é acadêmico e sem fins lucrativos.
