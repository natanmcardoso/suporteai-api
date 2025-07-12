from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn
from glpi import criar_chamado_glpi

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Suporte AI API",
    description="API para criação de chamados no GLPI",
    version="1.0.0"
)

class Chamado(BaseModel):
    """
    Modelo Pydantic para validação dos dados do chamado.
    
    Campos:
        nome: Nome completo do solicitante
        telefone: Telefone para contato
        empresa: Nome da empresa do solicitante
        setor: Setor/departamento do solicitante
        descricao: Descrição detalhada do problema
    """
    nome: str
    telefone: str
    empresa: str
    setor: str
    descricao: str

@app.get("/")
async def root():
    """
    Endpoint raiz para verificar se a API está funcionando.
    """
    return {"message": "Suporte AI API está funcionando!"}

@app.post("/abrir_chamado", status_code=status.HTTP_201_CREATED)
async def abrir_chamado(chamado: Chamado):
    """
    Endpoint para criar um novo chamado no GLPI.
    
    Processo:
    1. Valida os dados recebidos via modelo Pydantic
    2. Chama a função criar_chamado_glpi() para criar o chamado
    3. Retorna status 201 com dados do chamado criado ou erro 500
    
    Args:
        chamado (Chamado): Dados do chamado validados pelo modelo Pydantic
    
    Returns:
        Dict: Resposta contendo o status da criação do chamado
    
    Raises:
        HTTPException: Em caso de erro na criação do chamado (status 500)
    """
    
    # Converte o modelo Pydantic para dicionário
    dados_chamado = chamado.dict()
    
    # Chama a função para criar o chamado no GLPI
    status_code, resposta = criar_chamado_glpi(dados_chamado)
    
    # Verifica se houve erro na criação do chamado
    if status_code != 201:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar chamado no GLPI: {resposta.get('error', 'Erro desconhecido')}"
        )
    
    # Retorna sucesso com os dados do chamado criado
    return {
        "success": True,
        "message": "Chamado criado com sucesso!",
        "chamado_id": resposta.get('id'),
        "dados_enviados": dados_chamado,
        "resposta_glpi": resposta
    }

@app.get("/health")
async def health_check():
    """
    Endpoint para verificar a saúde da aplicação.
    """
    return {"status": "healthy", "service": "suporte-ai-api"}

# Executa a aplicação quando o arquivo for executado diretamente
if __name__ == "__main__":
    import os
    import sys
    import uvicorn
    # Corrige o path para importação correta no Windows
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    uvicorn.run(
        "main:app",
        host="127.0.0.1",  # Usar localhost para facilitar acesso local
        port=8000,
        reload=True,
        log_level="info"
    ) 