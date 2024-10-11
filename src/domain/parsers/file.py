from abc import ABC, abstractmethod


class FileParser(ABC):
    @abstractmethod
    def parse(self, filepath: str) -> str:
        pass
