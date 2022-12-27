from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        "id": 1,
        "library": "Pandas",
        "language": "Python"
    },
    {
        "id": 2,
        "library": "requests",
        "language": "Python"
    },
    {
        "id": 3,
        "library": "NumPy",
        "language": "Python"
    }
]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api', methods=['GET'])
def get_api():  # put application's code here
    return jsonify(data)


if __name__ == '__main__':
    app.run()
