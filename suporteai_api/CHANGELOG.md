# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-01-XX

### ✨ Adicionado
- **API REST completa** para criação de chamados no GLPI
- **Autenticação segura** via App Token e User Token
- **Gerenciamento de sessão** automático (initSession/killSession)
- **Validação de dados** com modelo Pydantic
- **Documentação automática** com Swagger UI
- **Endpoint de saúde** (`/health`)
- **Tratamento de erros** robusto
- **Configuração via variáveis de ambiente**
- **Deploy ready** para Render e outros serviços

### 🔧 Funcionalidades
- `GET /` - Verificação de status da API
- `POST /abrir_chamado` - Criação de chamados no GLPI
- `GET /health` - Verificação de saúde da aplicação
- `GET /docs` - Documentação Swagger automática

### 🛠 Tecnologias
- **FastAPI** - Framework web moderno
- **Pydantic** - Validação de dados
- **Requests** - Cliente HTTP
- **Uvicorn** - Servidor ASGI
- **Python-dotenv** - Gerenciamento de variáveis

### 📁 Estrutura do Projeto
```
suporteai_api/
├── main.py                 # Aplicação FastAPI principal
├── glpi.py                 # Integração com a API do GLPI
├── requirements.txt        # Dependências Python
├── env_example.txt         # Exemplo de variáveis de ambiente
├── render.yaml            # Configuração para deploy no Render
├── exemplos_payload.json  # Exemplos de payload para teste
├── .gitignore            # Arquivos ignorados pelo Git
├── LICENSE               # Licença MIT
├── CONTRIBUTING.md       # Guia de contribuição
├── CHANGELOG.md          # Este arquivo
└── README.md             # Documentação principal
```

### 🔐 Segurança
- Autenticação via tokens do GLPI
- Validação de entrada de dados
- Tratamento seguro de sessões
- Variáveis de ambiente para credenciais

### 📚 Documentação
- README.md completo com exemplos
- Guia de contribuição
- Changelog detalhado
- Exemplos de uso com cURL, Python e Postman

---

## Tipos de Mudanças

- **✨ Adicionado** - Nova funcionalidade
- **🐛 Corrigido** - Correção de bug
- **💥 Quebrado** - Mudança que quebra compatibilidade
- **📝 Documentação** - Mudanças na documentação
- **🎨 Estilo** - Mudanças que não afetam o código (espaços em branco, formatação, etc)
- **♻️ Refatorado** - Refatoração de código
- **⚡ Performance** - Melhoria de performance
- **🧪 Teste** - Adição ou correção de testes
- **🔧 Configuração** - Mudanças em arquivos de configuração 