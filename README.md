# P5_OpenFoodFacts
Utilisez les données publiques de l'OpenFoodFacts  
[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeH7711sJeOaZ_HOpwi3M7MjPOQeOPE2TyMxn-_NyxyHu_O2tm&s)](https://openclassrooms.com/fr)
[![](https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-fr-178x150.png)](https://fr.openfoodfacts.org/)  
## Contexte
La startup Pur Beurre connait bien les habitudes alimentaires françaises.  
Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs,  
sur la butte de Montmartre.  
L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation,  
mais ne savaient pas bien par quoi commencer.  
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ?  
## But du projet
Créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments,  
les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.  
Le programme doit pouvoir interroger la base de données d'OpenFoodFacts à travers son API.  
Cela lui permettra de lire et stocker, dans sa propre base de données, les informations utiles.  
Le programme devra ainsi, proposer des produits alternatifs, disponible depuis sa propre base.  
Chaque produit pourra être sauvegardé dans la base de donnée de l'application.  
Le projet hébergé sur GitHub est disponible [ici](https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git).  
## Découpage du projet
Le projet a été découpé en plusieurs étapes de réalisation.  
Chaque étape du projet est une 'user-story'  
qui représente une fonction principale, secondaire ou tertiaire de l'application.  
La réalisation du projet suit ces étapes fonctionnelles dans les sections :   
**Les User-Stories** et **Les Developer-stories**.  
Vous pouvez retrouver l'ensenmble de ces étapes fonctionnelles,  
ainsi que leur statut d'avancement sur l'outil en ligne [TRELLO](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts) 
### Les User-Stories
* __***US10***__  *Fonction console*

        En tant que personne lambda, je peux lancer l'IHM,
        afin de pouvoir interagir avec les différents menu du programme.

* __***US20***__ *Fonction menu principal*

        En tant qu’utilisateur enregistré,
        je peux faire un choix entre : 
            -"Quel aliment souhaitez-vous remplacez?"
            -"Retrouvez mes aliments substitués."
            -"Quitter le programme."
        afin de répondre à mon besoin actuel. 
* __***US30***__ *Fonction aliment à remplacer*

        En tant qu’utilisateur enregistré,
        je peux sélectionner la proposition 1,
        afin de choisir l’aliment à remplacer.

* __***US31***__ *Fonction catégorie alimentaire*

        En tant qu’utilisateur enregistré,
        je peux sélectionner la catégorie,
        afin de retrouver l’aliment que je désire remplacer.

* __***US32***__ *Fonction sélection aliment à remplacer*

        En tant qu’utilisateur enregistré,
        je peux sélectionner l’aliment à remplacer,
        afin de préparer l’étape de substitution.
    
* __***US33***__ *Fonction sélection aliment à substituer*

        En tant qu’utilisateur enregistré,
        je peux choisir un aliment de substitution en fonction de sa description, son point de vente,
        afin de conclure l’étape de substitution.

* __***US34***__ *Fonction sauvegarde aliment à substituer*

        En tant qu’utilisateur enregistré,
        je peux sauvegarder l’aliment de substitution dans la base de données,
        afin de pouvoir le retrouver dans son espace dédié.

* __***US40***__ *Fonction mes aliments substitués*

        En tant qu’utilisateur enregistré,
        je peux sélectionner la proposition 2 du menu principal,
        afin de retrouver mes aliments substitués.

* __***US41***__ *Fonction tableau aliments ajoutés*

        En tant qu’utilisateur enregistré,
        je peux accéder à un tableau d’informations,
        afin de voir les aliments ajoutés.

* __***US42***__ *Fonction tableau aliments soustraits*

        En tant qu’utilisateur enregistré,
        je peux accéder à un tableau d’informations,
        afin de voir les aliments soustraits.

* __***US50***__ *Fonction proposition 3*
    
        En tant qu’utilisateur,
        je peux sélectionner la proposition 3,
        afin de quitter le programme. 
### Les Developer-Stories
* __***DS10***__ *Fonction création base de données*
* __***DS11***__ *Fonction remplissage base de données*
* __***DS12***__ *Fonction modification base de données*
* __***DS20***__ *Fonction récupération des données API*
* __***DS21***__ *Fonction stockage des données API*
* __***DS22***__ *Fonction triage des données API*
* __***DS23***__ *Fonction injection des données API*
* __***DS30***__ *Fonction consultation des données locales*
* __***DS31***__ *Fonction affichage des données locales*
### Le modèle physique de données
Le modèle physique de données est disponible dans le fichier  
*P5_OpenFoodFacts.drawio*.  
pour lire ce fichier veuillez vous rendre sur le site [*DRAW.IO*](https://www.draw.io/).  
- Sélectionnez *"Device"*
- Sélectionnez *"Open Existing Diagram"*
- Sélectionnez le fichier *P5_OpenFoodFacts.drawio* disponible [*ici*](P5_OpenFoodFacts.drawio)
### Le fichier de création de la BDD
Dans ce projet, deux scripts dédiés à la base de données existent.  
- db_purebeurre_*_empty.sql *(Ne contenant aucune données)*  
- db_purebeurre_*_full.sql *(contenant des données)*  
Ces scripts de création de la base de données sont disponible dans le répertoire [*/Packages*](/Packages)
## Documentation - Driven development  
### Comment installer l'application PurBeurre  
#### *ENVIRONNEMENT VIRTUEL*.  
Ouvrir un invité de commandes et rendez-vous à la racine du projet téléchargé, exemple sous windows :   
-       cd D:projet\projet_python\P5_OpenFoodFacts-master
Créez l'environnement virtuel, exemple sous windows :  
-       python -m virtualenv -p python my_env.  
Lancez l'environnement virtuel, exemple sous windows :
-       my_env\Script\activate.  
#### *DEPENDANCES*.  
Pour installer les dépendances du programme, entrez la commande : 
-       pip install -r requirements.txt   
exemple sous windows :
-       my_env\Script\pip install -r Labyrinthe\requirements.txt
#### *DEMARRAGE DU PROGRAMME*.
Rendez-vous dans le répertoire "P5_OpenFoodFacts", exemple sous windows :
 -      cd P5_OpenFoodFacts
Lancer le programme principale "main.py", exemple sous windows :
-       python main.py 
Pour lancer le programme autrement, double-cliquez sur "main.py" oubien ouvrir "main.py" dans un IDE python.
### Comment fonctionne l'application Purbeurre  
        In progress...
### Comment utiliser l'application PurBeurre  
        In progress...
## Outils de développement  
- Pycharm ; version : 2019.3
- Python ; version : 3.7
- Draw.io ; version 12.5.8
- MySQL ; version 8.0 
- Notepad Plus Plus ; version 7.8.1
## AUTEUR  
Stephen A.OGOLO  
---
## Rappel
>[Projet hébergé sous GitHub](https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git)  
>[Projet planifié sous Trello](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts)  