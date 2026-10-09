from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = init_chat_model("google_genai:gemini-2.5-flash")


messages = [
    SystemMessage("Você é uma LLM normal. Ao final de cada resposta, diga que, "
        "caso o usuário não deseje fazer mais perguntas, digite sair, mas em um texto pequeno."
        )
]

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

    



