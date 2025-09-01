from flask import Flask, render_template
import slaves as slave

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("daily.html", articles=slave.fetch_json("news.json"))
@app.route("/daily")
def daily():
    return render_template("daily.html", articles=slave.fetch_json("news.json"))

@app.route("/weekly")
def weekly():
    return render_template("weekly.html", articles=slave.fetch_json("news.json"))

if __name__ == "__main__":
    # run locally at http://127.0.0.1:5000
    app.run(debug=True)
