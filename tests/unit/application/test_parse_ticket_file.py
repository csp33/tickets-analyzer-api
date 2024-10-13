from unittest.mock import Mock

import pytest

from src.application.parse_ticket_file import ParseTicketFileUseCase
from src.domain.parsers.file import FileParser
from src.domain.parsers.ticket import TicketParser


@pytest.fixture
def mock_file_parser():
    return Mock(spec=FileParser)


@pytest.fixture
def mock_ticket_parser():
    return Mock(spec=TicketParser)


@pytest.fixture
def parse_ticket_file_use_case(
    mock_file_parser: Mock, mock_ticket_parser: Mock
) -> ParseTicketFileUseCase:
    return ParseTicketFileUseCase(mock_file_parser, mock_ticket_parser)


def test_handle(
    parse_ticket_file_use_case: ParseTicketFileUseCase,
    mock_file_parser: Mock,
    mock_ticket_parser: Mock,
) -> None:
    ticket_filepath = "path/to/ticket/file"
    use_case = ParseTicketFileUseCase(mock_file_parser, mock_ticket_parser)

    result = use_case.handle(ticket_filepath)

    assert result == mock_ticket_parser.parse.return_value
    mock_file_parser.parse.assert_called_once_with(ticket_filepath)
    mock_ticket_parser.parse.assert_called_once_with(
        mock_file_parser.parse.return_value
    )
