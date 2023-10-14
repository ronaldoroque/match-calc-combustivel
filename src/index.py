import locale
from http import HTTPStatus
from typing import Optional, Union

from requests import get
from orjson import orjson

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.datastructures import Default
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, validator

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
    # app.mount("/static", StaticFiles(directory="static"), name="static")  # TODO: liberar quando a pasta for encontrada no ambiente de desenvolvimento da equipe.
    return app


app = create_app()
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


class Leg(BaseModel):
    via_waypoints: list
    admins: list
    weight: float
    duration: float
    steps: list
    distance: float
    summary: list[str] | str

    @validator('summary')
    def str_to_list(cls, v):
        if isinstance(v, str):
            v = v.split(", ")
            return v
        return v


class Route(BaseModel):
    weight_name: str
    weight: float
    duration: float
    distance: float
    legs: list[Leg]
    geometry: dict[str, Union[list[list[float]], str]]


async def get_route(viagem: Viagem) -> Route:
    endpoint_mapbox = f"https://api.mapbox.com/directions/v5/mapbox/driving"
    params = {
        'geometries': "geojson",
        'access_token': settings().mapbox_access_token,
    }
    url = f"{endpoint_mapbox}/{viagem.coodernadas()}"
    mapbox_return = get(url=url, params=params)
    response = mapbox_return.json()
    try:
        endereco = (response['routes'][0]['legs'][0]['summary'])
    except KeyError as erro:
        if max(viagem.origem_longitude, viagem.destino_longitude) > 90.0 or \
                min(viagem.origem_longitude, viagem.destino_longitude) < -90.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Longitude foram digitados corretamente.")
        elif max(viagem.origem_latitude, viagem.destino_latitude) > 180.0 or \
                min(viagem.origem_latitude, viagem.destino_latitude) < -180.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Latitude foram digitados corretamente.")
    route = Route(**response['routes'][0])
    return route


@app.post("/distance", response_class=HTMLResponse)
async def distance(request: Request, viagem: Viagem):
    route: Route = await get_route(viagem=viagem)
    vias_da_rota: list = route.legs[0].summary
    distance: str = ""
    consumo_do_veiculo: float = 0.0
    try:
        distance_float: float = route.distance / 1000
        format_decimal = "%.{0:d}f".format(2)
        distance = locale.format_string(format_decimal, distance_float, grouping=True, monetary=False)
        consumo_do_veiculo = distance_float / viagem.km_litro
        consumo_do_veiculo_str: str = locale.format_string(format_decimal, consumo_do_veiculo, grouping=True, monetary=False)
    except TypeError:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Erro interno de tipo.")
    except AttributeError:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Erro interno na resposta da API")
    return templates.TemplateResponse("item.html", {"request": request, "distance": distance,
                                                    'vias_da_rota': vias_da_rota, 'consumo_do_veiculo': consumo_do_veiculo_str})


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/api")
def read_root():
    return {"Hello": "World"}
