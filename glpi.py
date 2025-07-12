import requests
import os
from dotenv import load_dotenv
from typing import Dict, Tuple, Any

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def criar_chamado_glpi(dados: dict) -> Tuple[int, Dict[str, Any]]:
    """
    Cria um chamado no GLPI usando a API REST com autenticação completa.
    
    Processo:
    1. Inicia sessão com o GLPI via /initSession
    2. Cria o chamado via POST /Ticket
    3. Encerra a sessão via /killSession
    
    Args:
        dados (dict): Dicionário contendo os dados do chamado
            - nome: Nome do solicitante
            - telefone: Telefone do solicitante
            - empresa: Empresa do solicitante
            - setor: Setor do solicitante
            - descricao: Descrição do problema
    
    Returns:
        Tuple[int, Dict]: Tupla contendo o status_code e a resposta JSON da API
    """
    
    # Obtém as configurações da API do GLPI das variáveis de ambiente
    glpi_url = os.getenv('GLPI_URL')
    app_token = os.getenv('GLPI_APP_TOKEN')
    user_token = os.getenv('GLPI_USER_TOKEN')
    
    # Verifica se todas as variáveis de ambiente estão configuradas
    if not all([glpi_url, app_token, user_token]):
        return 500, {"error": "Configurações da API GLPI não encontradas"}
    
    # Headers base para todas as requisições
    base_headers = {
        'Content-Type': 'application/json',
        'App-Token': app_token
    }
    
    session_token = None
    
    try:
        # 1. INICIA SESSÃO COM O GLPI
        init_response = requests.get(
            f"{glpi_url}/initSession",
            headers=base_headers,
            timeout=30
        )
        
        if init_response.status_code != 200:
            return 500, {"error": f"Erro ao iniciar sessão GLPI: {init_response.text}"}
        
        # Extrai o token da sessão da resposta
        session_data = init_response.json()
        session_token = session_data.get('session_token')
        
        if not session_token:
            return 500, {"error": "Token de sessão não encontrado na resposta"}
        
        # Headers com o token da sessão
        session_headers = {
            **base_headers,
            'Session-Token': session_token
        }
        
        # 2. PREPARA OS DADOS DO CHAMADO
        ticket_data = {
            "input": {
                "name": f"Suporte por voz - {dados['nome']}",
                "content": f"""
Descrição do Problema:
{dados['descricao']}

Informações do Solicitante:
- Nome: {dados['nome']}
- Telefone: {dados['telefone']}
- Empresa: {dados['empresa']}
- Setor: {dados['setor']}
                """.strip(),
                "status": 1,  # 1 = Novo
                "priority": 3,  # 3 = Normal
                "type": 1,  # 1 = Incidente
                "source": 1  # 1 = Formulário
            }
        }
        
        # 3. CRIA O CHAMADO VIA API
        ticket_response = requests.post(
            f"{glpi_url}/Ticket",
            headers=session_headers,
            json=ticket_data,
            timeout=30
        )
        
        # Verifica se o chamado foi criado com sucesso
        if ticket_response.status_code != 201:
            return ticket_response.status_code, {
                "error": f"Erro ao criar chamado: {ticket_response.text}"
            }
        
        # Extrai o ID do chamado criado
        ticket_data_response = ticket_response.json()
        chamado_id = ticket_data_response.get('id')
        
        # 4. ENCERRA A SESSÃO
        kill_response = requests.get(
            f"{glpi_url}/killSession",
            headers=session_headers,
            timeout=30
        )
        
        # Retorna sucesso mesmo se o encerramento da sessão falhar
        if kill_response.status_code != 200:
            print(f"Aviso: Erro ao encerrar sessão GLPI: {kill_response.text}")
        
        # Retorna sucesso com o ID do chamado criado
        return 201, {
            "id": chamado_id,
            "message": "Chamado criado com sucesso",
            "dados": dados
        }
        
    except requests.exceptions.RequestException as e:
        # Em caso de erro na requisição, tenta encerrar a sessão se existir
        if session_token:
            try:
                requests.get(
                    f"{glpi_url}/killSession",
                    headers={**base_headers, 'Session-Token': session_token},
                    timeout=10
                )
            except:
                pass  # Ignora erro no encerramento da sessão
        
        return 500, {"error": f"Erro na comunicação com a API GLPI: {str(e)}"}
    
    except Exception as e:
        # Em caso de erro geral, tenta encerrar a sessão se existir
        if session_token:
            try:
                requests.get(
                    f"{glpi_url}/killSession",
                    headers={**base_headers, 'Session-Token': session_token},
                    timeout=10
                )
            except:
                pass  # Ignora erro no encerramento da sessão
        
        return 500, {"error": f"Erro inesperado: {str(e)}"} 