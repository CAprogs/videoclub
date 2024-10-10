# Contexte du Projet : Vidéo Club de Bob

Bob est un passionné de films classiques et a récemment ouvert son propre vidéoclub qu’il a nommé **"Retro Video Club"**. Ayant une connaissance douteuse de la programmation, il a tenté de créer un programme en Python qui simule les emprunts et les retours de films, ainsi que pour suivre le statut d’ouverture de son vidéoclub.

Cependant, Bob n’est pas très expérimenté en Python, et bien que son programme fonctionne, il n’a pas respecté toutes les bonnes pratiques de développement. Il y a donc de nombreuses améliorations possibles. Ton objectif est d'aider Bob à trouver des axes d'amélioration pour rendre son code plus lisible, plus efficace, et plus robuste.

## Description du projet

Le projet se compose de trois scripts principaux :

1. **`videoclub.py`** : Ce fichier contient la classe principale `VideoClub` qui gère l’état du vidéoclub (ouvert ou fermé), le stock de films, et les informations de base (nom, nombre de jours d’ouverture). Bob a également ajouté un décorateur pour mettre à jour l'état des films.

2. **`user.py`** : Ce fichier contient la classe `User`, qui représente un client du vidéoclub. Chaque utilisateur peut emprunter et rendre des films.

3. **`main.py`** : Le script principal qui simule le fonctionnement quotidien du vidéoclub sur plusieurs jours, en testant les emprunts et retours de films par un utilisateur.

Le stock de films est initialisé à partir d'un fichier `movies.json` contenant des informations de base (titre, auteur, réalisateur, année de parution et note IMDB).

## Ton travail

En tant que développeur expérimenté, ton rôle sera de revoir le code de Bob et d'y suggérer quelques améliorations.


⚠️ **Attention** :
Bob ne voudrait pas que des modifications soient apportées dans sa branche principale, il veut donc que tu crées une branche `dev` pour y apporter tes modifications, que tu pourras ensuite lui soumettre sous forme de pull request.

### Étapes à suivre :

1. Clone le dépôt sur ta machine locale.
2. Crée une nouvelle branche `dev` pour y apporter tes modifications.
3. Exécute le script `main.py` pour vérifier le fonctionnement actuel du programme.
4. Analyse le code de Bob et identifie les axes d'amélioration possibles.

PS : Bob n'a pas rééllement donné de consignes précises pour gérer les dépendances, mais tu peux utiliser un environnement virtuel pour installer les dépendances nécessaires.

## En résumé
Bob a besoin de ton aide pour rendre son programme plus lisible, maintenable, et pour respecter les standards de développement Python. À toi de jouer pour faire en sorte que le **Retro Video Club** devienne le meilleur vidéoclub numérique géré par un code propre et bien structuré !
