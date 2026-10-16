# LLMKeeper

Chat de linha de comando em Python que usa LangChain para conversar com provedores de modelos de linguagem. Ao iniciar, o programa pede o identificador do modelo e o provedor; não há um menu de modelos predefinidos.

## Requisitos

- Python 3.10 ou superior
- Uma chave de API válida para o provedor escolhido

As integrações instaladas estão listadas em `requirements.txt`: OpenAI, Google Gemini, Anthropic, xAI, DeepSeek e OpenRouter. O identificador do modelo e o nome do provedor devem ser compatíveis com a integração LangChain correspondente.

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

O programa carrega variáveis de ambiente com `python-dotenv`. Para configurar as chaves, copie o modelo de variáveis e preencha a chave do provedor que pretende usar. No PowerShell:

```powershell
Copy-Item .envexample .env
```

O arquivo `.envexample` lista estas variáveis:

```dotenv
OPENAI_API_KEY=sua-chave-openai
GOOGLE_API_KEY=sua-chave-google
ANTHROPIC_API_KEY=sua-chave-anthropic
XAI_API_KEY=sua-chave-xai
DEEPSEEK_API_KEY=sua-chave-deepseek
OPENROUTER_API_KEY=sua-chave-openrouter
```

Não é necessário preencher todas as chaves. Mantenha `.env` privado e não o publique no GitHub.

## Como usar

Execute o programa a partir da pasta do projeto:

```bash
python chat.py
```

Quando solicitado, informe o identificador do modelo e o provedor aceitos pela integração LangChain instalada. Em seguida, envie mensagens pelo terminal. Digite `sair` para encerrar e salvar as mensagens da sessão.

## Histórico de conversas

Se houver conteúdo em `memory.txt` na pasta do projeto, ele será carregado como contexto inicial para a conversa. Ao encerrar com `sair`, as mensagens humanas e as respostas da sessão são acrescentadas ao arquivo. O histórico é texto simples e permanece local; apague `memory.txt` para começar sem o contexto salvo.

Execute `chat.py` a partir da pasta do projeto para que o arquivo de histórico seja lido e gravado no mesmo local.

## Arquivos locais

O Git ignora `.env`, ambientes virtuais e `memory.txt`. `requirements.txt` contém as dependências do projeto.