import re

from src.domain.parsers.ticket import TicketParser
from src.domain.ticket import Ticket
from src.domain.ticket_item import TicketItem


class MercadonaTicketParser(TicketParser):
    __REGULAR_ITEM_PATTERN = re.compile(
        r"^(\d+)\s+(.+?)\s+((\d+,\d{2})?\s+)?(\d+,\d{2})$"
    )
    __WEIGHTED_ITEM_PATTERN = re.compile(
        r"^(\d+,\d{3})\s*kg\s*(\d+,\d{2})\s*€/kg\s*(\d+,\d{2})$"
    )
    __WEIGHTED_ITEM_DESCRIPTION_PATTERN = re.compile(r"^\s*(\d+)\s+(.+)$")
    __WEIGHTED_ITEM_FALLBACK_DESCRIPTION = "Unknown"
    __ITEMS_TO_IGNORE = ["PARKING"]

    def __parse_regular_item(self, match: re.Match[str]) -> TicketItem:
        quantity = int(match.group(1))
        description = match.group(2).strip()
        total_price = float(match.group(5).replace(",", "."))
        unit_price = (
            float(match.group(4).replace(",", "."))
            if match.group(4)
            else total_price / quantity
        )
        return TicketItem(
            quantity=quantity,
            description=description,
            unit_price=unit_price,
            total_price=total_price,
        )

    def __parse_weighted_item(
        self, match: re.Match[str], description: str | None
    ) -> TicketItem:
        quantity = float(match.group(1).replace(",", "."))
        unit_price = float(match.group(2).replace(",", "."))
        total_price = float(match.group(3).replace(",", "."))
        description = (
            description
            if description is not None
            else self.__WEIGHTED_ITEM_FALLBACK_DESCRIPTION
        )
        return TicketItem(
            quantity=quantity,
            description=description,
            unit_price=unit_price,
            total_price=total_price,
        )

    def parse(self, ticket_text: str) -> Ticket:
        items = []
        lines = ticket_text.splitlines()
        last_description = None

        for line in map(str.strip, lines):
            if any([ignored_item in line for ignored_item in self.__ITEMS_TO_IGNORE]):
                continue
            if regular_item_match := self.__REGULAR_ITEM_PATTERN.match(line):
                items.append(self.__parse_regular_item(regular_item_match))
                last_description = None
                continue

            if (
                weighted_item_description_match
                := self.__WEIGHTED_ITEM_DESCRIPTION_PATTERN.match(line)
            ):
                last_description = weighted_item_description_match.group(2).strip()
                continue

            if weighted_item_item_match := self.__WEIGHTED_ITEM_PATTERN.match(line):
                items.append(
                    self.__parse_weighted_item(
                        match=weighted_item_item_match, description=last_description
                    )
                )
                last_description = None

        return Ticket(items=items)
