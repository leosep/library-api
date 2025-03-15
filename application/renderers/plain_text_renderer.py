from application.interfaces.renderer_interface import PageRenderer

class PlainTextRenderer(PageRenderer):
    def render(self, content: str) -> str:
        return content
