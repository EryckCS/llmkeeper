# LLMKeeper

Chat de linha de comando em Python que usa LangChain para conversar com diferentes provedores de modelos de IA. Ao iniciar, o programa carrega o conteúdo já salvo em `memory.txt` como contexto da conversa. Ao digitar `sair`, acrescenta as mensagens da sessão ao arquivo.

## Modelos disponíveis

Escolha uma opção ao iniciar:

| Opção | Provedor | Modelo | Variável de API |
|---|---|---|---|
| 1 | OpenAI | `gpt-5-mini` | `OPENAI_API_KEY` |
| 2 | Google Gemini | `google_genai:gemini-2.5-flash` | `GOOGLE_API_KEY` |
| 3 | Anthropic | `claude-haiku-4-5-20251001` | `ANTHROPIC_API_KEY` |
| 4 | xAI | `grok-4.3` | `XAI_API_KEY` |
| 5 | DeepSeek | `deepseek-flash` | `DEEPSEEK_API_KEY` |

É necessária uma chave válida para o provedor escolhido. As integrações dos cinco provedores estão listadas em `requirements.txt`.

## Requisitos

- Python 3.10 ou superior
- Chave de API para pelo menos um dos provedores acima

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

## Configuração

Copie o modelo de configuração para `.env` na raiz do projeto:

```powershell
Copy-Item .envexample .env
```

Preencha a chave do provedor que vai usar. O arquivo `.envexample` mostra os nomes esperados:

```dotenv
OPENAI_API_KEY=sua-chave-openai
GOOGLE_API_KEY=sua-chave-google
ANTHROPIC_API_KEY=sua-chave-anthropic
XAI_API_KEY=sua-chave-xai
DEEPSEEK_API_KEY=sua-chave-deepseek
```

Não é necessário preencher as cinco chaves. Basta a que corresponde ao modelo selecionado.

## Uso

Execute o programa:

```bash
python chat.py
```

Escolha o modelo pelo número e converse pelo terminal. Digite `sair` para encerrar a sessão e salvar suas mensagens em `memory.txt`.

## Histórico da conversa

Na inicialização, se `memory.txt` existir e não estiver vazio, seu conteúdo é incluído no contexto enviado ao modelo. Ao sair, as mensagens da sessão são acrescentadas ao final do arquivo. Assim, o arquivo acumula o histórico entre execuções. O programa não carrega esse conteúdo como mensagens individuais; ele o apresenta ao modelo como texto de contexto.

## Segurança

Mantenha as chaves de API privadas e não publique o arquivo `.env`. O `.env`, os ambientes virtuais e `memory.txt` são arquivos locais ignorados pelo Git.
