from controller.model.index_model import Index


class IndexController:
    def __init__(self):
        self.template_name = "index.html"
        self.data = Index()
        self.name = self.data.name


def render():
    controller = IndexController()
    return controller.template_name, controller.name
