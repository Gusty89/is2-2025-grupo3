# app/mainApi.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import usuario_router, producto_router, deposito_router, movimiento_router, rol_router

app = FastAPI(
    title="Sistema de Inventario",
    description="API para gestión de usuarios, productos, depósitos, movimientos y roles",
    version="1.0.0"
)

# Permitir CORS para pruebas desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción restringir a dominios confiables
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(usuario_router.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(producto_router.router, prefix="/productos", tags=["Productos"])
app.include_router(deposito_router.router, prefix="/depositos", tags=["Depósitos"])
app.include_router(movimiento_router.router, prefix="/movimientos", tags=["Movimientos"])
app.include_router(rol_router.router, prefix="/roles", tags=["Roles"])
