from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Subtraction API is running"}

@app.get("/subtract")
def subtract(num1: int, num2: int):
    result = num1 - num2
    return {
        "num1": num1,
        "num2": num2,
        "result": result
    }
