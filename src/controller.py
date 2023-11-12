from fastapi import Request, Form, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates

from .mapbox_api import *

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.post("/distance", response_class=HTMLResponse)
async def distance(request: Request, viagem: Viagem):
    relatorio_viagem: RelatorioViagem = await calcula_viagem(viagem)
    relatorio_viagem_formatado: dict = relatorio_viagem.format()
    return templates.TemplateResponse("item.html", {"request": request, **relatorio_viagem_formatado})


@router.get("/home_html", response_class=HTMLResponse)
async def home_view_get(request: Request):
    dados_viajem_view = RelatorioViagem()
    return templates.TemplateResponse("home.html", {"request": request, "dados_viajem": dados_viajem_view})


@router.post("/home_html", response_class=HTMLResponse)
async def home_view_with_post(request: Request, origem_longitude: float = Form(...), origem_latitude: float = Form(...),
                    destino_longitude: float = Form(...), destino_latitude: float = Form(...),
                    media_consumo_veiculo: float = Form(...), ida_e_volta: bool = Form(...)):
    viagem = Viagem(origem_longitude=origem_longitude, origem_latitude=origem_latitude, destino_longitude=destino_longitude,
                    destino_latitude=destino_latitude, media_consumo_veiculo=media_consumo_veiculo, ida_e_volta=ida_e_volta)
    relatorio_viagem: RelatorioViagem = await calcula_viagem(viagem)
    relatorio_viagem_formatado: dict = relatorio_viagem.format()
    return templates.TemplateResponse("home.html", {"request": request, **relatorio_viagem_formatado})


@router.post("/viagem", response_class=JSONResponse)
async def post_data_viagem(viagem: Viagem) -> dict:
    """ Obter um relatório da viagem """
    relatorio_viagem: RelatorioViagem = await calcula_viagem(viagem)
    relatorio_viagem_formatado: dict = relatorio_viagem.format()
    return relatorio_viagem_formatado


@router.get("/destino_imagem", response_class=Response)
async def destino_imagem(origem_longitude: float, origem_latitude, destino_longitude: float, destino_latitude: float, geometry: Optional[str] = None) -> Response:
    """ Obtem a imagem do mapa pela API do Mapbox """
    coordenadas = Coordenadas(origem_longitude=origem_longitude, origem_latitude=origem_latitude,
                              destino_longitude=destino_longitude, destino_latitude=destino_latitude, geometry=geometry)
    return await get_map_image(coordenadas=coordenadas)
