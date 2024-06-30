from flask import Flask, jsonify

server = Flask(__name__)


@server.route("/")
def home():
    return "Hello, World"


@server.route("/api/data")
def get_data():
    data = {"message": "hello, API!", "data": [1, 2, 3, 4, 5]}
    return jsonify(data)


@server.route("/contact")
def contact():
    return "Thanks for Contacting us, How Can we Help you."


if __name__ == "__main__":
    server.run(debug=True)
