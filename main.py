from fastapi import FastAPI
from model.ModelName import ModelName
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello Word"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/all_item")
async def read_all_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/model_name")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3333)
