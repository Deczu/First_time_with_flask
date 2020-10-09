from controller import index_controller,rest_controller
from flask import render_template
from flask_restful import Resource,Api


def return_routes(app):
    api = Api(app)

    @app.route("/")
    def return_index():
        view, name = index_controller.render()
        return render_template(view ,name=name)

    def return_rest():
        rest = rest_controller.RestController()
        return rest.model
    api.add_resource(return_rest(),"/test")
