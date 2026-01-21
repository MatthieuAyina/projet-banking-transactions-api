Cette API, développée avec FastAPI, est une solution complète pour la gestion et l'analyse de transactions bancaires. Elle permet de manipuler des données financières, de générer des statistiques par utilisateur et d'identifier des transactions frauduleuses.

L'architecture suit les standards professionnels pour assurer la modularité et la facilité de test :

src/banking_api/ : Cœur de l'application (Routes FastAPI et modèles Pydantic).

src/banking_api/services/ : Logique métier isolée (calculs statistiques et algorithme de fraude).

tests/ : Suite de tests unitaires garantissant la fiabilité des services.

Dockerfile & pyproject.toml : Configuration pour le déploiement et le packaging.

Cloner le dépôt : git clone https://github.com/MatthieuAyina/projet-banking-transactions-api.git
cd projet-banking-transactions-api

Installer les dépendances : python -m pip install .

Démarrer l'API : python -m uvicorn src.banking_api.main:app --reload

Accès Swagger UI : http://127.0.0.1:8000/docs

Le projet a été développé avec une exigence de qualité stricte :

Conformité PEP8 : Code vérifié avec flake8 pour une lisibilité maximale.

Documentation Numpydoc : Toutes les fonctions sont documentées selon le standard NumPy.

Couverture de tests : 86% de coverage atteint.

Lancer les tests : pytest --cov=src
