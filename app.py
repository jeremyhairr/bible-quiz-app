from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        questions = [
            {
                "question": "Why were many people looking for Jesus at the beginning of John 6?",
                "answer": "Because He had done miracles and fed them bread."
            },
            {
                "question": "What did Jesus say was the real reason they were looking for Him?",
                "answer": "They wanted more bread, not Him."
            },
            {
                "question": "What did Jesus call Himself in this chapter?",
                "answer": "The Bread of Life."
            },
            {
                "question": "What happened to the people in the Old Testament who ate manna in the wilderness?",
                "answer": "They eventually died."
            },
            {
                "question": "What does Jesus promise to people who believe in Him?",
                "answer": "Eternal life and that He will raise them up on the last day."
            },
            {
                "question": "When Jesus says He is the Bread of Life, does He mean real bread? Why or why not?",
                "answer": "No — He means He feeds and satisfies our hearts and souls."
            },
            {
                "question": "What happens to us if we don’t trust in Jesus?",
                "answer": "We don’t have eternal life in heaven."
            },
            {
                "question": "What does it mean to 'feed on' Jesus?",
                "answer": "To believe in Him, trust Him, depend on Him."
            },
            {
                "question": "Can we make ourselves believe in Jesus all by ourselves?",
                "answer": "No — God draws us."
            },
            {
                "question": "What does it mean when Jesus says the Father 'draws' people to Him?",
                "answer": "God shows them their sin and need of a Savior and gives them faith to believe."
            },
            {
                "question": "If someone truly comes to Jesus, what does Jesus promise He will never do?",
                "answer": "Never cast them out."
            },
            {
                "question": "Who keeps us safe in salvation — us or Jesus?",
                "answer": "Jesus keeps us."
            },
            {
                "question": "What does Jesus mean when He says He will 'raise us up on the last day'?",
                "answer": "One day He will bring believers back to life forever."
            }
        ]

        return render_template(
            "result.html",
            name=name,
            age=age,
            questions=questions
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)