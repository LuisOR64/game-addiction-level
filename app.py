from fastapi import FastAPI
from router import router
from driver.driver_db import Base, engine

app = FastAPI(
    title="Game addiction level API con FastAPI",
    description="Prediccion de nivel de addicción a los videojuegos con Fast Api",
    version="1.0.0"
)

app.include_router(router.router)

@app.get("/")
def index():
    return {
        "title": "Fastapi game addiction level api V 1.0",
        "message": "API game addiction level"
        }

Base.metadata.create_all(engine)