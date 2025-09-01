# backend/app/main.py
from fastapi import FastAPI
from app.api import producto_api, deposito_api

app = FastAPI(title="Inventario MVH S.R.L")

app.include_router(producto_api.router)
app.include_router(deposito_api.router)
