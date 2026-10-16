from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from defs import *
load_dotenv()

while True:
    print("A seguir digite o nome do seu modelo (model).")

    try:
        nome_modelo = input("Digite: ")
        print("A seguir digite o provedor do seu modelo (model_provider).")
        provider_modelo = input("Digite: ")
        model = chamar_modelo(nome_modelo, provider_modelo)
        break
            
    except (ValueError, ImportError, ModuleNotFoundError) as erro:
        if ValueError:
            print("erro de valor")
        elif ImportError:
            print("erro de import")
        elif ModuleNotFoundError:
            print("module not found")

#Prompt inicial para o modelo.
messages = [
    SystemMessage("Você é uma LLM normal. Ao final de cada resposta, diga que, "
        "caso o usuário não deseje fazer mais perguntas fale para o usuário, digite sair."
        )
]

memoria = carregar_memoria()

if memoria:
    messages.append(
        SystemMessage(content=f"Contexto da conversa anterior:\n{memoria}")
)

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

    messages.append(HumanMessage(content=[{"type": "text", "text": usuario_input},
                                 {"type": "text", "text": tempohuman}]))
    response = model.invoke(messages)
    print(f"{'AI':-^80}")

    print("AI: ", response.content)
    tempoai = date_conversa()
    print(f"Time: {tempoai}")
    messages.append(AIMessage(content=[{"type": "text", "text": response.content},
                                       {"type": "text", "text": tempoai}]))