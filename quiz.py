import os


def clear_screen():
    """Efface le terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def display_question(question: dict, number: int, total: int) -> str:
    """
    Affiche une question et récupère la réponse de l'utilisateur.

    Args:
        question: Dictionnaire contenant la question, choix et réponse
        number: Numéro de la question courante
        total: Nombre total de questions

    Returns:
        La réponse saisie par l'utilisateur (A, B, C ou D)
    """
    clear_screen()
    print("=" * 60)
    print(f"  📚 QUIZGEN SIO — Question {number}/{total}")
    print("=" * 60)
    print()
    print(f"❓ {question['question']}")
    print()

    for letter, choice in question["choices"].items():
        print(f"   {letter}) {choice}")

    print()
    print("-" * 60)

    while True:
        answer = input("👉 Ta réponse (A/B/C/D) : ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("⚠️  Saisis uniquement A, B, C ou D")


def show_answer_feedback(question: dict, user_answer: str) -> bool:
    """
    Affiche le feedback après une réponse.

    Args:
        question: La question avec la bonne réponse
        user_answer: La réponse de l'utilisateur

    Returns:
        True si la réponse est correcte, False sinon
    """
    correct = question["answer"]
    is_correct = user_answer == correct

    print()
    if is_correct:
        print("✅ BONNE RÉPONSE !")
    else:
        print(f"❌ Mauvaise réponse. La bonne réponse était : {correct}")
        print(f"   → {question['choices'][correct]}")

    print()
    print(f"💡 Explication : {question['explanation']}")
    print()
    input("Appuie sur Entrée pour continuer...")

    return is_correct


def run_quiz(questions: list[dict]) -> dict:
    """
    Lance le quiz complet et retourne les résultats.

    Args:
        questions: Liste des questions générées

    Returns:
        Dictionnaire avec score, total et détail des réponses
    """
    score = 0
    total = len(questions)
    results = []

    for i, question in enumerate(questions, 1):
        user_answer = display_question(question, i, total)
        is_correct = show_answer_feedback(question, user_answer)

        if is_correct:
            score += 1

        results.append(
            {
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": question["answer"],
                "is_correct": is_correct,
            }
        )

    return {"score": score, "total": total, "results": results}


def display_score(quiz_result: dict, topic: str):
    """
    Affiche le score final du quiz.

    Args:
        quiz_result: Résultat du quiz avec score et total
        topic: Le sujet du cours révisé
    """
    clear_screen()
    score = quiz_result["score"]
    total = quiz_result["total"]
    percentage = (score / total) * 100

    print("=" * 60)
    print("  🏁 RÉSULTATS FINAUX")
    print("=" * 60)
    print()
    print(f"  📖 Sujet : {topic}")
    print(f"  ✅ Score : {score}/{total} ({percentage:.0f}%)")
    print()

    if percentage >= 80:
        print("  🌟 Excellent ! Tu maîtrises bien ce sujet !")
    elif percentage >= 60:
        print("  👍 Bien ! Encore quelques révisions et ce sera parfait.")
    elif percentage >= 40:
        print("  📚 Continue à réviser, tu progresses !")
    else:
        print("  💪 Ne lâche pas ! Relis ton cours et réessaie.")

    print()
    print("  📊 Détail des réponses :")
    print("-" * 60)
    for i, result in enumerate(quiz_result["results"], 1):
        icon = "✅" if result["is_correct"] else "❌"
        print(f"  {icon} Q{i}: {result['question'][:45]}...")

    print()
