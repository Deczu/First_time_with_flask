from flask_restful import Resource


class RestModel(Resource):
    def __init__(self):
        self.data = {"Test_data":"Here add some DB querry or smthing"}

    def get(self):
        return self.data
