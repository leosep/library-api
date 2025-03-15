from abc import ABC, abstractmethod

class PageRenderer(ABC):
    @abstractmethod
    def render(self, content: str) -> str:
        """Render the content into a specific format."""
        pass
