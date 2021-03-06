---
# P5_OpenFoodFacts
Utilisez les données publiques de l'OpenFoodFacts  
[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeH7711sJeOaZ_HOpwi3M7MjPOQeOPE2TyMxn-_NyxyHu_O2tm&s)](https://openclassrooms.com/fr)
[![](https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-fr-178x150.png)](https://fr.openfoodfacts.org/)  

---
## CONTEXTE
La startup Pur Beurre connait bien les habitudes alimentaires françaises.  
Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs,  
sur la butte de Montmartre.  
L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation,  
mais ne savaient pas bien par quoi commencer.  
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ?  

---
## BUT DU PROJET
Créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments,  
les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.  
Le programme doit pouvoir interroger la base de données d'OpenFoodFacts à travers son API.  
Cela lui permettra de lire et stocker, dans sa propre base de données, les informations utiles.  
Le programme devra ainsi, proposer des produits alternatifs, disponible depuis sa propre base.  
Chaque produit pourra être sauvegardé dans la base de donnée de l'application.  
Le projet hébergé sur GitHub est disponible [ici](https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git).  

---
## DECOUPAGE DU PROJET
Le projet a été découpé en plusieurs étapes de réalisation.  
Chaque étape du projet est une 'user-story'  
qui représente une fonction principale, secondaire ou tertiaire de l'application.  
La réalisation du projet suit ces étapes fonctionnelles dans les sections :   
**Les User-Stories** et **Les Developer-stories**.  
Vous pouvez retrouver l'ensenmble de ces étapes fonctionnelles,  
ainsi que leur statut d'avancement sur l'outil en ligne [TRELLO](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts) 

---
### Les User-Stories
Liste des fonctions liées aux opérations IHM :  
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
        je peux sélectionner 'Quel aliment souhaitez-vous remplacer ?',
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
        je peux sélectionner la proposition 'Retrouver mes aliments substitués',
        afin de retrouver mes aliments substitués.

* __***US41***__ *Fonction tableau aliments ajoutés*

        En tant qu’utilisateur enregistré,
        je peux accéder à un tableau d’informations,
        afin de voir les aliments ajoutés.

* __***US42***__ *Fonction tableau aliments soustraits*

        En tant qu’utilisateur enregistré,
        je peux accéder à un tableau d’informations,
        afin de voir les aliments soustraits.

* __***US50***__ *Fonction fermeture du programme*
    
        En tant qu’utilisateur,
        je peux sélectionner 'Quitter',
        afin de quitter le programme. 

---
### Les Developer-Stories
Liste des fonctions liées aux opérations algorithmiques:  
* __***DS10***__ *Fonction création base de données*
* __***DS11***__ *Fonction remplissage base de données*
* __***DS12***__ *Fonction modification base de données*
* __***DS20***__ *Fonction récupération des données API*
* __***DS21***__ *Fonction stockage des données API*
* __***DS22***__ *Fonction triage des données API*
* __***DS23***__ *Fonction injection des données API*
* __***DS30***__ *Fonction consultation des données locales*
* __***DS31***__ *Fonction affichage des données locales*

Vous pouvez retrouver l'ensenmble de ces étapes fonctionnelles,  
ainsi que leur statut d'avancement sur l'outil en ligne [TRELLO](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts) 

---
### Le modèle physique de données
Le modèle physique de données est disponible dans le fichier  
*P5_OpenFoodFacts.drawio*.  
pour lire ce fichier veuillez vous rendre sur le site [*DRAW.IO*](https://www.draw.io/).  
- Sélectionnez *"Device"*
- Sélectionnez *"Open Existing Diagram"*
- Sélectionnez le fichier *P5_OpenFoodFacts.drawio* disponible [*ici*](P5_OpenFoodFacts.drawio)

---
## ENVIRONNEMENT DE DEVELOPPEMENT  

---
### Outils de développemment  
Liste des outils et versions utilisées:
-        Pycharm ; version : 2019.3
-        Python ; version : 3.7.4
-        Draw.io ; version 12.5.8
-        MySQL ; version 8.0 
-        Notepad Plus Plus ; version 7.8.1

---
### Qualité de développement  
Liste des outils, des versions utilisées
et des rapports de qualité:  
-        Pylint ; Version : 2.4.4 ; Note : 10/10
-        Flake8 ; Version : 3.7.9 ; Note : Line too long ~ 90/79

---
## COMMENT INSTALLER L'APPLICATION  

---
### *La pré-installation automatisée*.   
La pré-installation suit les étapes suivante:
-       Création d'un environnement virtuel
-       Activation de l'environnement virtuel
-       Installation des dépendances, modules externes du programme
---
### *La procédure de la pré-installation automatisée*.
-       Téléchargez le projet P5_OpenFoodFacts au format .zip => https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git
-       Décompressez le fichier .zip
-       Ouvrez le dossier extrait
-       Double-cliquez sur le script "pre_installation.bat"
Après avoir lancé la pré-installation, via le script "pre_installation.bat",
un invité de commande s'ouvre et le processus d'installation se déroule.  
En fin d'installation, le message _PREINSTALLATION TERMINE_ s'affiche.

L'invité de commande reste ouverte. Vous pouvez immédiatement démarrer le programme ainsi:

-       main.py

---
### *Pré-installation manuelle*.

---
#### *L'installation manuelle de l'environnement virtuel*.  
Ouvrir un invité de commandes et rendez-vous dans le dossier parent du projet téléchargé.   
Créez l'environnement virtuel, avec le même nom que celui du projet.  
Cette opération permettra de transformer le projet en environnement virtuel.
Exemple sous windows :  

        python -m virtualenv -p python P5_OpenFoodFacts-master.          
Lancez l'environnement virtuel, exemple sous windows :  

        P5_OpenFoodFacts-master\Scripts\activate.  
---
#### *L'installation manuelle des dépendances*.  
Voici la liste des modules externes essentiels au fonctionnement du programme :  
-      configparser==4.0.2 "Ce module permet la gestion du fichier de configuration'settings.ini'".
-       mysql-connector>=2.2.9 "Ce module permet la communication avec le serveur MYSQL.
-       requests>=2.22.0 "Ce module permet la communication protocolaire HTTP vers l'API.
-       getpass4>=0.0.8 "Ce module permet la sasie masquée de mot de passe utilisateur.
Pour installer les dépendances du programme, rendez-vous dans le répertoire _\Scripts_ du projet  
puis entrez la commande :
 
-       pip install -r requirements.txt  

Exemple sous windows :

-       my_env\Scripts\pip install -r P5_OpenFoodFacts-master\requirements.txt

---
## COMMENT FONCTIONNE L'APPLICATION  

---
### *l'Architecture interne*
        -> pre_installation.bat
        -> main.py
        -> Packages -> api_operations.py
                    -> console.py
                    -> loading.py
                    -> mysql_operations.py
                    -> options.py
                    -> db_purebeurre.sql
                    -> settings.ini
                    -> urls.json

---
### *Le processus algorhitmique*
Les blocs ci-dessous décrivent le processus algorhitmique du programme.  
Chaque bloc shématise une opération fonctionnelle,  
qui peut être réalisé par un ou plusieurs modules.  
Les blocs sont numérotés par ordre d'exécution.  

        1. Démarrage du programme
        2. Récupération des paramètres d'initialisation
        3. Récupération des données OpenFoodFacts
        4. Création et remplissage de la base données locale
        5. Exécution de l'interface homme-machine
        6. Extinction du programme

---
### *La base de données*  
Un script est dédié à la base de données.  
-       db_purebeurre.sql     
Ce scripts est disponible dans le répertoire [*/Packages*](/Packages)  

---
### *Les requêtes HTTP*  
Un fichier est dédié à la conservation des requête HTTP.  
-       urls.json     
Ce fichier est disponible dans le répertoire [*/Packages*](/Packages)  

---
### *Le paramétrage*  
__ATTENTION__ :
  
-        LA PRESENCE ET LA VALORISATION DE LA TOTALITE DES PARAMETRES SONT OBLIGATOIRES.
  
Le paramétrage du programme est centralisé dans un fichier de configuration.
-       settings.ini
Il contient les paramètres essentiels au lancement du programme. 
Ce fichier est disponible dans le répertoire [*/Packages*](/Packages)   

---
#### *Paramétrage MYSQL*

---
##### Mise à jour de la base de données :  "check_db_exists"    
-       check_db_exists=0
Au lancement du programme, durant la phase d'initialisation,  
L'activation du paramètre "check_db_exists=1" permet de proposer  
- soit la mise à jour de la base de données, si celle-ci est déjà existante.  
- soit la conservation de la base de données actuelle, si celle-ci est déjà existante.  

Par défaut, ce paramètre est valorisé à "0" afin de ne pas proposer ce choix à l'utilisateur,  
durant le lancement du programme.

---
##### Création de la base de donnée :  "user", "host", "psw", "db_name" et "db_sql_file" 
-        user=stephen
-        host=localhost
-        psw=stephen
-        db_name=db_purebeurre
-        db_sql_file=./Packages/db_purebeurre.sql

Au lancement du programme, durant la phase d'initialisation,  
le processus utilise les valeurs des paramètres "user", "host", "psw" et "db_name"  
pour se connecter à la base de données créée par le programme.  
Elles seront également utilisées pour réaliser toutes les opérations liées à la base de données.  

Concernant le paramètre "db_sql_file", il est valorisé par le chemin,  
relatif ou absolu, du script sql dédié à la conception des tables SQL de la base de données.  

Pour rappel:
- "user" = "nom de l'utilisateur"  
- "host" = "la machine d'hébergement du serveur MYSQL"    
- "psw" = "mot de passe de l'utilisateur"  
- "db_name" = "nom de la base de données"      

---
#### *Paramétrage API*  

---
##### Requêtage URLS :  "urls_json_file" 
      
-       urls_json_file=./Packages/urls.json

le paramètre "urls_json_file" est valorisé par le chemin relatif ou absolu,  
du fichier contenant les requêtes HTTP,  
dédiées aux opérations liées à l'API OpenFoodFacts.  
Le fichier précisé doit obligatoirement être sous format json.

---
#### *Paramétrage ROOT MYSQL*

---
##### Activation du mode root MYSQL :  "root_access" 
-        root_access=0    
 
Au lancement du programme, durant la phase d'initialisation,  
l'activation du paramètre "root_access=1" permet de lancer  
l'autentification administrateur MYSQL. Il est essentiellement utile  
pour créer un utilisateur MYSQL, si celui-ci n'existe pas.  

Par défaut, ce paramètre est valorisé à "0" afin de ne pas proposer l'autentification  
administrateur MYSQL à l'utilisateur, durant le lancement du programme.

---
##### Création d'un utilisateur mysql :  "root_user_db", "root_host_db" et "root_psw_db"    
-        root_user_db=test_user_test_p5
-        root_host_db=localhost
-        root_psw_db=test

Au lancement du programme, durant la phase d'initialisation,  
le processus utilise les valeurs des paramètres "root_user_db", "root_host_db" et "root_psw_db""  
pour créer un utilisateur mysql. Cet utilisateur aura les droits de lecture et d'écriture sur la base de données,  
dont le nom est précisé par le paramètre "db_name".  
Ces paramètres sont uniquement dédiés à la création d'utilisateurs MYSQL.  
Ces paramètres sont pris en compte, uniquement lorsque le mode root est activé (root_access=1).

Pour rappel:
- "root_user_db" = "nom de l'utilisateur"  
- "root_host_db" = "la machine d'hébergement du serveur MYSQL"    
- "root_psw_db" = "mot de passe de l'utilisateur" 

--- 
## COMMENT UTILISER L'APPLICATION  

---
### *Démarrage du programme*.
Rendez-vous dans le répertoire "P5_OpenFoodFacts", exemple sous windows :
 -      cd P5_OpenFoodFacts
Assurez-vous que votre environnement virtuel est correctement installé et activé.
Si ce n'est pas le cas, veuillez suivre les instructions de pré-installation.
Lancer le programme principale "main.py", exemple sous windows :
-       python main.py  
Pour lancer le programme autrement, double-cliquez sur "main.py"  
oubien ouvrir "main.py" dans un IDE python.  

---
### *Prise en main de la console*.  
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :  

        1 - Quel aliment souhaitez-vous remplacer ?
        2 - Retrouver mes aliments substitués.
L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur  
et ce dernier sélectionne les réponses :

        Sélectionnez la catégorie.
Plusieurs propositions sont associées à un chiffre.  
L'utilisateur entre le chiffre correspondant et appuie sur entrée  

        Sélectionnez l'aliment.
Plusieurs propositions sont associées à un chiffre.
L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée

        Le programme propose un substitut, sa description,  
        un magasin ou l'acheter et un lien vers la page d'Open Food Facts concernant cet aliment.

L'utilisateur a alors la possibilité d'enregistrer la substitution.  

Après un retour au menu principale, l'utilisateur peut répéter l'opération,  
consulter l'historique de ces substitutions ou fermer le programme. 


---
## RAPPEL
>[Projet hébergé sous GitHub](https://github.com/StephenAOGOLO/P5_OpenFoodFacts.git)  
>[Projet planifié sous Trello](https://trello.com/invite/b/46lT5ayx/e10292af3dc3d7b88e39166737f37d71/p5openfoodfacts)

---
## AUTEUR  
        Stephen A.OGOLO  

---
## REMERCIEMENTS
        Merci pour cette lecture et pour l'attention portée à ces informations.  
        Bonne utilisation ;)  