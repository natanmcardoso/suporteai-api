# 🎯 Suporte AI API

> **API REST para criação automatizada de chamados no GLPI via FastAPI**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [API Endpoints](#-api-endpoints)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Deploy](#-deploy)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🎯 Sobre o Projeto

A **Suporte AI API** é uma solução desenvolvida em FastAPI que permite a criação automatizada de chamados no sistema GLPI (Gestionnaire Libre de Parc Informatique). Ideal para integração com sistemas de suporte por voz, chatbots ou qualquer aplicação que necessite criar tickets de suporte de forma programática.

### ✨ Principais Características

- 🔐 **Autenticação Segura**: Utiliza App Token e User Token do GLPI
- 🔄 **Sessão Completa**: Inicia, utiliza e encerra sessões automaticamente
- 📝 **Validação de Dados**: Modelo Pydantic para validação robusta
- 🚀 **Performance**: FastAPI para alta performance e baixa latência
- 📚 **Documentação Automática**: Swagger UI integrado
- 🐳 **Deploy Ready**: Configuração para Render e outros serviços

## 🚀 Funcionalidades

### ✅ Endpoints Implementados

| Método | Endpoint | Descrição | Status |
|--------|----------|-----------|--------|
| `GET` | `/` | Verifica se a API está funcionando | ✅ |
| `POST` | `/abrir_chamado` | Cria um novo chamado no GLPI | ✅ |
| `GET` | `/health` | Verifica a saúde da aplicação | ✅ |
| `GET` | `/docs` | Documentação Swagger automática | ✅ |

### 🔐 Processo de Autenticação GLPI

1. **Inicia Sessão** via `/initSession`
2. **Cria o Chamado** via POST `/Ticket`
3. **Encerra Sessão** via `/killSession`

## 🛠 Tecnologias Utilizadas

- **[Python 3.8+](https://python.org)** - Linguagem principal
- **[FastAPI](https://fastapi.tiangolo.com)** - Framework web moderno
- **[Pydantic](https://pydantic-docs.helpmanual.io)** - Validação de dados
- **[Requests](https://requests.readthedocs.io)** - Cliente HTTP
- **[Uvicorn](https://uvicorn.org)** - Servidor ASGI
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** - Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Acesso a um servidor GLPI com API REST habilitada
- App Token e User Token do GLPI configurados

## ⚙️ Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/suporteai-api.git
cd suporteai-api
```

### 2. Crie um Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

## 🔧 Configuração

### 1. Configure as Variáveis de Ambiente

Copie o arquivo de exemplo e configure suas credenciais:

```bash
cp env_example.txt .env
```

Edite o arquivo `.env` com suas configurações:

```env
# URL base da API REST do GLPI (deve terminar com /apirest.php)
GLPI_URL=https://seudominio.com/apirest.php

# Token do App (gerado no GLPI em Configuração > Geral > API > App Tokens)
GLPI_APP_TOKEN=sua_chave_do_app

# Token do Usuário (gerado no GLPI em Configuração > Geral > API > User Tokens)
GLPI_USER_TOKEN=seu_token_de_usuario
```

### 2. Obter Tokens do GLPI

#### App Token
1. Acesse o GLPI como administrador
2. Vá em **Configuração > Geral > API**
3. Clique em **App Tokens**
4. Crie um novo token e copie a chave

#### User Token
1. Acesse o GLPI com sua conta
2. Vá em **Configuração > Geral > API**
3. Clique em **User Tokens**
4. Crie um novo token e copie a chave

## 🚀 Uso

### Executar Localmente

```bash
python main.py
```

A API estará disponível em: **http://127.0.0.1:8000**

### Executar com Uvicorn

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Documentação da API

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📡 API Endpoints

### GET /

Verifica se a API está funcionando.

**Resposta:**
```json
{
  "message": "Suporte AI API está funcionando!"
}
```

### POST /abrir_chamado

Cria um novo chamado no GLPI.

**Status de Retorno:** `201 Created` ou `500 Internal Server Error`

**Payload:**
```json
{
    "nome": "João Silva",
    "telefone": "(11) 99999-9999",
    "empresa": "Empresa ABC Ltda",
    "setor": "TI",
    "descricao": "Não consigo acessar o sistema de email. Aparece erro de conexão."
}
```

**Resposta de Sucesso (201):**
```json
{
    "success": true,
    "message": "Chamado criado com sucesso!",
    "chamado_id": 12345,
    "dados_enviados": {
        "nome": "João Silva",
        "telefone": "(11) 99999-9999",
        "empresa": "Empresa ABC Ltda",
        "setor": "TI",
        "descricao": "Não consigo acessar o sistema de email. Aparece erro de conexão."
    },
    "resposta_glpi": {
        "id": 12345,
        "message": "Chamado criado com sucesso",
        "dados": {
            "nome": "João Silva",
            "telefone": "(11) 99999-9999",
            "empresa": "Empresa ABC Ltda",
            "setor": "TI",
            "descricao": "Não consigo acessar o sistema de email. Aparece erro de conexão."
        }
    }
}
```

**Resposta de Erro (500):**
```json
{
    "detail": "Erro ao criar chamado no GLPI: Configurações da API GLPI não encontradas"
}
```

### GET /health

Verifica a saúde da aplicação.

**Resposta:**
```json
{
    "status": "healthy",
    "service": "suporte-ai-api"
}
```

## 💡 Exemplos de Uso

### Testando com cURL

```bash
# Verificar se a API está funcionando
curl http://127.0.0.1:8000/

# Criar um chamado
curl -X POST "http://127.0.0.1:8000/abrir_chamado" \
     -H "Content-Type: application/json" \
     -d '{
       "nome": "João Silva",
       "telefone": "(11) 99999-9999",
       "empresa": "Empresa ABC Ltda",
       "setor": "TI",
       "descricao": "Não consigo acessar o sistema de email."
     }'
```

### Testando com Python

```python
import requests

# Criar chamado
url = "http://127.0.0.1:8000/abrir_chamado"
dados = {
    "nome": "João Silva",
    "telefone": "(11) 99999-9999",
    "empresa": "Empresa ABC Ltda",
    "setor": "TI",
    "descricao": "Não consigo acessar o sistema de email."
}

response = requests.post(url, json=dados)
print(response.json())
```

### Testando com Postman

1. Abra o Postman
2. Crie uma nova requisição POST
3. URL: `http://127.0.0.1:8000/abrir_chamado`
4. Headers: `Content-Type: application/json`
5. Body (raw JSON): Use um dos exemplos do arquivo `exemplos_payload.json`

## 🚀 Deploy

### Deploy no Render

1. **Fork** este repositório
2. Acesse [Render](https://render.com)
3. Conecte seu repositório
4. Configure as variáveis de ambiente:
   - `GLPI_URL`
   - `GLPI_APP_TOKEN`
   - `GLPI_USER_TOKEN`
5. Deploy automático será realizado

### Deploy no Heroku

```bash
# Instalar Heroku CLI
heroku create sua-app-name
heroku config:set GLPI_URL=sua_url
heroku config:set GLPI_APP_TOKEN=seu_token
heroku config:set GLPI_USER_TOKEN=seu_token
git push heroku main
```

### Deploy com Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📁 Estrutura do Projeto

```
suporteai_api/
├── main.py                 # Aplicação FastAPI principal
├── glpi.py                 # Integração com a API do GLPI
├── requirements.txt        # Dependências Python
├── env_example.txt         # Exemplo de variáveis de ambiente
├── render.yaml            # Configuração para deploy no Render
├── exemplos_payload.json  # Exemplos de payload para teste
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Este arquivo
```

## 🔧 Configuração do Chamado no GLPI

O sistema cria chamados no GLPI com as seguintes características:

| Campo | Valor | Descrição |
|-------|-------|-----------|
| **Nome** | `"Suporte por voz - {nome}"` | Título do chamado |
| **Status** | `1` | Novo |
| **Prioridade** | `3` | Normal |
| **Tipo** | `1` | Incidente |
| **Origem** | `1` | Formulário |
| **Conteúdo** | Descrição + informações do solicitante | Detalhes do problema |

## 🐛 Tratamento de Erros

| Código | Descrição |
|--------|-----------|
| `200` | Requisições GET bem-sucedidas |
| `201` | Chamado criado com sucesso |
| `400` | Dados inválidos (validação Pydantic) |
| `500` | Erro interno do servidor ou erro na comunicação com GLPI |

## 📝 Logs e Debug

Os logs são exibidos no console durante a execução:

- ✅ Requisições recebidas
- 🔐 Status da autenticação GLPI
- ❌ Erros de comunicação com GLPI
- ⚠️ Avisos sobre encerramento de sessão

## 🤝 Contribuição

1. **Fork** o projeto
2. Crie uma **Branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### Padrões de Código

- Use **docstrings** para documentar funções
- Siga o padrão **PEP 8** para Python
- Adicione **testes** para novas funcionalidades
- Mantenha a **compatibilidade** com versões anteriores

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

- 📧 **Email**: seu-email@exemplo.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/seu-usuario/suporteai-api/issues)
- 📖 **Documentação**: [Wiki](https://github.com/seu-usuario/suporteai-api/wiki)

## 🙏 Agradecimentos

- [FastAPI](https://fastapi.tiangolo.com) - Framework web incrível
- [GLPI](https://glpi-project.org) - Sistema de gestão de TI
- [Pydantic](https://pydantic-docs.helpmanual.io) - Validação de dados
- Comunidade open source

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

</div> 