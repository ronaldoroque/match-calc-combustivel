from copy import copy

from fastapi.testclient import TestClient


class TestInsertCoord:
    payload = {
        "origem_longitude": -41.9480517645751,
        "origem_latitude": -18.9047485170197,
        "destino_longitude": -41.96912319730861,
        "destino_latitude": -18.827914896778022,
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

    def test_criar_relatorio_de_viagem_(self, client: TestClient) -> None:
        response = client.post(f"/viagem", json=self.payload)
        assert response.status_code == 200
