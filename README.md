# LLMKeeper

Chat de linha de comando em Python que usa LangChain para conversar com diferentes provedores de IA. O programa permite escolher um modelo ao iniciar e reutiliza o conteúdo de `memory.txt` como contexto de conversas anteriores.

## Modelos disponíveis

| Opção | Provedor | Modelo | Variável de ambiente |
|---|---|---|---|
| 1 | OpenAI | `gpt-5-mini` | `OPENAI_API_KEY` |
| 2 | Google Gemini | `google_genai:gemini-2.5-flash` | `GOOGLE_API_KEY` |
| 3 | Anthropic | `claude-haiku-4-5-20251001` | `ANTHROPIC_API_KEY` |
| 4 | xAI | `grok-4.3` | `XAI_API_KEY` |
| 5 | DeepSeek | `deepseek-flash` | `DEEPSEEK_API_KEY` |

É necessária uma chave válida para o provedor escolhido. As integrações dos provedores estão listadas em `requirements.txt`.

## Requisitos

- Python 3.10 ou superior
- Chave de API para pelo menos um dos provedores listados

## Instalação

Na pasta do projeto, crie e ative um ambiente virtual.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS ou Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração das chaves

Copie `.envexample` para `.env` na pasta do projeto. No PowerShell:

```powershell
Copy-Item .envexample .env
```

Preencha a chave correspondente ao modelo que pretende usar:

```dotenv
OPENAI_API_KEY=sua-chave-openai
GOOGLE_API_KEY=sua-chave-google
ANTHROPIC_API_KEY=sua-chave-anthropic
XAI_API_KEY=sua-chave-xai
DEEPSEEK_API_KEY=sua-chave-deepseek
```

Não é necessário preencher todas as chaves. Mantenha `.env` privado e não o publique no GitHub.

## Como usar

Inicie o chat na pasta do projeto:

```bash
python chat.py
```

Digite o número do modelo desejado e envie mensagens pelo terminal. Digite `sair` para encerrar a sessão.

## Histórico

No início, se `memory.txt` existir e tiver conteúdo, o programa o inclui como texto de contexto para o modelo. Ao digitar `sair`, as mensagens da sessão atual são acrescentadas ao final do arquivo. Assim, conversas anteriores permanecem registradas e são apresentadas ao modelo em execuções futuras.

O histórico é armazenado localmente em texto simples. Apague `memory.txt` para começar sem o contexto salvo.

## Arquivos locais

O arquivo `.env`, os ambientes virtuais e `memory.txt` são ignorados pelo Git. `requirements.txt` lista as dependências necessárias para executar o projeto.
