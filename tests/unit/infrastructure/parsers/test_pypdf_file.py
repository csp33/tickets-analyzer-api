import pytest
from unittest.mock import MagicMock, patch

from src.infrastructure.parsers.pypdf_file import PyPDFFileParser


@pytest.fixture
def pdf_file_parser() -> PyPDFFileParser:
    return PyPDFFileParser()


@patch("src.infrastructure.parsers.pypdf_file.PdfReader")
def test_parse(mock_pdf_reader: MagicMock, pdf_file_parser: PyPDFFileParser) -> None:
    filepath = "test_path"
    mock_pdf_instance = MagicMock()
    mock_pdf_reader.return_value = mock_pdf_instance

    result = pdf_file_parser.parse(filepath)

    assert result == mock_pdf_instance.pages[0].extract_text.return_value
    mock_pdf_reader.assert_called_once_with(filepath)
    mock_pdf_instance.pages[0].extract_text.assert_called_once_with(
        extraction_mode="layout"
    )
