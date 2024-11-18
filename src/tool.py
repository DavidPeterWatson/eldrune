
from abc import ABC, abstractmethod
from typing import List

# AI Provider classes remain the same as before
class Tool(ABC):

    def get_name(self) -> str:
        return self.get_definition()['function']['name']

    @abstractmethod
    def get_definition(self) -> object:
        pass

    @abstractmethod
    def use(self, arguments):
        pass
