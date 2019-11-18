# Initialisation du projet

## Initialisation de l'environnement
Création de votre environnement virtuel : `virtualenv env_name -p python3`

Activation de votre environnement virtuel : `source env_name/bin/activate`

Toutes les commandes utiles devront maintenant être exécutées avec l'environment virtuel actif.

Pour sortir de l'environnement virtuel `deactivate`

Installation de Django dans l'environnement virtuel : `pip install django`

## Création du projet
Création du projet : `django-admin startproject project_name`

Entrer dans le projet : `cd project_name`

Lancer votre projet : `./manage.py runserver`

Vous venez de lancer votre projet !

Votre terminal vous informe que vous avez des erreurs de migration !

La commande `./manage.py migrate` va mettre  à jour votre base de données et résoudra ce problème.


# Premiers pas
## Création de l'application

Nous allons commencer par créer un application `accueil` pour nous familiariser avec le Framework.
Création d'une application : `./manage.py startapp app_name`

Vous pouvez désormais ouvrir votre projet dans votre éditeur favori !

Renseignez votre application dans le fichier settings.py du projet
Ajoutez les routes vers votre application dans myApp/urls.py

## Premère page
Nous allons maintenant créer notre première page !

Allez dans le fichier myApp/accueil/views.py et ajoutez la fonction "helloWorld" qui renverra une simple HttpResponse avec un titre Hello World !

Créez un fichier urls.py dans votre application "accueil"
Definissez votre route dans myApp/accueil/urls.py, la page dot être disponible à l'adresse http://localhost:3000

Vous venez de réussir à créer votre première page !

## Introduction aux templates

Créez un dossier templates dans votre application.
Django recommande de créer un dossier du nom de votre application dans ce dossier. (Vous devriez avoir un chemin du type (accueil/templates/accueil).

Créez un template helloWorld.html dans ce dossier.

Maintenant adaptez votre view pour utiliser ce template.

## Introduction aux filtres

Maintenant que vous avez un helloWorld dans un fichier html essayons de jouer avec les filtres.

Essayez de modifier la view et le fichier html précédemment créé pour que votre page helloWorld affiche la date actuelle.

## Aller plus loin avec les urls et les filtres

Maintenant que vous avez compris comment bien structurer les pages html d'un projet  Django, voyons comment rendre ces pages dynamiques et les urls un peu plus polyvalentes.

D'abord créez un nouveau template sum.html qui aura pour objectif d'additionner deux nombres passés dans l'url.

Créez ensuite la view correspondante.

Jouons un peu avec le routage, d'abord créez une route classique qui prend en compte le typage de votre url.

Et maintenant créez une route utilisant les regex ! (vous pouvez commenter l'une ou l'autre pour utiliser celle que vous préférez)

Maintenant que votre page est accessible essayez d'afficher la somme de deux façons différentes:
- en calculant à l'intérieur du fichier view.py
- en calculant directement dans le template

Félicitations vous êtes prêt à passer aux choses sérieuses !

# Annuaire

## Afficher des résultats

Nous allons maintenant essayer de créer un petit annuaire.

Créez vous une seconde application "annuaire".

Voici une constante que vous pouvez définir dans votre fichier myApp/annuaire/views.py

```json
    contacts = [
       {
          "nom": "Cassidy",
          "prenom": "Hammond",
          "telephone": "03 94 96 50 97"
        },
        {
          "nom": "Charde",
          "prenom": "Hyde",
          "telephone": "03 44 84 02 60"
        },
        {
          "nom": "Dorian",
          "prenom": "Bailey",
          "telephone": "03 78 24 49 97"
        },
        {
          "nom": "Vivien",
          "prenom": "Duffy",
          "telephone": "03 26 81 80 44"
        },
        {
          "nom": "Ivory",
          "prenom": "Colon",
          "telephone": "03 85 87 65 55"
        }
    ]
```

Nous voulons lister les différents contacts sur une page.

Vous pouvez reprendre la page list.html fournie dans notre archive et la compléter pour afficher la liste des contacts.

Vous pouvez également ajouter un lien de notre page accueil vers notre annuaire afin de faciliter la navigation.

Une fois la liste des contacts terminée nous voulons pouvoir cliquer sur le nom d'un contact pour afficher sa fiche. (Nom, prénom et numéro de téléphone)
Pour cela vous pouvez compléter le fichier contact.html fourni dans l'archive.

## Ajoutons un header

Pour compléter notre application, nous voulons ajouter un header/menu sur toutes les pages de notre application.
Pour cela, vous pouvez ajouter le fichier base.html dans le dossier myApp/templates/layouts.

Ajouter également `os.path.join(BASE_DIR, 'templates'),` dans le fichier myApp/settings dans TEMPLATES.DIRS.
Cela permet de spécifier à Django que les templates globaux de l'application se trouvent dans le dossier myApp/templates

## Customisons un peu

Modifiez le fichier settings.py pour prendre en compte les fichier statics
Vous pouvez prendre le fichier css fournis pour l'intégrer directement a votre projet.

## Base de données

Pour l'instant notre application se base sur des données figées, nous voulons pouvoir moduler ces données.

Ajoutons maintenant une base de données !

Ajoutez une classe Contact dans le fichier myApp/annuaire/models. Cette classe doit contenir les attributs nom, prénom et téléphone. Pas besoin d'ajouter d'ID unique, Django s'en charge pour vous!

Cette page pourra vous être utile pour définir vos différents types de champs.
https://docs.djangoproject.com/fr/2.2/ref/models/fields/

Une fois votre modèle créé, vous pouvez générer la migration et l'appliquer!

Vous pouvez vérifier que la migration a bien été prise en compte en lancant le shell Django `./manage.py shell` et en important votre classe Contact `from annuaire.models import Contact`

Vous pouver utiliser la commande `quit()` pour sortir du shell Django.

Maintenant insérons des données dans votre table contact. Voici quelques données si vous êtes peu inspiré:

```json
    {
		"nom": "Cassidy",
		"prenom": "Hammond",
		"telephone": "03 94 96 50 97"
	},
	{
		"nom": "Charde",
		"prenom": "Hyde",
		"telephone": "03 44 84 02 60"
	},
	{
		"nom": "Dorian",
		"prenom": "Bailey",
		"telephone": "03 78 24 49 97"
	},
	{
		"nom": "Vivien",
		"prenom": "Duffy",
		"telephone": "03 26 81 80 44"
	},
	{
		"nom": "Ivory",
		"prenom": "Colon",
		"telephone": "03 85 87 65 55"
	}
```

Vous pouvez maintenant adapter vos fonctions dans myApp/annuaire/views.py afin d'appeler la base de données.

# Pour aller plus loin

## Evolution du modèle

Nous voulons maintenant prendre en compte les entreprises.
Nous voulons garder une seule entité "contact" pour l'application. On considérera que le nom de l'entreprise est renseigné dans le champ "nom" et que "prenom" sera vide.
Ajoutez également un booléen "entreprise" pour savoir s'il s'agit d'un particulier ou d'une entreprise.

Attention aux données déjà existantes dans votre base, elles doivent rester accessibles après l'upgrade de votre base! (le champ entreprise ne peut pas être null)

Une fois la base mise à jour vous pouvez y insérer quelques données.
Voici quelques entreprises :
```json
    {
		"nom": "Mollis Lectus Pede Foundation",
		"prénom": "",
		"telephone": "07 78 07 96 07",
		"entreprise": "1"
	},
	{
		"nom": "Orci LLC",
		"prénom": "",
		"telephone": "03 47 72 76 30",
		"entreprise": "1"
	},
	{
		"nom": "Montes Nascetur Ridiculus Ltd",
		"prénom": "",
		"telephone": "05 75 63 52 48",
		"entreprise": "1"
	},
	{
		"nom": "Volutpat Nulla Consulting",
		"prénom": "",
		"telephone": "09 18 47 42 35",
		"entreprise": "1"
	},
	{
		"nom": "Vitae Company",
		"prénom": "",
		"telephone": "04 28 63 52 29",
		"entreprise": "1"
	}
```

## Pages jaunes - Pages blanches

Notre modèle ayant évolué, nous voulons maintenant avoir deux listes différentes pour les particuliers et les entreprises.
Affichez les différentes listes sur les urls 'annuaire/particuliers' et 'annuaire/entreprises'.

Ajoutez des liens Pages Jaunes, Pages Blanches dans le menu afin de faciliter la navigation.
