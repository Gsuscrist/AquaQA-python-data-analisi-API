from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.statistics import statistics

app = FastAPI()

app.include_router(statistics)
origins = ["https://aquaqa.sytes.net"]

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
