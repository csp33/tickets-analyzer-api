import traceback
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status

from src.application.parse_ticket_file import ParseTicketFileUseCase
from src.domain.ticket import Ticket
from src.infrastructure.parsers.pypdf_file import PyPDFFileParser
from src.infrastructure.parsers.mercadona_ticket_parser import MercadonaTicketParser

router = APIRouter()


@router.post("/")
async def process_mercadona_ticket(
    ticket_file: UploadFile = File(media_type="application/pdf"),
) -> Ticket:
    use_case = ParseTicketFileUseCase(
        file_parser=PyPDFFileParser(), ticket_parser=MercadonaTicketParser()
    )

    with NamedTemporaryFile(suffix=".pdf") as temp_file:
        temp_file.write(ticket_file.file.read())
        try:
            return use_case.handle(temp_file.file.name)
        except Exception:
            traceback.print_exc()
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid PDF"
            )
