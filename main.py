from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="API de Gerenciamento", version="1.0")

class Registro(BaseModel):
    id: int
    conteudo: str

@app.get("/health")
def health_check():
    return {"status": "online", "timestamp": datetime.now()}

@app.post("/registros/")
def criar_registro(registro: Registro):
    return {"mensagem": "Registro processado", "id": registro.id}
