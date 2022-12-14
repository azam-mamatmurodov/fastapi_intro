from typing import Union

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    name: Union[str, None] = Query(default=None, alias="name"),
):
    results = {"item_id": item_id}
    if name:
        results.update({"name": name})
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
