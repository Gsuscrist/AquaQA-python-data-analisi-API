from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.statistics import statistics
app = FastAPI()

app.include_router(statistics)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Probability & Statistics API"}

