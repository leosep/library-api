from application.interfaces.renderer_interface import PageRenderer

class HTMLRenderer(PageRenderer):
    def render(self, content: str) -> str:
        return f"<html><body><p>{content}</p></body></html>"
