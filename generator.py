import os
import json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def generate_quiz(course_text: str, num_questions: int = 5) -> list[dict]:
    """
    Génère un QCM à partir d'un texte de cours via l'API Groq.

    Args:
        course_text: Le texte du cours à transformer en quiz
        num_questions: Nombre de questions à générer (défaut: 5)

    Returns:
        Liste de questions avec choix et réponse correcte
    """
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""Tu es un professeur expert en BTS SIO (Services Informatiques aux Organisations).
À partir du texte de cours suivant, génère exactement {num_questions} questions QCM (Questionnaire à Choix Multiples).

TEXTE DU COURS :
{course_text}

INSTRUCTIONS :
- Génère des questions pertinentes qui testent la compréhension réelle
- Chaque question doit avoir exactement 4 choix (A, B, C, D)
- Une seule réponse correcte par question
- Les questions doivent couvrir différents aspects du cours
- Adapte la difficulté au niveau BTS SIO

Réponds UNIQUEMENT avec un JSON valide, sans texte avant ou après, dans ce format exact :
[
  {{
    "question": "La question ici ?",
    "choices": {{
      "A": "Premier choix",
      "B": "Deuxième choix",
      "C": "Troisième choix",
      "D": "Quatrième choix"
    }},
    "answer": "A",
    "explanation": "Explication courte de la bonne réponse"
  }}
]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = response.choices[0].message.content.strip()

    # Nettoyer les éventuels backticks markdown
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]

    questions = json.loads(response_text.strip())
    return questions
