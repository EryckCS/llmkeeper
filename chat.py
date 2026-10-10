from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

def escolher_modelo(escolha):

    if escolha == 1:
        return init_chat_model("gpt-5-mini")
    elif escolha == 2:
        return init_chat_model("google_genai:gemini-2.5-flash")
    elif escolha == 3:
        return init_chat_model("claude-haiku-4-5-20251001")
    elif escolha == 4:
        return init_chat_model("grok-4.3")
    elif escolha == 5:
        return init_chat_model("deepseek-flash")
    else:
        print("Digite um número válido")
        return None

print("O sistema tem alguns modelos prontos para uso, escolha com base sua api key!\n\n"
      "[1] gpt-5-mini\n"
      "[2] google_genai:gemini-2.5-flash\n"
      "[3] claude-haiku-4-5-20251001\n"
      "[4] grok-4.3\n"
      "[5] deepseek-flash\n"
)

#Prompt inicial para o modelo.
messages = [
    SystemMessage("Você é uma LLM normal. Ao final de cada resposta, diga que, "
        "caso o usuário não deseje fazer mais perguntas fale para o usuário, digite sair."
        )
]

while True:
    try:
        opcao = int(input("Digite o número da sua escolha: "))
        model = escolher_modelo(opcao)
        if model is not None:
            break
    except (ValueError, ImportError, ModuleNotFoundError) as erro:
        print("Digite apenas número de 1 até 5, ou escolha o modelo válido para chave api que você colocou!")

#Input do usuário e transformar messages em str para guardar no memory.txt
while True:
    print(f"{'HUMAN':-^80}")
    usuario_input = input("Digite sua mensagem: ")
    human_message = HumanMessage(usuario_input)

    if usuario_input.lower().strip() == "sair":
        print("Finalizando o chat e guardando o contexto!")
        with open("memory.txt", "w", encoding="utf-8") as fp:
            for msg in messages:
                fp.write(f"{msg.type}: {msg.content}\n\n")
        break

    messages.append(HumanMessage(usuario_input))
    response = model.invoke(messages)
    print(f"{'AI':-^80}")
    print("AI: ", response.content)
    messages.append(response)