from abc import abstractmethod, ABC

from src.domain.ticket import Ticket


class TicketParser(ABC):
    @abstractmethod
    def parse(self, ticket_text: str) -> Ticket:
        pass
