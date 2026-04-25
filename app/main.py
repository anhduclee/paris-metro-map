from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.crud.nodes import create_collection_nodes, drop_collection_nodes
from app.crud.edges import create_collection_edges, drop_collection_edges

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_collection_nodes()
    await create_collection_edges()
    yield
    await drop_collection_edges()
    await drop_collection_nodes()

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
async def ping():
    return {"ping": "pong"}
