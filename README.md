# LLMKeeper

Um chat simples de linha de comando em Python com Gemini, integrado pelo LangChain. As mensagens da conversa são mantidas em memória durante a execução e salvas em `memory.txt` ao encerrar com `sair`.

## Requisitos

- Python 3.10 ou superior
- Uma chave de API do Google AI Studio

## Instalação

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

No macOS ou Linux, ative com `source .venv/bin/activate`.

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```dotenv
GOOGLE_API_KEY=sua-chave-do-google-ai-studio
```

## Uso

```bash
python chat.py
```

Digite `sair` para encerrar e salvar o histórico em `memory.txt`.

## Segurança

Não publique sua chave de API. O arquivo `.env`, o ambiente virtual e o histórico local `memory.txt` são ignorados pelo Git.
