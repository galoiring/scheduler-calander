from flask import Flask
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello():
    return 'Hello from Flask backend!'


@app.route('/list_test', methods=['GET'])
def list_datasets():
    return 'list of all the calanders'


if __name__ == '__main__':
    app.run(debug=True)
