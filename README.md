# 🎓 QuizGen SIO — Générateur de Quiz IA pour BTS SIO

> Transforme n'importe quel cours en QCM interactif grâce à l'intelligence artificielle.

---

## 📌 Description

**QuizGen SIO** est une application Python en ligne de commande qui utilise l'API Claude (Anthropic) pour générer automatiquement des QCM à partir de tes cours. Idéal pour réviser le BTS SIO de façon active et efficace.

---

## ✨ Fonctionnalités

- 📝 **Génération automatique** de QCM à partir de n'importe quel texte de cours
- 🤖 **IA intégrée** via l'API Claude d'Anthropic
- ✅ **Feedback instantané** avec explication de chaque réponse
- 📊 **Historique des scores** sauvegardé en JSON
- 🎯 **Résultats détaillés** avec pourcentage et niveau d'appréciation
- 🔢 **Nombre de questions paramétrable** (3 à 10)

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-pseudo/quizgen-sio.git
cd quizgen-sio
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la clé API

Crée un fichier `.env` à la racine du projet :

```
ANTHROPIC_API_KEY=ta_clé_api_ici
```

> 💡 Obtiens ta clé API sur [console.anthropic.com](https://console.anthropic.com)

---

## ▶️ Lancer l'application

```bash
python main.py
```

---

## 📁 Structure du projet

```
quizgen-sio/
├── main.py           # Menu principal et navigation
├── generator.py      # Génération du quiz via l'API Claude
├── quiz.py           # Logique du quiz et affichage
├── history.py        # Sauvegarde et affichage de l'historique
├── requirements.txt  # Dépendances Python
├── .gitignore        # Fichiers ignorés par Git
├── data/
│   └── scores.json   # Historique des scores (généré automatiquement)
└── README.md
```

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| Python 3.10+ | Langage principal |
| Anthropic SDK | Génération IA des questions |
| JSON | Persistance des scores |
| Git / GitHub | Versioning et déploiement |

---

## 📚 Compétences BTS SIO couvertes

| Code | Compétence |
|------|-----------|
| B1.3 | Développement d'une solution applicative |
| B1.4 | Travail en mode projet avec Git |
| B2.1 | Utilisation d'une API externe |
| B3.1 | Gestion et persistance des données |

---

## 🗺️ Améliorations futures

- [ ] Interface graphique avec Tkinter ou PyQt
- [ ] Export des résultats en PDF
- [ ] Mode révision ciblée sur les questions ratées
- [ ] Support de fichiers PDF en entrée

---

## 👤 Auteur

**Ton Nom** — BTS SIO SLAM  
[GitHub](https://github.com/ton-pseudo) · [Portfolio](https://ton-portfolio.fr)

---

## 📄 Licence

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus de détails.
