# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o projeto **Suporte AI API**! 

## 📋 Como Contribuir

### 1. Fork e Clone

1. Faça um **fork** do repositório
2. Clone seu fork localmente:
   ```bash
   git clone https://github.com/seu-usuario/suporteai-api.git
   cd suporteai-api
   ```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp env_example.txt .env
# Edite o arquivo .env com suas configurações
```

### 3. Crie uma Branch

```bash
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b fix/correcao-bug
```

### 4. Desenvolva

- Escreva código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Siga os padrões de código estabelecidos
- Teste suas mudanças localmente

### 5. Commit e Push

```bash
git add .
git commit -m "feat: adiciona nova funcionalidade X"
git push origin feature/nova-funcionalidade
```

### 6. Pull Request

1. Vá para o repositório original no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Descreva suas mudanças detalhadamente
5. Aguarde a revisão

## 📝 Padrões de Código

### Python

- Siga o **PEP 8** para estilo de código
- Use **type hints** quando possível
- Documente funções com **docstrings**
- Mantenha linhas com no máximo 88 caracteres

### Commits

Use o padrão **Conventional Commits**:

```
feat: adiciona nova funcionalidade
fix: corrige bug na autenticação
docs: atualiza documentação
test: adiciona testes para endpoint X
refactor: refatora função de validação
style: formata código
chore: atualiza dependências
```

### Estrutura de Arquivos

```
suporteai_api/
├── main.py                 # Aplicação principal
├── glpi.py                 # Integração GLPI
├── tests/                  # Testes unitários
├── docs/                   # Documentação adicional
├── requirements.txt        # Dependências
└── README.md              # Documentação principal
```

## 🧪 Testes

### Executar Testes

```bash
# Instalar pytest
pip install pytest

# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=.

# Executar testes específicos
pytest tests/test_main.py
```

### Escrever Testes

```python
# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Suporte AI API está funcionando!"}

def test_criar_chamado():
    dados = {
        "nome": "Teste",
        "telefone": "(11) 99999-9999",
        "empresa": "Empresa Teste",
        "setor": "TI",
        "descricao": "Problema de teste"
    }
    response = client.post("/abrir_chamado", json=dados)
    assert response.status_code in [201, 500]  # 201 sucesso, 500 erro GLPI
```

## 📚 Documentação

### Atualizar README

- Mantenha o README atualizado
- Adicione exemplos de uso
- Documente novas funcionalidades
- Inclua screenshots quando relevante

### Docstrings

```python
def minha_funcao(parametro: str) -> dict:
    """
    Descrição breve da função.
    
    Args:
        parametro (str): Descrição do parâmetro
        
    Returns:
        dict: Descrição do retorno
        
    Raises:
        ValueError: Quando o parâmetro é inválido
        
    Example:
        >>> resultado = minha_funcao("teste")
        >>> print(resultado)
        {'status': 'success'}
    """
    pass
```

## 🐛 Reportar Bugs

### Antes de Reportar

1. Verifique se o bug já foi reportado
2. Teste com a versão mais recente
3. Reproduza o bug em um ambiente limpo

### Template de Bug Report

```markdown
## 🐛 Descrição do Bug

Descrição clara e concisa do bug.

## 🔄 Passos para Reproduzir

1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## ✅ Comportamento Esperado

O que deveria acontecer.

## ❌ Comportamento Atual

O que está acontecendo.

## 📱 Informações do Sistema

- OS: [ex: Windows 10]
- Python: [ex: 3.9.0]
- FastAPI: [ex: 0.104.1]

## 📋 Logs

```
Logs de erro aqui
```

## 🖼️ Screenshots

Se aplicável, adicione screenshots.
```

## 💡 Sugerir Melhorias

### Template de Feature Request

```markdown
## 💡 Descrição da Melhoria

Descrição clara da funcionalidade desejada.

## 🎯 Problema que Resolve

Explicação de como isso ajudaria.

## 💭 Solução Proposta

Descrição da solução ideal.

## 🔄 Alternativas Consideradas

Outras soluções que você considerou.

## 📋 Informações Adicionais

Qualquer contexto adicional.
```

## 🏷️ Labels

Use as labels apropriadas:

- `bug` - Bug report
- `enhancement` - Nova funcionalidade
- `documentation` - Melhorias na documentação
- `good first issue` - Bom para iniciantes
- `help wanted` - Precisa de ajuda
- `question` - Pergunta/dúvida

## 📞 Suporte

Se você tiver dúvidas sobre como contribuir:

- Abra uma **issue** com a label `question`
- Entre em contato via email
- Consulte a documentação do projeto

## 🙏 Agradecimentos

Obrigado por contribuir para tornar este projeto melhor! 

---

**Lembre-se**: Cada contribuição, por menor que seja, é muito bem-vinda! 🎉 