from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        question = "Why were many people looking for Jesus at the beginning of John 6?"
        answer = "Because He had done miracles and fed them bread."

        question = "What did Jesus say was the real reason they were looking for Him?"
        answer = "They wanted more bread, not Him."

        question = "What did Jesus call Himself in this chapter?"
        answer = "The Bread of Life."

        question = "What happened to the people in the Old Testament who ate manna in the wilderness?"
        answer = "They eventually died."

        question = "What does Jesus promise to people who believe in Him?"
        answer = "Eternal life and that He will raise them up on the last day."

        question = "In John 6:44..."
        answer = "Salvation is of the Lord..."

        return render_template(
            "result.html",
            name=name,
            age=age,
            question=question,
            answer=answer
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)