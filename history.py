import json
import os
from datetime import datetime

SCORES_FILE = "data/scores.json"


def load_scores() -> list[dict]:
    """Charge l'historique des scores depuis le fichier JSON."""
    if not os.path.exists(SCORES_FILE):
        return []

    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_score(topic: str, score: int, total: int):
    """
    Sauvegarde un score dans l'historique.

    Args:
        topic: Le sujet du cours révisé
        score: Nombre de bonnes réponses
        total: Nombre total de questions
    """
    os.makedirs("data", exist_ok=True)
    scores = load_scores()

    entry = {
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "topic": topic,
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100, 1),
    }

    scores.append(entry)

    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


def display_history():
    """Affiche l'historique complet des scores."""
    scores = load_scores()

    print("=" * 60)
    print("  📊 HISTORIQUE DES SCORES")
    print("=" * 60)

    if not scores:
        print("\n  Aucun score enregistré pour l'instant.")
        print("  Lance un quiz pour commencer !\n")
        return

    print()
    for i, entry in enumerate(reversed(scores[-10:]), 1):
        percentage = entry["percentage"]
        icon = "🌟" if percentage >= 80 else "👍" if percentage >= 60 else "📚"
        print(
            f"  {icon} {entry['date']} | {entry['topic'][:25]:<25} | "
            f"{entry['score']}/{entry['total']} ({percentage}%)"
        )

    print()
    if len(scores) > 0:
        avg = sum(s["percentage"] for s in scores) / len(scores)
        print(f"  📈 Moyenne générale : {avg:.1f}%")
        print(f"  🎯 Total de quiz complétés : {len(scores)}")
    print()
