from abc import ABC, abstractmethod
from typing import List
from tool import Tool


class AssistantContext(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_instructions(self) -> str:
        pass

    @abstractmethod
    def get_tools(self) -> List[Tool]:
        pass

    @abstractmethod
    def get_completed_tool(self) -> Tool:
        pass
    