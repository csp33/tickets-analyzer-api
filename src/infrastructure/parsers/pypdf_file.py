from typing import Literal

from pypdf import PdfReader

from src.domain.parsers.file import FileParser


class PyPDFFileParser(FileParser):
    __EXTRACTION_MODE: Literal["plain", "layout"] = "layout"

    def parse(self, filepath: str) -> str:
        pdf = PdfReader(filepath)
        return pdf.pages[0].extract_text(extraction_mode=self.__EXTRACTION_MODE)
