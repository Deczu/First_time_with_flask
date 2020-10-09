from flask import Flask
from routes import return_routes

import os

app = Flask("My_app",template_folder=os.path.join(os.getcwd(),'controller','view'))
return_routes(app)


if __name__ == "__main__":
    app.run(debug=True)
