from flask import Flask
from flask_restplus import Api 

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,  
            version='1.0',
            title='Api Sensor',
            description='Sensor Fox',
            doc='/docs'

        )

    def rub(self,):
        self.app.run(
            debug=True
        )     

server = Server()