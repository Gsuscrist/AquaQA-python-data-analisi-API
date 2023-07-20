from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.statistics import statistics

app = FastAPI()

# Configuración de CORS para permitir las solicitudes desde el origen especificado
origins = ["https://aquaqa.sytes.net"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye tu enrutador `statistics` en la aplicación
app.include_router(statistics)

@app.get("/")
async def root():
    return {"message": "Probability & Statistics API"}
