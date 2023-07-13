from fastapi import FastAPI
from routes.statistics import statistics
app = FastAPI()

app.include_router(statistics)

@app.get("/")
async def root():
    return {"message": "Hello World"}

