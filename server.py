from fastapi import FastAPI
from src.router.index_router import api_router
app: FastAPI = FastAPI()

app.title = "Ecommerce API"
app.version = "0.0.1"


@app.get("/")
def Home() -> object:
    return { "Greeting": "Hello" }

api_router( app )