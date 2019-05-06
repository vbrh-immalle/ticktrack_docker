from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    hostname = socket.gethostname() # We willen dat de webapplicatie de hostname van de server toont omdat meerdere Docker-instanties verschillende hostnames hebben
    return f"<p>Hello! (Being served from {hostname})</p>"


# Om onderscheid tussen docker en lokale ontwikkelomgeving (die op poort 8080 draait) te maken
port = 80
if socket.gethostname() == "xubimma":
    port = 8080

app.run(host="0.0.0.0", port=port)
