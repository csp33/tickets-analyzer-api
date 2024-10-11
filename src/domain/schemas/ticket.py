from pydantic import BaseModel

from src.domain.schemas.ticket_item import TicketItem


class Ticket(BaseModel):
    items: list[TicketItem]
