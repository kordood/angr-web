import sys
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World"


if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    port = sys.argv[2] if len(sys.argv) > 2 else 5001

    if type(port) is str:
        port = int(port)

    app.run(host=host, port=port)
