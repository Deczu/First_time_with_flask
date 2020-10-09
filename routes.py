from controller import index_controller
from flask import render_template
from flask_restful import Resource,Api


def return_routes(app):
    api = Api(app)

    @app.route("/")
    def return_index():
        view, name = index_controller.render()
        return render_template(view ,name=name)

    class Test(Resource):
        def get(self):
            return {"asd": 123}
    api.add_resource(Test,"/test")
