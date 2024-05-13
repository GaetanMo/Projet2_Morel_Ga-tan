# Système de surveillance des prix

Cet outil permet de scraper des informations sur les livres du site web https://books.toscrape.com/index.html dans des fichiers pour chaque catégorie au format csv. De plus, il télécharge localement l'image de couverture de tous les livres dans un dossier images.

## Installation et utilisation

1. Assurez-vous d'avoir Python installé sur votre système

2. Installez les bibliothèques python requises en exécutant la commande suivante :

pip intall -r requirements.txt

3. Exécutez le script en utilisant la commande suivante : python main.py

## Fonctionnalités

Le script récupère automatiquement les informations sur les livres. Il créé ensuite un premier dossier "categories" contenant tous les fichiers .csv de chaque catégorie. Il créé également un dossier images avec des sous-dossiers pour chaque catégorie regroupant toutes les pages de couvertures des livres.

## Exemples d'utilisation

Voici comment exécuter le script pour récupérer les données :

1. Ouvrez un terminal.
2. Accédez au répertoire où se trouve le script Python.
3. Exécutez la commande `python main.py`.
4. Attendez que le script se termine. Les fichiers CSV et les images seront générés dans les dossiers correspondants.
