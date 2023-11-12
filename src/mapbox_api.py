from http import HTTPStatus
from statistics import geometric_mean

from requests import get, Response as Requests_Response
from fastapi import HTTPException
from fastapi.responses import Response as Fastapi_Response

from src.config import get_settings as settings
from .schemas import *


async def get_route(viagem: Viagem, geometries: str = "polyline") -> Route:
    if viagem.origem_longitude == viagem.destino_longitude and viagem.origem_latitude == viagem.destino_latitude:
        mess = "As coordenadas de origem e destino fornecidas são iguais. Por favor, verifique a digitação."
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=mess)
    endpoint_mapbox = "https://api.mapbox.com/directions/v5/mapbox/driving"
    params = {
        'geometries': geometries,
        'access_token': settings().mapbox_access_token,
    }
    url = f"{endpoint_mapbox}/{viagem.get_coodernadas_to_str()}"
    mapbox_return = get(url=url, params=params)
    response = mapbox_return.json()
    if 'code' in response and (response['code'] == 'NoSegment' or response['code'] == 'InvalidInput'):
        mess = "Não foi possível encontrar uma rota com base nas coordenadas fornecidas. Verifique se os valores foram digitados corretamente."
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=mess)
    if 'routes' not in response:
        if max(viagem.origem_longitude, viagem.destino_longitude) > 90.0 or \
                min(viagem.origem_longitude, viagem.destino_longitude) < -90.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Longitude foram digitados corretamente.")
        elif max(viagem.origem_latitude, viagem.destino_latitude) > 180.0 or \
                min(viagem.origem_latitude, viagem.destino_latitude) < -180.0:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail="Verifique se os valores de Latitude foram digitados corretamente.")
        else:
            mess = "Não foi possível encontrar uma rota com base nas coordenadas fornecidas. Verifique se os valores foram digitados corretamente."
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=mess)
    route = Route(**response['routes'][0])
    return route


async def get_place_name(longitude: float, latitude: float) -> str:
    endpoint_mapbox = "https://api.mapbox.com/search/geocode/v6/reverse"
    params = {
        'longitude': longitude,
        'latitude': latitude,
        'access_token': settings().mapbox_access_token,
    }
    mapbox_return = get(url=endpoint_mapbox, params=params)
    response = mapbox_return.json()
    route: str = response['features'][0]['properties']['name']
    return route


async def get_map_image(coordenadas: Coordenadas, zoom: float = 15.0, width: int = 470, height: int = 300) -> Fastapi_Response:
    endpoint_mapbox = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
    pino_a = f"pin-s-a+ff3348({coordenadas.origem_longitude},{coordenadas.origem_latitude})"
    pino_b = f"pin-s-b+589294({coordenadas.destino_longitude},{coordenadas.destino_latitude})"
    path = f"path-5+f44-0.5({coordenadas.geometry})"
    # URL para mapa apenas do destino:
    if coordenadas.geometry is None:
        url = f"{endpoint_mapbox}/{pino_b}/{coordenadas.destino_longitude},{coordenadas.destino_latitude},{zoom}/{width}x{height}"
    # URL para mapa com pontos de origem e destino e a rota:
    else:
        url = f"{endpoint_mapbox}/{pino_a},{pino_b},{path}/auto/{width}x{height}"
    params = {
        'access_token': settings().mapbox_access_token,
    }
    mapbox_return: Requests_Response = get(url=url, params=params)
    if mapbox_return.status_code == 422:
        message = mapbox_return.json()['message']
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=message)
    result = Fastapi_Response(content=mapbox_return.content, media_type=mapbox_return.headers._store['content-type'][1])
    return result


async def get_relatorio(viagem: Viagem) -> RelatorioViagem:
    route: Route = await get_route(viagem=viagem)
    route_summary: list = route.legs[0].summary
    vias_da_rota: list = ["<origem>", *route_summary, "<destino>"]
    distancia_km: float = route.distance / 1000
    consumo_total_de_combustivel = 0.0
    if viagem.media_consumo_veiculo != 0.0:
        consumo_total_de_combustivel: float = distancia_km / viagem.media_consumo_veiculo
    relatorio_de_viagem = RelatorioViagem(distancia_km=distancia_km, vias_da_rota=vias_da_rota,
                                          consumo_total_de_combustivel=consumo_total_de_combustivel,
                                          geometry=route.geometry)
    return relatorio_de_viagem


def invert_viagem(viagem: Viagem) -> Viagem:
    return Viagem(origem_longitude=viagem.destino_longitude, origem_latitude=viagem.destino_latitude,
                    destino_longitude=viagem.origem_longitude, destino_latitude=viagem.origem_latitude,
                  media_consumo_veiculo=viagem.media_consumo_veiculo, ida_e_volta=viagem.ida_e_volta)


def join_ida_e_volta(relatorio_ida: RelatorioViagem, relatorio_volta: RelatorioViagem) -> RelatorioViagem:
    distancia_ida_e_volta: float = relatorio_ida.distancia_km + relatorio_volta.distancia_km
    if relatorio_volta.vias_da_rota[0] == "<origem>":
        del relatorio_volta.vias_da_rota[0]
    if relatorio_volta.vias_da_rota[-1] == "<destino>":
        del relatorio_volta.vias_da_rota[-1]
    vias_da_rota_ida_e_volta: list[str] = [*relatorio_ida.vias_da_rota, *relatorio_volta.vias_da_rota, "<origem>"]
    consumo_total_de_combustivel_ida_e_volta: float = relatorio_ida.consumo_total_de_combustivel + relatorio_volta.consumo_total_de_combustivel
    return RelatorioViagem(distancia_km=distancia_ida_e_volta, vias_da_rota=vias_da_rota_ida_e_volta,
                           consumo_total_de_combustivel=consumo_total_de_combustivel_ida_e_volta,
                           ida_e_volta=True, geometry=relatorio_ida.geometry)


async def identifica_origen_destino_e_percurso(relatorio_viagem: RelatorioViagem, viagem: Viagem) -> RelatorioViagem:
    place_origem = await get_place_name(longitude=viagem.origem_longitude, latitude=viagem.origem_latitude)
    place_destino = await get_place_name(longitude=viagem.destino_longitude, latitude=viagem.destino_latitude)
    for index, route_point in enumerate(relatorio_viagem.vias_da_rota):
        if route_point == "<origem>":
            relatorio_viagem.vias_da_rota[index] = {'type': "origem", 'name': place_origem}
        elif route_point == "<destino>":
            relatorio_viagem.vias_da_rota[index] = {'type': "destino", 'name': place_destino}
        else:
            relatorio_viagem.vias_da_rota[index] = {'type': "percurso", 'name': route_point}
    return relatorio_viagem


async def calcula_viagem(viagem: Viagem) -> RelatorioViagem:
    relatorio_ida: RelatorioViagem = await get_relatorio(viagem)
    if not viagem.ida_e_volta:
        return await identifica_origen_destino_e_percurso(relatorio_ida, viagem)
    viagem_volta: Viagem = invert_viagem(viagem)
    relatorio_volta: RelatorioViagem = await get_relatorio(viagem_volta)
    relatorio_ida_e_volta: RelatorioViagem = join_ida_e_volta(relatorio_ida=relatorio_ida, relatorio_volta=relatorio_volta)
    return await identifica_origen_destino_e_percurso(relatorio_ida_e_volta, viagem)
