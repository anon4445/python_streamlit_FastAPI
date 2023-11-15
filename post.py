from fastapi import FastAPI
app = FastAPI()

@app.post("/add")
def add_numbers(num1: float, 
                num2: float):      # this is the parameter of the API.
    result = num1 + num2
    return {"result": result}