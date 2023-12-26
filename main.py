from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn
from starlette.middleware.cors import CORSMiddleware

from api_v1.menu_views import (
    main_menu_router,
    submenu_router,
    dish_recipe_router,
    get_combined_menu_router,
    html_router,
)
from config import settings
from core.models.base import BaseORM
from core.database import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(BaseORM.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
# app.include_router(html_router, prefix=settings.api_v1_prefix)
app.include_router(get_combined_menu_router, prefix=settings.api_v1_prefix)
app.include_router(main_menu_router, prefix=settings.api_v1_prefix)
app.include_router(submenu_router, prefix=settings.api_v1_prefix)
app.include_router(dish_recipe_router, prefix=settings.api_v1_prefix)


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://db:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        server_header=False,
    )
