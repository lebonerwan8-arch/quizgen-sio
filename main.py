import os
import sys
from generator import generate_quiz
from quiz import run_quiz, display_score
from history import save_score, display_history


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    """Affiche le menu principal."""
    clear_screen()
    print("=" * 60)
    print("  🎓 QUIZGEN SIO — Révise ton BTS SIO avec l'IA")
    print("=" * 60)
    print()
    print("  1. 📝 Générer un quiz depuis mon cours")
    print("  2. 📊 Voir mon historique de scores")
    print("  3. 🚪 Quitter")
    print()
    print("-" * 60)


def get_course_input() -> tuple[str, str]:
    """
    Récupère le texte du cours et le sujet depuis l'utilisateur.

    Returns:
        Tuple (topic, course_text)
    """
    clear_screen()
    print("=" * 60)
    print("  📖 NOUVEAU QUIZ")
    print("=" * 60)
    print()

    topic = input("📌 Sujet du cours (ex: POO Python, SQL, Réseaux...) : ").strip()
    if not topic:
        topic = "Cours BTS SIO"

    print()
    print("📄 Colle ton texte de cours ci-dessous.")
    print("   (Tape 'FIN' sur une nouvelle ligne quand tu as terminé)")
    print("-" * 60)

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "FIN":
            break
        lines.append(line)

    course_text = "\n".join(lines).strip()
    return topic, course_text


def get_num_questions() -> int:
    """Demande le nombre de questions souhaité."""
    print()
    while True:
        try:
            num = input("❓ Combien de questions ? (3 à 10, défaut: 5) : ").strip()
            if num == "":
                return 5
            num = int(num)
            if 3 <= num <= 10:
                return num
            print("⚠️  Entre un nombre entre 3 et 10.")
        except ValueError:
            print("⚠️  Saisis un nombre valide.")


def main():
    """Point d'entrée principal de l'application."""
    while True:
        display_menu()

        choice = input("  Ton choix (1/2/3) : ").strip()

        if choice == "1":
            topic, course_text = get_course_input()

            if not course_text:
                print("\n⚠️  Aucun texte saisi. Retour au menu.")
                input("Appuie sur Entrée...")
                continue

            num_questions = get_num_questions()

            print()
            print("⏳ Génération du quiz en cours avec l'IA...")
            print("   (Cela peut prendre quelques secondes...)")

            try:
                questions = generate_quiz(course_text, num_questions)
            except Exception as e:
                print(f"\n❌ Erreur lors de la génération : {e}")
                print("   Vérifie ta clé API et ta connexion internet.")
                input("\nAppuie sur Entrée pour revenir au menu...")
                continue

            print(f"✅ {len(questions)} questions générées !")
            input("Appuie sur Entrée pour commencer le quiz...")

            result = run_quiz(questions)
            display_score(result, topic)

            save_score(topic, result["score"], result["total"])
            print("  💾 Score sauvegardé dans l'historique.")
            input("\nAppuie sur Entrée pour revenir au menu...")

        elif choice == "2":
            clear_screen()
            display_history()
            input("Appuie sur Entrée pour revenir au menu...")

        elif choice == "3":
            clear_screen()
            print("\n  👋 À bientôt et bonne révision !\n")
            sys.exit(0)

        else:
            print("⚠️  Choix invalide. Saisis 1, 2 ou 3.")
            input("Appuie sur Entrée...")


if __name__ == "__main__":
    main()
