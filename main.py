from flask import Flask, jsonify

app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 6969

app = Flask(__name__)

version = {
"version": "0.0.1",
"title": "Jogo do Caboclo"
}

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/api/metadata", methods=["GET"])
def get_tasks():
    return jsonify({"metadata: ": version})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)