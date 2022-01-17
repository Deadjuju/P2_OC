# Projet 2 - OpenClassrooms: Utilisez les bases de Python pour l'analyse de marché
![Logo](https://user.oc-static.com/upload/2020/09/22/1600779540759_Online%20bookstore-01.png "logo du projet")  


## Ce script python permet de récupérer les informations de la librairie en ligne
## [Books to Scrape](https://books.toscrape.com "Link to books to scrape")
***

### Données à extraire
Les données extraites pour chaque ouvrage sont les suivantes: 
    
    {  
        "product_page_url": L’Url de la page,
        "universal_ product_code (upc)": Le code UPC du livre,
        "title": Titre du livre,
        "price_including_tax": Prix TTC,
        "price_excluding_tax": Prix HT,
        "number_available": nombre d’exemplaire disponible,
        "product_description": résumé de l’ouvrage,
        "category": catégorie du livre,
        "review_rating": note du livre,
        "image_url": url de sa couverture
    }
Elles seront stockées dans un dossier, créé automatiquement à la racine du projet, nommé **extracts**.
***  
  
## I. Installation du projet

### Langage utilisé **Python**
Ce script fonctionne au **minimum** sur la version **Python 3.4**.   

### Environnement virtuel
Ouvrir un terminal à la racine du dossier.    
     
  1. Taper la commande suivante pour générer l'environnement virtuel:  

    python -m venv env  


> *env* est le nom par défaut de l'environnement virtuel mais peut être nommer différemment.  
  
  2. Activer ensuite l'environnement virtuel:
    
    > Sur Windows  
    - terminal de type bash: source env/Scripts/activate
    - terminal de type shell: env\Scripts\activate
      
    > Sur Mac ou Linux
    - source env/bin/activate

### Installer les paquets
  3. Pour installer les librairies supplémentaires exécuter la commande suivante:

    pip install -r requirements.txt

## II. Exécution du programme

Pour exécuter le programme rentrer la commande suivante dans le terminal:

         py run.py

## III. Choisir l'option à exécuter
Ce script donne la possibilité à l'utilisateur de choisir s'il veut extraire les données précédemment citées pour:
- 1 livre en particulier;
- 1 catégorie de livre;
- tous les livres du site.
>*What do you want to do?*
> - *To extract data from a single book, type '1'.*
> - *To extract data from a chosen category, type '2'.*
> - *To extract data from the entire site, type '3'.*
>
>*Your choice: || -->* **VOTRE RÉPONSE: 1, 2 ou 3**
  
    
### 1. Extraction des données pour un ouvrage
Pour extraire les données d'un livre en particulier il faut renseigner une **URL** valide provenant du site [Books to Scrape](https://books.toscrape.com "Site de Books to Scrape").
Il est également possible de demander au script de télécharger l'image de couverture du livre.  
Les données sont stockées dans un dossier nommé **extract_one_book** et créé automatiquement à l'intérieur du dossier **extracts**:
+ un fichier csv - "nom_du_livre.csv"
+ un fichier jpg - "nom_du_livre.jpg" (si le téléchargement des images a été précisé)
  
### 2. Extraction des données d'une catégorie
Pour extraire les donner des livres d'une catégorie choisie il faut renseigner le nom de la catégorie.  
Taper *"list"* pour afficher la liste des noms de toutes les catégories du site si besoin avant de renseigner le nom de la catégorie désirée.  
Les données sont stockées dans un dossier nommé **extract_one_category** et créé automatiquement à l'intérieur du dossier **extracts**:
+ un **dossier** - *"nom_de_la_catégorie*
    + un **fichier csv** - *"nom_de_la_catégorie_extract.csv"*
    + un **dossier** *"img"* (si le téléchargement des images a été précisé)
        + un **fichier jpg** pour chaque livre de la catégorie - *"nom_du_livre.jpg"* 

### 3. Extraction des données de l'entièreté  du site
Une fois cette option choisie le script s'exécute tout seul. Il faut juste renseigner, avant le démarrage du script, si les images de couvertures doivent être sauvegardées.  
Les données sont stockées dans un dossier nommé **extract_entire_site** et créé automatiquement à l'intérieur du dossier **extracts**:
+ un **dossier** pour chaque catégorie du site - *"nom_de_la_catégorie*
    + un **fichier csv** - *"nom_de_la_catégorie_extract.csv"*
    + un **dossier** *"images"* (si le téléchargement des images a été précisé)
        + un **fichier jpg** pour chaque livre de la catégorie - *"nom_du_livre.jpg"* 

### 4. Mise à jour de la liste des catégories du site
Dans le cas où le site **Books to Scrape** changerait le nom ou le nombre de ses catégories il est possible de mettre à jour dans le programme deux listes:
+ une liste contenant les noms de chaque catégorie
+ une liste associant le nom de la catégorie à sa page Url
Pour mettre ces 2 listes à jour il faut se rendre dans le dossier category_lists.  

Dans un terminal:  

    cd category_lists 
    py list_categories_generator.py




