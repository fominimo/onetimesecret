from typing import Optional
from fastapi import FastAPI
from app.server.routes.secret import router as secret_router

app = FastAPI()
app.include_router(secret_router, tags=["Secret"], prefix="/secret")


@app.get("/", tags=["Root"])
async def read_root():
    return {'Hello': 'World'}

