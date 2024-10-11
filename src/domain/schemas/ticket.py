from datetime import datetime

from pydantic import BaseModel

from src.domain.schemas.ticket_item import TicketItem


class Ticket(BaseModel):
    timestamp: datetime
    items: list[TicketItem]
