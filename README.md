# 🧡 Conecta-Doação

Sistema web para gestão de doações desenvolvido com **Python + Flask**, com foco em organização, controle e praticidade para instituições assistenciais como a APAE.

---

## 📌 Sobre o projeto

O **Conecta-Doação** foi desenvolvido para facilitar o gerenciamento de doações, permitindo que usuários registrem contribuições e que administradores tenham controle total das informações.

O sistema automatiza o cadastro de dados, melhora a organização e torna o processo mais eficiente através de uma interface simples e intuitiva.

---

## 🚀 Funcionalidades

### 👤 Usuário
- Cadastro de conta  
- Login e autenticação  
- Cadastro de doações  
- Visualização das próprias doações  
- Upload de foto de perfil  

### 🛠️ Administrador
- Visualização de todas as doações  
- Filtros por nome, cidade, CEP e status  
- Atualização de status das doações  
- Exclusão de registros  

### ⚙️ Sistema
- Integração com API ViaCEP  
- Preenchimento automático de endereço  
- Padronização de dados (ex: número S/N)  
- Banco de dados SQLite  

---

## 🛠️ Tecnologias utilizadas

- Python  
- Flask  
- SQLite  
- HTML + CSS (Bootstrap)  
- JavaScript  
- API ViaCEP  

---

## 🧠 Arquitetura do projeto

```
app/
├── routes.py
├── models.py
├── templates/
│   ├── auth/
│   ├── doacoes/
│   ├── admin/
│   ├── user/
│   └── components/
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gabriell-andrade/conecta-doacao.git
cd conecta-doacao
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Execute o projeto

```bash
python run.py
```

---

### 5. Acesse no navegador

```bash
http://127.0.0.1:5000/
```

---

## 🌐 Integração com ViaCEP

Ao inserir um CEP válido, o sistema consulta automaticamente a API ViaCEP e preenche:

- Rua  
- Bairro  
- Cidade  
- Estado  

---

## 📊 Estrutura do banco de dados

### Tabela: usuarios

- id  
- nome  
- sobrenome  
- email  
- senha  
- tipo  
- foto_perfil  

### Tabela: doadores

- id  
- usuario_id  
- nome  
- email  
- cep  
- rua  
- numero  
- complemento  
- bairro  
- cidade  
- estado  
- descricao  
- status  

---

## 👨‍💻 Autores

Projeto desenvolvido como parte do Projeto Integrador (UNIVESP).

- Adriana Mayumi Chagas  
- Gabriel Andrade de Medeiros  
- Karla Giovana Soares Olimpio  
- Lucas Bonilha Grasser de Sousa  
- Jefferson Alves Correia  
- José Marcondes dos Santos  
- Tiago Augusto Olimpio Macena  
- Vitor Ferreira Rodrigues de Miranda  

---

## 📄 Licença

Este projeto é acadêmico e sem fins lucrativos.
