## Initialisation de l'environnement
Creation de l'environnement virtuel
`virtualenv env_name -p python3`
Activation de votre environnement virtuel
`source env_name/bin/activate`
Installation de Django dans l'environnement virtuel
`pip install django`
Création du projet
`django-admin startproject project_name`
Entrer dans le projet
`cd project_name`
Lancer votre projet
`./manage.py runserver`

Bravo vous avez réussi a lancer votre application
Vous avez des erreurs de migration, `./manage.py migrate` les resoudra.


## Notre première application
### Démarrage de l'application
Création de votre première application
`./manage.py startapp app_name`

Vous pouvez désormais ouvrir votre projet dans votre éditeur favori

Renseignez votre application dans le fichier settings.py
Ajoutez les routes vers votre application dans myApp/urls.py

Nous allons maintenant créer notre première page!!

Allez dans le fichier myApp/accueil/views.py et ajouter la fonction "helloWorld" qui renverra une simple HttpResponse avec un titre Hello World!

Créez un fichier urls.py dans votre application accueil
Definissez votre route dans myApp/accueil/urls.py

Ca marche!!

### Introduction de la notion de template 

Créez un dossier templates dans votre application, puis un dossier du nom de votre application dans ce dossier.

Puis créez une page helloWorld.html dans ce dossier

Modifiez votre fonction helloWorld dans le fichier myApp/accueil/views pour renvoyer la page que vous venez de créer.

Vérifiez vous obtenez le même résultat!

### Utilisons les différents types de route


## Annuaire

### Afficher des résultats

Nous allons maintenant essayer de créer un petit annuaire.

Créez vous une seconde application annuaire

Voici une constante que vous pouvez définir dans votre fichier myApp/annuaire/views.py

    ```json
    contacts = [
        {'id': 0, 'nom': 'Nom', 'prenom': 'Prénom', 'telephone':'03 12 34 66 55'},
        {'id': 1, 'nom': 'Tata', 'prenom': 'Toto', 'telephone':'03 99 99 99 99'},
        {'id': 2, 'nom': 'Lechien', 'prenom': 'Bobby', 'telephone':'03 01 01 01 01'},
    ]
    ```

Nous voulons lister les différents contacts sur une page.

Vous pouvez reprendre la page list.html fournit dans notre archive et la compléter.

Une fois la liste des contacts terminées nous voulons pourvoir cliquer sur le nom d'un contact pour afficher sa fiche.
Pour cela vous pouvez compléter le fichier contact.html fournit dans l'archive.

### Ajoutons un header

Vous pouvez ajouter le fichier base.html dans le dossier myApp/templates/layouts
Ajouter dans le fichier myApp/settings `os.path.join(BASE_DIR, 'templates'),` dans TEMPLATES.DIRS
Cela permet de spécifier à Django que les template global de l'application se trouvent dans myApp/templates

## Base de données

Ajoutons maintenant une base de données 

Ajouter une classe contact dans le fichier myApp/annuaire/models
Cette classe doit contenir les attributs nom/prénom/telephone.
Pas besoin d'ajouter d'ID unique, Django s'en charge pour vous!


Une fois votre model créé, vous pouvez générer la migration et l'appliquer!

Vous pouvez vérifier que la migration a bie été prise en compte en lancant le shell Django `./manage.py shell` et en important votre classe Contact `from annuaire.models import Contact`

Vous pouver utiliser la commande `quit()` pour sortir du shell Django.

Vous pouvez maintenant insérer des données dans votre table contact:

Vois quelques données si vous êtes peu inspiré:

**Mettre quelques données du format suivant**
```json
{nom='BAZIR', prenom='Allyson',telephone='06 13 13 13 13'}
```

Vous pouvez maintenant adapter vos fonctions dans myApp/annuaire/views.py afin d'appeler la base de données.

## Pour aller un peu plus loin

### Evolution du modèle

Nous voulons maintenant prendre en compte les entreprises.
Nous voulons garder une seule entité contact pour l'application, on considéra que le nom de l'entreprise sera renseigné dans le champ "nom" de contact et que prenom sera vide.
Ajoutez également un booleen "entreprise" pour savoir s'il s'agit d'un particulier ou d'une entreprise.

Attention aux données déjà existantes dans votre base, elles doivent rester accessibles après l'upgrade de votre base! (le champ entreprise ne peut pas être null)

### Page jaune - Page blanche

Notre modèle ayant évoluer, nous voulons maintenant avoir deux listes différentes pour les particuliers et les entreprises.
Afficher les différentes listes sur les urls 'annuaire/particuliers' et 'annuaire/entreprises'


Ajoutez des liens Pages Jaune, Page Blanche dans le menu afin de faciliter la navigation. 
























