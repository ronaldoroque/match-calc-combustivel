from http import HTTPStatus
from requests import get
from fastapi import HTTPException

from src.config import get_settings as settings
from .schemas import *


async def get_route(viagem: Viagem) -> Route:
    if viagem.origem_longitude == viagem.destino_longitude and viagem.origem_latitude == viagem.destino_latitude:
        mess = "As coordenadas de origem e destino fornecidas são iguais. Por favor, verifique a digitação."
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=mess)
    endpoint_mapbox = f"https://api.mapbox.com/directions/v5/mapbox/driving"
    params = {
        'geometries': "geojson",
        'access_token': settings().mapbox_access_token,
    }
    url = f"{endpoint_mapbox}/{viagem.get_coodernadas_to_str()}"
    mapbox_return = get(url=url, params=params)
    response = mapbox_return.json()
    try:
        endereco = response['routes'][0]['legs'][0]['summary']
    except KeyError as erro:
        if max(viagem.origem_longitude, viagem.destino_longitude) > 90.0 or \
                min(viagem.origem_longitude, viagem.destino_longitude) < -90.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Longitude foram digitados corretamente.")
        elif max(viagem.origem_latitude, viagem.destino_latitude) > 180.0 or \
                min(viagem.origem_latitude, viagem.destino_latitude) < -180.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Latitude foram digitados corretamente.")
    except IndexError as erro:
        mess = "Não foi possível encontrar uma rota com base nas coordenadas fornecidas. Verifique se os valores foram digitados corretamente."
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=mess)
    route = Route(**response['routes'][0])
    return route


async def get_relatorio(viagem: Viagem) -> RelatorioViagem:
    route: Route = await get_route(viagem=viagem)
    vias_da_rota: list = route.legs[0].summary
    distancia_km: float = route.distance / 1000
    consumo_total_de_combustivel = 0.0
    if viagem.media_consumo_veiculo != 0.0:
        consumo_total_de_combustivel: float = distancia_km / viagem.media_consumo_veiculo
    relatorio_de_viagem = RelatorioViagem(distancia_km=distancia_km, vias_da_rota=vias_da_rota, consumo_total_de_combustivel=consumo_total_de_combustivel)
    return relatorio_de_viagem


def invert_viagem(viagem: Viagem) -> Viagem:
    return Viagem(origem_longitude=viagem.destino_longitude, origem_latitude=viagem.destino_latitude,
                    destino_longitude=viagem.origem_longitude, destino_latitude=viagem.origem_latitude,
                  media_consumo_veiculo=viagem.media_consumo_veiculo, ida_e_volta=viagem.ida_e_volta)


def join_ida_e_volta(relatorio_ida: RelatorioViagem, relatorio_volta: RelatorioViagem) -> RelatorioViagem:
    distancia_ida_e_volta: float = relatorio_ida.distancia_km + relatorio_volta.distancia_km
    vias_da_rota_ida_e_volta: list = list(set(relatorio_ida.vias_da_rota + relatorio_volta.vias_da_rota))
    consumo_total_de_combustivel_ida_e_volta: float = relatorio_ida.consumo_total_de_combustivel + relatorio_volta.consumo_total_de_combustivel
    return RelatorioViagem(distancia_km=distancia_ida_e_volta, vias_da_rota=vias_da_rota_ida_e_volta,
                           consumo_total_de_combustivel=consumo_total_de_combustivel_ida_e_volta, ida_e_volta=True)


async def calcula_viagem(viagem: Viagem) -> RelatorioViagem:
    relatorio_ida: RelatorioViagem = await get_relatorio(viagem)
    if not viagem.ida_e_volta:
        return relatorio_ida
    viagem_volta: Viagem = invert_viagem(viagem)
    relatorio_volta: RelatorioViagem = await get_relatorio(viagem_volta)
    relatorio_ida_e_volta: RelatorioViagem = join_ida_e_volta(relatorio_ida=relatorio_ida, relatorio_volta=relatorio_volta)
    return relatorio_ida_e_volta
