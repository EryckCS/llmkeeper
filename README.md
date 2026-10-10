# LLMKeeper

Chat de linha de comando em Python que usa o LangChain para conversar com diferentes provedores de modelos de IA. Você escolhe um modelo ao iniciar; as mensagens ficam na memória durante a sessão e são gravadas em `memory.txt` quando você digita `sair`.

## Modelos disponíveis

Escolha uma opção ao iniciar o programa:

| Opção | Provedor | Modelo | Variável de API no `.env` |
|---|---|---|---|
| 1 | OpenAI | `gpt-5-mini` | `OPENAI_API_KEY` |
| 2 | Google Gemini | `google_genai:gemini-2.5-flash` | `GOOGLE_API_KEY` |
| 3 | Anthropic | `claude-haiku-4-5-20251001` | `ANTHROPIC_API_KEY` |
| 4 | xAI | `grok-4.3` | `XAI_API_KEY` |
| 5 | DeepSeek | `deepseek-flash` | `DEEPSEEK_API_KEY` |

Você precisa de uma chave válida para o provedor do modelo escolhido. As chaves são obtidas nos sites de cada provedor. O projeto inclui os pacotes de integração correspondentes no `requirements.txt`.

Caso algum model esteja indisponivel, favor me contatar ou efetuar você mesmo a mudança no código.

## Requisitos

- Python 3.10 ou superior
- Uma chave de API para pelo menos um dos provedores listados

## Instalação

Na pasta do projeto, crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

No macOS ou Linux, use:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração das chaves

Crie um arquivo `.env` na raiz do projeto. Você pode copiar o `.envexample` e preencher somente a chave do provedor que pretende usar:

```dotenv
OPENAI_API_KEY=sua-chave-openai
GOOGLE_API_KEY=sua-chave-google
ANTHROPIC_API_KEY=sua-chave-anthropic
XAI_API_KEY=sua-chave-xai
DEEPSEEK_API_KEY=sua-chave-deepseek
```

Não compartilhe nem publique suas chaves. Você não precisa preencher todas as variáveis; basta a correspondente ao modelo escolhido.

## Uso

Execute:

```bash
python chat.py
```

Digite o número do modelo e, em seguida, envie mensagens no terminal. Digite `sair` para encerrar e gravar o histórico da sessão em `memory.txt`.

O histórico não é carregado automaticamente quando o programa é iniciado novamente; cada execução começa uma nova conversa. Ao sair, `memory.txt` é substituído pelo histórico da sessão atual.

## Segurança

Não publique sua chave de API. O arquivo `.env`, o ambiente virtual e `memory.txt` são ignorados pelo Git.