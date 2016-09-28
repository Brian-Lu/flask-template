from flask import Flask, render_template
from utils import occupations
app = Flask(__name__)
@app.route("/")
def index():
    return "<a href = '/occupations'>Occupations</a>"

@app.route("/occupations")
def occupation():
    occupationsDict = occupations.convertDict("data/occupations.csv")
    job = occupations.occupations()
    helpfulLink = occupationsDict[job][1]
    return render_template("occupations.html", occupationsDict = occupationsDict, job = job, helpfulLink = helpfulLink)

if __name__ == "__main__":
    app.run()
        
