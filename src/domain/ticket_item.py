from pydantic import BaseModel


class TicketItem(BaseModel):
    quantity: float
    description: str
    unit_price: float | None
    total_price: float
