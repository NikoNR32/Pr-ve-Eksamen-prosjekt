from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def forside():
    return render_template("Forside.html")


@app.route("/produkter")
def produkter():
    return "Her skal produktsiden være"


@app.route("/login")
def login():
    return "Her skal innlogging være"


@app.route("/handlekurv")
def handlekurv():
    return "Her skal handlekurven være"


@app.route("/produkt/<int:produkt_id>")
def produkt(produkt_id):
    return f"Du ser på produkt med ID {produkt_id}"


@app.route("/sok")
def sok():
    q = request.args.get("q")
    return f"Du søkte etter: {q}"


if __name__ == "__main__":
    app.run(debug=True)