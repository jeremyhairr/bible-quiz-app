from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        questions = [
            {
                "question": "Where was Jesus traveling in John 7:1?",
                "choices": [
                    "A. Judea",
                    "B. Galilee",
                    "C. Egypt",
                    "D. Rome"
                ],
                "answer": "B"
            },

            {
                "question": "Why did Jesus avoid traveling in Judea?",
                "choices": [
                    "A. It was too crowded",
                    "B. The weather was bad",
                    "C. The Jewish leaders wanted to kill him.",
                    "D. His disciples told Him not to go. "
                ],
                "answer": "C"
            },
            {
                "question": "What festival was near in John 7?",
                "choices": [
                    "A. Passover",
                    "B. Pentecost",
                    "C. Festival of Booths (Tabernacles)",
                    "D. Day of Atonement"
                ],
                "answer": "C"
            },
            {
                "question": "What did the Festival of Booths celebrate",
                "choices": [
                    "A. David beating Goliath.",
                    "B. God's provision and the harvest",
                    "C. The building of the temple",
                    "D. The birth of Moses"
                ],
                "answer": "B"
            },
            {
                "question": "During the Festival of Booths, what did people live in?",
                "choices": [
                    "A. Tents or booths",
                    "B. boats",
                    "C. caves",
                    "D. stone houses"
                ],
                "answer": "A"
            },
            {
                "question": "Did Jesus’ brothers believe in Him at this time?",
                "choices": [
                    "A. Yes",
                    "B. No"

                ],
                "answer": "B"
            },
            {
                "question": "What did Jesus’ brothers tell Him to do?",
                "choices": [
                    "A. Leave Galilee and go to the festival publicly",
                    "B. Stay hidden in Galilee",
                    "C. Return to Nazareth",
                    "D. Go preach in Nineveh"
                ],
                "answer": "A"
            },
            {
                "question": "What did Jesus say about His time",
                "choices": [
                    "A. It had already come",
                    "B. It would never come",
                    "C. His time had not yet come",
                    "D. He did not know the time"
                ],
                "answer": "C"
            },
            {
                "question": "Why did the world hate Jesus?",
                "choices": [
                    "A. Because He traveled a lot",
                    "B. Because He testified that its works were evil",
                    "C. Because He healed people",
                    "D. Because He was from Rome"
                ],
                "answer": "B"
            },
            {
                "question": "Did Jesus eventually go to the festival?",
                "choices": [
                    "A. Yes, but secretly",
                    "B. No, He stayed in Galilee",
                    "C. Yes, with a large crowd",
                    "D. Yes, with His brothers"
                ],
                "answer": "A"
            },

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