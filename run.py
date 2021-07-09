from flask import Flask
import time
time.strftime("%H:%M:%S")

app = Flask(__name__)

@app.route("/")
def mostrar_hora():
    hora=time.strftime("%X")
    return "La hora actual es {}". format(hora)
