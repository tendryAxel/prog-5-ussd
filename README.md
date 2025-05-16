# Projet UV – [Nom du projet]

## 🧾 Description

Ce projet a été réalisé dans le cadre d'un project universitaire.  
Il a pour objectif de creer un terminal interactif pour repondre a des choix multiples.

## ⚙️ Installation

Voici les étapes à suivre pour lancer le projet dans le cadre d’UV :

### 1. Installation de `uv`

Assurez-vous que `uv` est installé :

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
````
or 
```bash
pip install uv
````

Ou suivez les instructions officielles : [https://docs.uv.dev/](https://docs.uv.dev/)

### 2. Création d’un environnement virtuel avec `uv`

Dans le répertoire racine du projet :

```bash
uv venv
source .venv/bin/activate  # ou `.venv/Scripts/activate` sous Windows
```

### 3. Installation des dépendances

```bash
bash install.sh
```

---

## 🚀 Lancer le projet

Une fois l’environnement prêt, exécutez le script principal :

```bash
uv run main.py
```

---

## 🧹 Qualité du code

### Linter

Pour vérifier la qualité du code :

```bash
bash lint.sh
```

### Formatage automatique

Pour formater le code :

```bash
bash format.sh
```

---

## 🧪 Tests (si applicables)

```bash
pytest tests/
```

---

## 👤 Auteurs

* **tendryAxel** —

---

## 📄 Licence

Projet académique – utilisation non commerciale uniquement.
