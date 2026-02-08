from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


def fake_ml_model(x: float) -> float:
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting FastAPI app")
    ml_models["model_1"] = fake_ml_model
    yield
    ml_models.clear()
    logging.info("Deleting FastAPI app")


app = FastAPI(lifespan=lifespan)


@app.post("/")
async def predict(x: float) -> float:
    model = ml_models["model_1"]
    return model(x)
