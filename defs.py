from langchain.chat_models import init_chat_model
import datetime
from pathlib import Path

def date_conversa():
    return datetime.datetime.now()

def chamar_modelo(nome_modelo, provider_modelo):
    return init_chat_model(model=nome_modelo,
                           model_provider=provider_modelo)

def carregar_memoria():

    memory_path = Path(__file__).with_name("memory.txt")
    
    if memory_path.exists():
        return memory_path.read_text(encoding="utf-8").strip()