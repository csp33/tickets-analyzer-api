from src.domain.parsers.file import FileParser
from src.domain.parsers.ticket import TicketParser
from src.domain.ticket import Ticket


class ParseTicketFileUseCase:
    def __init__(
        self,
        file_parser: FileParser,
        ticket_parser: TicketParser,
    ) -> None:
        self.__file_parser = file_parser
        self.__ticket_parser = ticket_parser

    def handle(self, ticket_filepath: str) -> Ticket:
        ticket_content = self.__file_parser.parse(ticket_filepath)
        return self.__ticket_parser.parse(ticket_content)
