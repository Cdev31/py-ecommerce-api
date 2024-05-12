from fastapi import FastAPI

app: FastAPI = FastAPI()

app.title = "Ecommerce API"
app.version = "0.0.1"


@app.get("/")
def Home() -> object:
    return { "Greeting": "Hello" }

