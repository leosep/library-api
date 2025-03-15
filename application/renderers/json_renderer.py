from application.interfaces.renderer_interface import PageRenderer

class JsonRenderer(PageRenderer):
    def render(self, content: str) -> str:
         return {"content": content}
