import locale
from http import HTTPStatus
from typing import Optional

from requests import get
from orjson import orjson

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.datastructures import Default
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from src.config import get_settings as settings
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def create_app() -> FastAPI:

    app = FastAPI(
        debug=settings().debug,
        title=settings().project_name,
        description=settings().description,
        version=settings().version,
        default_response_class=Default(ORJSONResponse)
    )

    api_version = "/api/v1"
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = create_app()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Viagem(BaseModel):
    origem_longitude: float
    origem_latitude: float
    destino_longitude: float
    destino_latitude: float
    ida_e_volta: Optional[bool] = True
    km_litro: float

    def coodernadas(self):
        return f"{self.origem_longitude},{self.origem_latitude};{self.destino_longitude},{self.destino_latitude}"


@app.post("/distance", response_class=HTMLResponse)
async def distance(request: Request, viagem: Viagem):
    endpoint_mapbox = f"https://api.mapbox.com/directions/v5/mapbox/driving"
    params = {
        'geometries': "geojson",
        'access_token': settings().mapbox_access_token,
    }
    url = f"{endpoint_mapbox}/{viagem.coodernadas()}"
    mapbox_return = get(url=url, params=params)
    response = orjson.loads(mapbox_return.text)
    distance = None
    endereco = (response['routes'][0]['legs'][0]['summary'])
    consumo_do_veiculo = None
    try:
        distance_float: float = (response['routes'][0]['distance'])/1000
        formato_decimal = "%.{0:d}f".format(2)
        distance = locale.format_string(formato_decimal, distance_float, grouping=True, monetary=False)
        consumo_do_veiculo = distance_float / viagem.km_litro
        consumo_do_veiculo = round(consumo_do_veiculo)
    except TypeError:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Erro interno de tipo.")
    except AttributeError:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Erro interno na resposta da API")
    return templates.TemplateResponse("item.html", {"request": request, "distance": distance,
                                                    'endereco': endereco, 'consumo_do_veiculo': consumo_do_veiculo})


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/api")
def read_root():
    return {"Hello": "World"}
