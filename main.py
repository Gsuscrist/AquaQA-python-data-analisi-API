from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.statistics import statistics

app = FastAPI()

app.include_router(statistics)
origins = ["http://localhost:8000", "http://aquaqa.sytes.net", "https://aquaqa.sytes.net", "http://localhost:5173",
           "http://127.0.0.1:8000", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(statistics)

@app.get("/")
async def root():
    return {"message": "Probability & Statistics API"}
