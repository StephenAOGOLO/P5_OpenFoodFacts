# P5_OpenFoodFacts
Utilisez les données publiques de l'OpenFoodFacts

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
La réalisation du projet suit ces étapes fonctionnelles dans la section **Les User-Stories**.  
Vous pouvez retrouver l'ensenmble de ces étapes fonctionnelles,  
ainsi que leur statut d'avancement sur l'outil en ligne [TRELLO](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts) 

## Les User-Stories
* __***US10***__  *Fonction compte utilisateur*

        En tant que personne lambda,
        je peux créer un compte utilisateur,
        afin de m’enregistrer à la base de données du programme.

* __***US20***__ *Fonction menu principal*

        En tant qu’utilisateur enregistré,
        je peux faire un choix entre : 
            -"Quel aliment souhaitez-vous remplacez?"
            -"Retrouvez mes aliments substitués."
            -"Quitter le programme."
        afin de répondre à mon besoin actuel. 
* __***US30***__ *Fonction proposition 1*

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

* __***US40***__ *Fonction proposition 2*

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

## Documentation - Driven development  
- _***Comment fonctionne l'application Purbeurre***_  

        In progress...
- _***Comment installer l'application PurBeurre***_  

        In progress...
- _***Comment utiliser l'application PurBeurre***_  

        In progress...

## Outils de développement  
- Pycharm ; version : 2019.3
- Python ; version : 3.7
- Draw.io ; version 12.5.8
- MySQL ; version 8.0 
- Notepad Plus Plus ; version 7.8.1
---
## Rappel
>[Projet hébergé sous GitHub](https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git)  
>[Projet planifié sous Trello](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts)  