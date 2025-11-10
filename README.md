# OpenMoE Visualization & MLOps Integration

##  Contexte du projet
Ce projet a été réalisé dans le cadre d’un stage au sein de l’entreprise, avec pour objectif principal de **visualiser et analyser le fonctionnement interne d’un modèle Mixture of Experts (MoE)**, tout en intégrant un pipeline MLOps complet.

Le projet s’appuie sur le modèle **Switch Transformer (google/switch-base-8)**, développé par Google Research, et met en œuvre des outils modernes pour la traçabilité et la reproductibilité des expériences.

---

##  Objectifs du projet

### 1. Visualiser le fonctionnement interne du modèle OpenMoE
- Suivre le **routage des tokens** dans chaque couche du modèle.
- Identifier **les experts activés** pour chaque token.
- Analyser la **répartition des activations** à travers les couches.

### 2. Analyser la spécialisation des experts
- Identifier les **experts dominants** et les plus fréquemment activés.
- Comparer les activations entre couches pour observer la spécialisation progressive.

### 3. Intégrer un pipeline MLOps complet
- **MLflow** : suivi des expériences, des métriques et des artefacts.
- **MinIO** : stockage des fichiers (artefacts, métriques, CSV).
- **Frontend React** : visualisation interactive des résultats.

---

##  Architecture du projet

OpenMoeProject/
│
├── backend/
│ ├── app.py # API Flask pour le frontend
│ ├── analyseRouter.py # Extraction et génération du CSV des routages
│ ├── log_router_data.py # Suivi MLflow + enregistrement dans MinIO
│ ├── data/router_analysis.csv # Données exportées depuis le modèle
| |── bucketremove.py #ce fichier permet de supprimer un bucket dans MinIO
  |── requirements.txt #pour l'installation des librairies 
│
├── frontend/
│ ├── src/
│ │ ├── App.js # Interface React principale
│ │ ├── components/ # (optionnel) Graphiques & Tableaux
│ ├── package.json
│
├── .env # Configuration des accès MLflow & MinIO
└── README.md # Documentation du projet

##  Technologies utilisées

| Domaine | Outils / Frameworks |
|----------|--------------------|
| **Modèle IA** | PyTorch, Transformers (Hugging Face) |
| **MLOps** | MLflow, MinIO |
| **Backend** | Flask |
| **Frontend** | React.js, Axios, Recharts |
| **Data** | Pandas, CSV |
| **Langages** | Python, JavaScript |

###  1. Lancer le backend (Flask)
Depuis le dossier `backend/` :
```bash
python app.py
