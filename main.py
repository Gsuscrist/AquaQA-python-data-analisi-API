from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from routes.statistics import statistics

app = FastAPI()

origins = ["https://aquaqa.sytes.net"]


@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = ",".join(origins)
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    return response


# Incluye tu enrutador `statistics` en la aplicación
app.include_router(statistics)


@app.get("/")
async def root():
    return {"message": "Probability & Statistics API"}
