from fastapi import FastAPI

from src.routes.auth import router as auth_router
from src.routes.dashboard import router as dashboard_router
from src.routes.add_details import router as add_details_router
app=FastAPI()


app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(add_details_router)