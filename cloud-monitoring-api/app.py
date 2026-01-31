from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="Cloud Monitoring API", version="1.0", description="Testing Flask + Swagger")

ns = api.namespace('health', description='Health checks')

@ns.route('/')
class Health(Resource):
    def get(self):
        return {"status": "UP", "message": "Flask API is working"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
