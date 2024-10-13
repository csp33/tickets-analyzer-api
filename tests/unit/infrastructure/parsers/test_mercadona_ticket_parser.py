from datetime import datetime
from typing import Any

import pytest

from src.domain.schemas.ticket import Ticket
from src.domain.schemas.ticket_item import TicketItem
from src.infrastructure.parsers.mercadona_ticket_parser import MercadonaTicketParser


@pytest.fixture
def mercadona_ticket_parser() -> MercadonaTicketParser:
    return MercadonaTicketParser()


test_cases = {
    "Regular items": {
        "ticket_lines": [
            "12/10/2024 12:30",
            "4 ARENA AGLOMERANTE                      3,75        15,00",
            "1 PAN CENTENO 51 %                                    1,55",
            "1 C. AMARILLA BANDEJA                                 1,73",
            "1 DUO CANONIGOS RUCULA                                1,38",
        ],
        "expected_ticket": Ticket(
            timestamp=datetime(2024, 10, 12, 12, 30),
            items=[
                TicketItem(
                    quantity=4,
                    description="ARENA AGLOMERANTE",
                    unit_price=3.75,
                    total_price=15,
                ),
                TicketItem(
                    quantity=1,
                    description="PAN CENTENO 51 %",
                    unit_price=1.55,
                    total_price=1.55,
                ),
                TicketItem(
                    quantity=1,
                    description="C. AMARILLA BANDEJA",
                    unit_price=1.73,
                    total_price=1.73,
                ),
                TicketItem(
                    quantity=1,
                    description="DUO CANONIGOS RUCULA",
                    unit_price=1.38,
                    total_price=1.38,
                ),
            ],
        ),
    },
    "Weighted items": {
        "ticket_lines": [
            "12/10/2024 12:30",
            "1 PLATANO",
            "0,526 kg                     1,95 €/kg         1,03",
            "1 MANZ. ROJA DULCE",
            "1,080 kg                     2,00 €/kg         2,16",
        ],
        "expected_ticket": Ticket(
            timestamp=datetime(2024, 10, 12, 12, 30),
            items=[
                TicketItem(
                    quantity=0.526,
                    description="PLATANO",
                    unit_price=1.95,
                    total_price=1.03,
                ),
                TicketItem(
                    quantity=1.08,
                    description="MANZ. ROJA DULCE",
                    unit_price=2.0,
                    total_price=2.16,
                ),
            ],
        ),
    },
    "Ignored Parking": {
        "ticket_lines": [
            "12/10/2024 12:30",
            "1 DUO CANONIGOS RUCULA                                1,38",
            "1 PARKING                                              0,00",
        ],
        "expected_ticket": Ticket(
            timestamp=datetime(2024, 10, 12, 12, 30),
            items=[
                TicketItem(
                    quantity=1,
                    description="DUO CANONIGOS RUCULA",
                    unit_price=1.38,
                    total_price=1.38,
                ),
            ],
        ),
    },
}


@pytest.mark.parametrize(
    argnames="tc", argvalues=test_cases.values(), ids=test_cases.keys()
)
def test_parse_items(
    mercadona_ticket_parser: MercadonaTicketParser, tc: dict[str, Any]
) -> None:
    ticket = mercadona_ticket_parser.parse("\n".join(tc["ticket_lines"]))

    assert ticket == tc["expected_ticket"]
