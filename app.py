from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        questions = [
            {
                "question": "What book of the Bible is this story from?",
                "choices": [
                    "A. Matthew",
                    "B. John",
                    "C. Acts",
                    "D. Romans"
                ],
                "answer": "B"
            },
            {
                "question": "What did many people say about Jesus' teaching?",
                "choices": [
                    "A. It was funny",
                    "B. It was confusing",
                    "C. It was hard to accept",
                    "D. It was boring"
                ],
                "answer": "C"
            },
            {
                "question": "What does the word 'disciple' mean?",
                "choices": [
                    "A. A king",
                    "B. A follower or learner",
                    "C. A soldier",
                    "D. A prophet"
                ],
                "answer": "B"
            },
            {
                "question": "Did every disciple who followed Jesus truly believe in Him?",
                "choices": [
                    "A. Yes, all of them did",
                    "B. No, some only followed for a time",
                    "C. Only the children believed",
                    "D. Only the Pharisees believed"
                ],
                "answer": "B"
            },
            {
                "question": "What gives people spiritual life according to Jesus?",
                "choices": [
                    "A. Good works",
                    "B. Being rich",
                    "C. The Spirit of God",
                    "D. Being popular"
                ],
                "answer": "C"
            },
            {
                "question": "What happened when many people heard Jesus' difficult teaching?",
                "choices": [
                    "A. They clapped",
                    "B. They left and stopped following Him",
                    "C. They built Him a house",
                    "D. They gave Him gifts"
                ],
                "answer": "B"
            },
            {
                "question": "When many people left, what question did Jesus ask the twelve disciples?",
                "choices": [
                    "A. Do you understand everything?",
                    "B. Do you want to go away too?",
                    "C. Will you build a church?",
                    "D. Will you feed the crowd?"
                ],
                "answer": "B"
            },
            {
                "question": "Who answered Jesus on behalf of the disciples?",
                "choices": [
                    "A. John",
                    "B. Matthew",
                    "C. Peter",
                    "D. Andrew"
                ],
                "answer": "C"
            },
            {
                "question": "What did Peter say Jesus has?",
                "choices": [
                    "A. The best stories",
                    "B. The words of eternal life",
                    "C. The most friends",
                    "D. The biggest house"
                ],
                "answer": "B"
            },
            {
                "question": "According to Peter, who is Jesus?",
                "choices": [
                    "A. A great teacher only",
                    "B. The Holy One of God",
                    "C. A good helper",
                    "D. A prophet only"
                ],
                "answer": "B"
            },
            {
                "question": "What is an important truth this passage teaches about following Jesus?",
                "choices": [
                    "A. Following Jesus is always easy",
                    "B. Only adults should follow Jesus",
                    "C. Sometimes following Jesus is hard",
                    "D. Following Jesus makes you rich"
                ],
                "answer": "C"
            },
            {
                "question": "Who did John say would betray Jesus?",
                "choices": [
                    "A. Peter",
                    "B. Judas",
                    "C. John",
                    "D. Thomas"
                ],
                "answer": "B"
            },
            {
                "question": "Even though Judas followed Jesus, what was true about him?",
                "choices": [
                    "A. He truly loved Jesus",
                    "B. He was the best disciple",
                    "C. He did not truly believe",
                    "D. He never heard Jesus teach"
                ],
                "answer": "C"
            },
            {
                "question": "According to the sermon, what two things really matter to Jesus?",
                "choices": [
                    "A. Having the biggest crowd",
                    "B. Believing and being a faithful follower of His",
                    "C. Having the most money",
                    "D. Having the loudest music"
                ],
                "answer": "B"
            },
            {
                "question": "What is the big question this passage asks us?",
                "choices": [
                    "A. Will we be famous?",
                    "B. Will we walk away from Jesus or stay with Him?",
                    "C. Will we become kings?",
                    "D. Will we travel the world?"
                ],
                "answer": "B"
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