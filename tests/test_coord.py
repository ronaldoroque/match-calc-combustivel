from copy import copy

from fastapi.testclient import TestClient


class TestInsertCoord:
    payload = {
        "origem_longitude": -41.9480517645751,
        "origem_latitude": "-18,9047485170197",
        "destino_longitude": -41.953074390246016,
        "destino_latitude": -18.849342234646826,
        "ida_e_volta": False,
        "media_consumo_veiculo": 14,
    }

    def test_criar_relatorio_de_viagem(self, client: TestClient) -> None:
        response = client.post(f"/viagem", json=self.payload)
        assert response.status_code == 200

    def test_media_consumo_negativa(self, client: TestClient) -> None:
        payload_errado = self.payload.copy()
        payload_errado["media_consumo_veiculo"] = -14
        response = client.post(f"/viagem", json=payload_errado)
        payload_resp = response.json()
        assert response.status_code == 422
        assert "detail" in payload_resp

    def test_longitude_fora_limite(self, client: TestClient) -> None:
        payload_errado = self.payload.copy()
        payload_errado["origem_longitude"] = -182
        response = client.post(f"/viagem", json=payload_errado)
        payload_resp = response.json()
        assert response.status_code == 422
        assert "detail" in payload_resp

    def test_latitude_fora_limite(self, client: TestClient) -> None:
        payload_errado = self.payload.copy()
        payload_errado["origem_latitude"] = -92
        response = client.post(f"/viagem", json=payload_errado)
        payload_resp = response.json()
        assert response.status_code == 422
        assert "detail" in payload_resp

    def test_rota_impossivel(self, client: TestClient) -> None:
        payload_errado = self.payload.copy()
        payload_errado["origem_latitude"] = 18.9974329098728
        payload_errado["origem_longitude"] = 47.55946265902358
        response = client.post(f"/viagem", json=payload_errado)
        payload_resp = response.json()
        assert response.status_code == 422
        assert "detail" in payload_resp

    def test_mesmo_destino_e_origem(self, client: TestClient) -> None:
        payload_errado = self.payload.copy()
        payload_errado["origem_longitude"] = -41.953074390246016
        payload_errado["origem_latitude"] = -18.849342234646826
        response = client.post(f"/viagem", json=payload_errado)
        payload_resp = response.json()
        assert response.status_code == 400
        assert "detail" in payload_resp
