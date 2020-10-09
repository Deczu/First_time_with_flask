from controller import index_controller
from flask import render_template


def return_routes(app):
    @app.route("/")
    def return_index():
        view, name = index_controller.render()
        return render_template(view ,name=name)
