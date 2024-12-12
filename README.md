# Script_perso

**Script_Perso** est une application interactive en ligne de commande basée sur Python pour gérer, afficher, trier et fusionner des jeux de données CSV. L'outil est conçu pour simplifier le travail avec des fichiers de données tabulaires.

## Fonctionnalités

- **Fusionner des fichiers CSV** : Combine plusieurs fichiers CSV en un seul jeu de données, à condition que les en-têtes correspondent.
- **Afficher les données** : Affiche le jeu de données actuel dans un format tabulaire lisible et bien aligné.
- **Trier les données** : Trie les données par une colonne spécifiée, avec un tri inverse optionnel.
- **Exporter les données** : Sauvegarde le jeu de données actuel dans un nouveau fichier CSV.

## Instructions d'installation

### 1. Prérequis

- Installez Python (version 3.6 ou supérieure) sur votre machine.
- Assurez-vous que les bibliothèques nécessaires sont installées, si nécessaire, vous pouvez installer les dépendances avec la commande suivante :
  
  ```bash
  pip install -r requirements.txt
  
2. Préparation de l'environnement
Placez le fichier main.py et lib.py ainsi que tous les fichiers CSV avec lesquels vous souhaitez travailler dans le même répertoire.
3. Lancer le script
Exécutez le script via un terminal ou une invite de commande :

bash
Copier le code
python main.py
Guide d'utilisation
Une fois le script lancé, vous verrez l'invite suivante : Script_Perso:. À partir de là, vous pouvez utiliser les commandes suivantes :

1. Quitter le Shell
Commande : exit

Description : Quitte le shell Script_Perso.

Exemple :

bash
Copier le code
Script_Perso: exit
2. Ajouter un fichier CSV
Commande : add

Description : Liste les fichiers CSV disponibles dans le répertoire courant et fusionne le fichier sélectionné avec le jeu de données actuel. Les en-têtes du nouveau fichier doivent correspondre à ceux du fichier existant.

Exemple :

bash
Copier le code
Script_Perso: add
Sélectionnez un fichier en entrant son numéro dans la liste affichée.

3. Afficher les données actuelles
Commande : view

Description : Affiche les données actuelles dans un format tabulaire bien aligné pour une lecture facile.

Exemple :

bash
Copier le code
Script_Perso: view

4. Trier les données
Commande : sort
Description : Trie les données par une colonne spécifiée. Vous serez invité à :
Choisir un numéro de colonne.
Décider si le tri doit être effectué dans l'ordre inverse.
Exemple :
bash
Copier le code
Script_Perso: sort

5. Exporter les données
Commande : exporter

Description : Exporte les données actuelles dans un nouveau fichier CSV. Vous serez invité à fournir un nom de fichier.

Exemple :

bash
Copier le code
Script_Perso: unload
Nom du fichier à exporter : données_triées.csv
Structure des fichiers
L'application repose sur une bibliothèque de soutien lib.py pour gérer les opérations CSV. Ce fichier doit inclure les fonctions suivantes :

charger_csv(fichier) : Fonction pour lire un fichier CSV et renvoyer son en-tête et ses données.
verifier_egalite(en_tete1, en_tete2) : Fonction pour vérifier si deux en-têtes de fichiers CSV correspondent.
trier_donnees(donnees, en_tete, colonne, inverse) : Fonction pour trier les données par une colonne spécifiée.
ecrire_csv(nom_fichier, donnees, en_tete) : Fonction pour écrire le jeu de données dans un fichier CSV.
Assurez-vous que lib.py est dans le même répertoire que script_perso_shell.py.

Gestion des erreurs
Incompatibilité des en-têtes : Si les en-têtes d'un fichier CSV à ajouter ne correspondent pas à ceux du jeu de données actuel, une erreur sera levée.
Entrée invalide : Le shell valide les entrées numériques lorsque cela est nécessaire.
Exemples
Exemple : Ajouter et afficher un fichier CSV
bash
Copier le code
Script_Perso: ajouter
1. fichier1.csv
2. fichier2.csv
Numéro du fichier à ajouter : 1
Puis, affichez les données :

bash
Copier le code
Script_Perso: afficher
Nom                 | Valeur1     | Valeur2     | Catégorie      | Tag       
---------------------------------------------------------------------------  
Pommes               | 50.0       | 0.5         | Fruits         | sante     
Oranges              | 85.0       | 0.58        | Fruits         | sante     
Exemple : Trier les données
Trier par une colonne (par exemple, Valeur1) :

bash
Copier le code
Script_Perso: trier
1. Nom
2. Valeur1
3. Valeur2
4. Catégorie
5. Tag
Numéro de la colonne à trier : 2
Le tri doit-il être inversé ?(o/n) : n
Puis, affichez les données triées :
