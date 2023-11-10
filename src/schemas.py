from ctypes import Union
import locale
from http import HTTPStatus
from typing import Optional, Union

from fastapi import HTTPException
from fastapi.logger import logger
from pydantic import BaseModel, validator

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
format_decimal = "%.{0:d}f".format(2)


class Viagem(BaseModel):
    origem_longitude: Union[float, str]
    origem_latitude: Union[float, str]
    destino_longitude: Union[float, str]
    destino_latitude: Union[float, str]
    ida_e_volta: Optional[bool] = False
    media_consumo_veiculo: Union[float, str]

    def get_coodernadas_to_str(self):
        return f"{self.origem_longitude},{self.origem_latitude};{self.destino_longitude},{self.destino_latitude}"

    @validator('origem_longitude', 'origem_latitude', 'destino_longitude', 'destino_latitude', 'media_consumo_veiculo')
    def str_to_float(cls, v):
        if isinstance(v, str):
            v = float(v.replace(",", "."))
            return v
        return v

    @validator('origem_longitude', 'destino_longitude')
    def longitude_limite(cls, v):
        if v > 180 or v < -180:
            mess = 'Verifique se os valores de Longitude foram digitados corretamente.'
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=mess)
        return v

    @validator('origem_latitude', 'destino_latitude')
    def latitude_limite(cls, v):
        if v > 90 or v < -90:
            mess = 'Verifique se os valores de Latitude foram digitados corretamente.'
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=mess)
        return v

    @validator('media_consumo_veiculo')
    def media_consumo_limite(cls, v):
        if v <= 0:
            mess = 'A média de consumo deve ser maior que zero.'
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=mess)
        return v


class Leg(BaseModel):
    via_waypoints: list
    admins: list
    weight: float
    duration: float
    steps: list
    distance: float
    summary: Union[list[str], str]

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


class RelatorioViagem(BaseModel):
    distancia_km: Optional[float] = None
    vias_da_rota: Optional[list[str]] = []
    consumo_total_de_combustivel: Optional[float] = None
    ida_e_volta: Optional[bool] = False

    def float_to_str_br(self, valor: float) -> str:
        return locale.format_string(format_decimal, valor, grouping=True, monetary=False)

    def float_rounded(self, valor: float) -> float:
        return round(valor, 2)

    def format(self) -> dict[str]:
        distancia_km_str_br: str = self.float_to_str_br(self.float_rounded(self.distancia_km))
        # vias_da_rota_str: str = ", ".join(self.vias_da_rota)
        consumo_total_de_combustivel_str_br: str = self.float_to_str_br(self.float_rounded(self.consumo_total_de_combustivel))
        result = {
            'distancia_km': distancia_km_str_br,
            'vias_da_rota': self.vias_da_rota,
            'consumo_total_de_combustivel': consumo_total_de_combustivel_str_br,
            'ida_e_volta': self.ida_e_volta,
        }
        return result