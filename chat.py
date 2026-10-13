from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from pathlib import Path
import datetime
load_dotenv()

def date_conversa():
    return datetime.datetime.now()

def escolher_modelo(escolha):

    if escolha == 1:
        return init_chat_model(model="qwen3.5:2b",
                               model_provider="ollama")
    elif escolha == 2:
        return init_chat_model("google_genai:gemini-2.5-flash")
    elif escolha == 3:
        return init_chat_model("claude-haiku-4-5-20251001")
    elif escolha == 4:
        return init_chat_model("xai:grok-4.7")
    elif escolha == 5:
        return init_chat_model("deepseek-flash")
    else:
        print("Digite um número válido")
        return None

#Prompt inicial para o modelo.
messages = [
    SystemMessage("Você é uma LLM normal. Ao final de cada resposta, diga que, "
        "caso o usuário não deseje fazer mais perguntas fale para o usuário, digite sair."
        )
]

def carregar_memoria():

    memory_path = Path(__file__).with_name("memory.txt")
    
    if memory_path.exists():
        return memory_path.read_text(encoding="utf-8").strip()


memoria = carregar_memoria()

if memoria:
    messages.append(
        SystemMessage(content=f"Contexto da conversa anterior:\n{memoria}")
)

def pedir_modelo():
    print("O sistema tem alguns modelos prontos para uso, escolha com base sua api key!\n\n"
    "[1] gpt-5-mini: OPENAI\n"
    "[2] google_genai:gemini-2.5-flash: GOOGLE\n"
    "[3] claude-haiku-4-5-20251001: ANTHROPIC\n"
    "[4] grok-4.3: GROK\n"
    "[5] deepseek-flash: DEEPSEEK\n"
)

    while True:
        try:
            opcao = int(input("Digite o número da sua escolha: "))
            model = escolher_modelo(opcao)
            if model is not None:
                return model
        except (ValueError, ImportError, ModuleNotFoundError) as erro:
            print("Digite apenas número de 1 até 5, ou escolha o modelo válido para chave api que você colocou!")

model = pedir_modelo()


#Input do usuário e transformar messages em str para guardar no memory.txt
while True:
    print(f"{'HUMAN':-^80}")
    usuario_input = input("Digite sua mensagem: ")
    tempohuman = date_conversa()
    print(f"Time: {tempohuman}")
    human_message = HumanMessage(usuario_input)


    if usuario_input.lower().strip() == "sair":
        filtered_messages = [msg for msg in messages if msg.type != "system"]
        response = model.invoke(filtered_messages)
        print("Finalizando o chat e guardando o contexto!")
        with open("memory.txt", "a", encoding="utf-8") as fp:
            for msg in messages:
                if msg.type == "system":
                    continue

                elif msg.type == "human":
                    fp.write(f"{msg.type}: {msg.content}\n\n")
                else:
                    fp.write(f"{msg.type}: {msg.content}\n\n")                    
        break

    messages.append(HumanMessage([usuario_input, tempohuman.isoformat()]))
    response = model.invoke(messages)
    print(f"{'AI':-^80}")

    print("AI: ", response.content)
    tempoai = date_conversa()
    print(f"Time: {tempoai}")
    messages.append(AIMessage([response.content, tempoai.isoformat()]))