# 📚 API de Livros - FastAPI

Projeto de estudo para aprender FastAPI através da criação de uma API REST para gerenciamento de livros.

## 🎯 Objetivo

Criar uma API completa com operações CRUD (Create, Read, Update, Delete) e um cliente Python para consumir a API.

---

## 📋 Passos de Implementação

### **Passo 1: Instalação do FastAPI** 🛠️

Primeiro, foi necessário instalar as dependências do projeto:

```bash
# Criar ambiente virtual
python -m venv .pyenv

# Ativar ambiente virtual
source .pyenv/bin/activate  # Linux/Mac
# ou
.pyenv\Scripts\activate  # Windows

# Instalar FastAPI e Uvicorn
pip install fastapi uvicorn[standard]

# Instalar biblioteca para requisições HTTP
pip install requests
```

---

### **Passo 2: Criar API com Endpoints GET** 🚀

**Arquivo:** `api.py`

- Criado o servidor FastAPI com `app = FastAPI()`
- Implementado banco de dados em memória (dicionário Python)
- Criado modelo Pydantic `Livro` para validação de dados
- Implementado dois endpoints GET:
  - `GET /livros` - Listar todos os livros
  - `GET /livros/{livro_id}` - Buscar livro por UUID

**Teste no Swagger:**
```bash
uvicorn api:app --reload
```
Acessar: http://127.0.0.1:8000/docs

---

### **Passo 3: Adicionar Endpoint POST** ➕

**Arquivo:** `api.py`

- Criado modelo `LivroPostPut` (sem UUID, pois é gerado automaticamente)
- Implementado endpoint:
  - `POST /livros` - Adicionar novo livro ao banco de dados
- Configurado validação automática de dados com Pydantic
- Retorna o livro criado com UUID gerado

**Teste no Swagger:** Testar criação de livro pela interface interativa

---

### **Passo 4: Criar Cliente - Operações GET** 📡

**Arquivo:** `cliente.py`

- Criado cliente Python usando biblioteca `requests`
- Implementada função `tratar_resposta()` para formatar JSON de forma legível
- Implementadas funcionalidades:
  - Listar todos os livros
  - Buscar livro por UUID
- Criado menu interativo no terminal

**Executar:**
```bash
# Terminal 1 - Servidor
uvicorn api:app --reload

# Terminal 2 - Cliente
python cliente.py
```

---

### **Passo 5: Adicionar POST no Cliente** ✏️

**Arquivo:** `cliente.py`

- Implementada função `adicionar_livro()`
- Coleta dados do usuário via `input()`
- Envia requisição POST para a API
- Exibe o livro criado com UUID

---

### **Passo 6: Melhorias Visuais** 🎨

**Arquivo:** `cliente.py`

- Adicionados emojis em todo o menu e interações
- Interface mais amigável e visualmente atraente:
  - 📚 Menu principal
  - 🔍 Busca
  - ✅ Sucesso
  - ❌ Erro
  - 👤 Autor, 📕 Título, 🏢 Editora, 📅 Ano

---

## 🚀 Como Executar

### 1. **Iniciar o Servidor FastAPI**

```bash
uvicorn api:app --reload
```

A API estará disponível em:
- **Base URL:** http://127.0.0.1:8000
- **Documentação interativa (Swagger):** http://127.0.0.1:8000/docs
- **Documentação alternativa (ReDoc):** http://127.0.0.1:8000/redoc

### 2. **Executar o Cliente**

Em outro terminal:

```bash
python cliente.py
```

---

## 📝 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/{livro_id}` | Busca livro por UUID |
| POST | `/livros` | Adiciona novo livro |

---

## 🔧 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI
- **Requests** - Cliente HTTP

---

## 📚 Conceitos Aprendidos

### **API vs Cliente**
- **API (api.py):** Servidor que **fornece** dados e funcionalidades
- **Cliente (cliente.py):** Aplicação que **consome** a API

### **Endpoints**
- São as "rotas" ou "caminhos" da API
- Exemplo: `/livros`, `/livros/{id}`

### **Métodos HTTP**
- **GET:** Buscar/listar dados
- **POST:** Criar novos dados
- **PUT:** Atualizar dados existentes
- **DELETE:** Remover dados

### **JSON**
- Formato de troca de dados entre cliente e servidor
- `json.dumps()` formata dados Python em JSON legível

---

## 🎓 Próximos Passos

- [ ] Implementar endpoints PUT e DELETE
- [ ] Adicionar persistência de dados (banco de dados real)
- [ ] Implementar autenticação
- [ ] Criar testes automatizados
- [ ] Deploy da API

---

## 📄 Licença

Projeto de estudos - livre para uso e modificação.
