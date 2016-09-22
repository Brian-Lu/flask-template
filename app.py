from flask import Flask, render_template
from occupations import convertDict, picker, occupations
app = Flask(__name__)
@app.route("/")
def index():
    return "<a href = '/occupations'>Occupations</a>"
dict = convertDict("occupations.csv")
valueList = []
keyList = []
for item in dict:
    keyList.append(item)
    valueList.append(item)
@app.route("/occupations")
def occupation():
    return render_template("occupations.html", keyList = keyList, valueList = valueList)


if __name__ == "__main__":
    app.run()
        
