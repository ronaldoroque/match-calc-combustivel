from fastapi import FastAPI
from fastapi.datastructures import Default
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

from src.config import get_settings as settings
from src.controller import router


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings().debug,
        title=settings().project_name,
        description=settings().description,
        version=settings().version,
        default_response_class=Default(ORJSONResponse)
    )
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["*"]
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings().allowed_origins.split(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(router=router)
    return app


app = create_app()


@app.get("/", response_class=ORJSONResponse)
async def hello_word():
    return {"message": "Hello Word"}
