from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"<p>Hello! (Being served from {hostname})</p>"


port = 80
if socket.gethostname() == "xubimma":
    port = 8080

app.run(host="0.0.0.0", port=port)
