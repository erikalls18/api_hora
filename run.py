from flask import Flask
import time
time.strftime("%H:%M:%S")

app = Flask(__name__)

@app.route("/")
def mostrar_hora():
    hora=time.strftime("%X")
    return "La hora actual es {}". format(hora)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)