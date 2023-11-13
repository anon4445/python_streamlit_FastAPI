from fastapi import FastAPI

app= FastAPI()

@app.get("/items")
def get_items():
    my_food= ["french fries", "egg", "beef"]
    return{"items": my_food }