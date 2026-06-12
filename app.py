import os
import json
from flask import Flask, render_template, request, redirect, url_for, session
from generator import generate_quiz
from history import save_score, load_scores
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic", "Cours BTS SIO")
        course_text = request.form.get("course_text", "").strip()
        num_questions = int(request.form.get("num_questions", 5))

        if not course_text:
            return render_template("index.html", error="Colle ton texte de cours avant de continuer.")

        questions = generate_quiz(course_text, num_questions)

        session["questions"] = questions
        session["topic"] = topic
        session["current"] = 0
        session["score"] = 0
        session["answers"] = []

        return redirect(url_for("quiz"))

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = session.get("questions", [])
    current = session.get("current", 0)

    if not questions or current >= len(questions):
        return redirect(url_for("results"))

    feedback = None

    if request.method == "POST":
        user_answer = request.form.get("answer")
        question = questions[current]
        correct = question["answer"]
        is_correct = user_answer == correct

        if is_correct:
            session["score"] = session.get("score", 0) + 1

        answers = session.get("answers", [])
        answers.append({
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": correct,
            "is_correct": is_correct,
            "explanation": question["explanation"],
            "choices": question["choices"]
        })
        session["answers"] = answers
        session["current"] = current + 1

        feedback = {
            "is_correct": is_correct,
            "correct_answer": correct,
            "correct_text": question["choices"][correct],
            "explanation": question["explanation"],
            "user_answer": user_answer
        }

        current = session["current"]
        if current >= len(questions):
            return redirect(url_for("results"))

    question = questions[current]
    return render_template(
        "quiz.html",
        question=question,
        number=current + 1,
        total=len(questions),
        feedback=feedback
    )


@app.route("/results")
def results():
    score = session.get("score", 0)
    answers = session.get("answers", [])
    topic = session.get("topic", "Quiz")
    total = len(answers)

    if total == 0:
        return redirect(url_for("index"))

    percentage = round((score / total) * 100)
    save_score(topic, score, total)

    return render_template("results.html", score=score, total=total,
                           percentage=percentage, answers=answers, topic=topic)


@app.route("/history")
def history():
    scores = load_scores()
    scores_reversed = list(reversed(scores))
    avg = round(sum(s["percentage"] for s in scores) / len(scores), 1) if scores else 0
    return render_template("history.html", scores=scores_reversed, avg=avg, total=len(scores))


if __name__ == "__main__":
    app.run(debug=True)
