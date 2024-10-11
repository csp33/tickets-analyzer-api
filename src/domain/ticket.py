from pydantic import BaseModel

from src.domain.ticket_item import TicketItem


class Ticket(BaseModel):
    items: list[TicketItem]
