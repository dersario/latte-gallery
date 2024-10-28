from fastapi import FastAPI
from latte_gallery.routers import router, accounts_router, pictures_router
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI(title='MakVNS')
    app.include_router(router)
    app.include_router(accounts_router)
    app.include_router(pictures_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True
    )
    return app