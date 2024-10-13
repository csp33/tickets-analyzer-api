from pathlib import Path

from fastapi.testclient import TestClient


def test_process_mercadona_ticket(client: TestClient) -> None:
    filepath = str(Path(__file__).parent / "files" / "test_ticket.pdf")
    with open(filepath, "rb") as f:
        response = client.post(
            "/mercadona", files={"ticket_file": (filepath, f, "application/pdf")}
        )

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "description": "P.RELLENO PISTA/TRUF",
                "quantity": 1.0,
                "total_price": 2.15,
                "unit_price": 2.15,
            },
            {
                "description": "HELADO SANDWICH NATA",
                "quantity": 1.0,
                "total_price": 1.9,
                "unit_price": 1.9,
            },
            {
                "description": "CASTAÑA 500 GR",
                "quantity": 1.0,
                "total_price": 3.5,
                "unit_price": 3.5,
            },
            {
                "description": "XUXES TOP TEN",
                "quantity": 1.0,
                "total_price": 1.25,
                "unit_price": 1.25,
            },
            {
                "description": "TAGLIATELLE",
                "quantity": 1.0,
                "total_price": 1.15,
                "unit_price": 1.15,
            },
            {
                "description": "CROQUETA ESPINACAS",
                "quantity": 1.0,
                "total_price": 2.1,
                "unit_price": 2.1,
            },
            {
                "description": "PALOMIT. MANTEQUILLA",
                "quantity": 1.0,
                "total_price": 1.35,
                "unit_price": 1.35,
            },
            {
                "description": "ALBÓNDIGAS GUISADAS",
                "quantity": 1.0,
                "total_price": 2.75,
                "unit_price": 2.75,
            },
            {
                "description": "SALSA DE SETAS",
                "quantity": 1.0,
                "total_price": 1.65,
                "unit_price": 1.65,
            },
            {
                "description": "CHAPATA CRISTAL 4UDS",
                "quantity": 1.0,
                "total_price": 1.4,
                "unit_price": 1.4,
            },
        ],
        "timestamp": "2024-09-28T15:02:00",
    }
