from ctypes import Union
import locale
from typing import Optional, Union

from pydantic import BaseModel, validator

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
format_decimal = "%.{0:d}f".format(2)


class Viagem(BaseModel):
    origem_longitude: float
    origem_latitude: float
    destino_longitude: float
    destino_latitude: float
    ida_e_volta: Optional[bool] = False
    media_consumo_veiculo: float

    def coodernadas(self):
        return f"{self.origem_longitude},{self.origem_latitude};{self.destino_longitude},{self.destino_latitude}"


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

    def float_to_str_br(self, valor: float) -> str:
        return locale.format_string(format_decimal, valor, grouping=True, monetary=False)

    def float_rounded(self, valor: float) -> float:
        return round(valor, 2)

    def format(self) -> dict[str]:
        distancia_km_str_br: str = self.float_to_str_br(self.float_rounded(self.distancia_km))
        vias_da_rota_str: str = ", ".join(self.vias_da_rota)
        consumo_total_de_combustivel_str_br: str = self.float_to_str_br(self.float_rounded(self.consumo_total_de_combustivel))
        result = {
            'distancia_km': distancia_km_str_br,
            'vias_da_rota': vias_da_rota_str,
            'consumo_total_de_combustivel': consumo_total_de_combustivel_str_br,
        }
        return result