from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        question = "In John 6:44, Jesus says, 'No one comes to the Father unless He first draws them.' Does this mean that salvation is of the Lord?"
        answer = "Salvation is of the Lord. Paul says in Ephesians 2 that salvation is of the Lord so that no one can boast."

        return render_template("result.html", name=name, age=age, question=question, answer=answer)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)