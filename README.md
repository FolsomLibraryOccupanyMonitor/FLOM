# FLOM

### Folsom Library Occupancy Manager

http://www.flom.ml

Develop an embedded system that allows students to sign into a website with their RCS ID to check what study rooms in the library are occupied and which are not. This will increase students' efficiency when studying. 

## Build Instructions

Clone the URI and run the `manage.py` file located in the \_software directory.

`python manage.py runserver`

Your local build will require access to a database. Our implementation uses [Postgres](https://www.postgresql.org/) and you can create a `config.ini` file with data to your local database. Alternatively, we can set you up with access to our AWS database if you want to join our team.

You may need to download these python libraries (if you don't already have them).

```pip install Django``` \
```pip install psycopg2``` \
```pip install memcache``` 

## Code of Conduct and Style Guidelines

Our developers pride ourselves on writing beautiful and efficient code. Contributers should follow standard good style practices such as
useful commenting, proper indentation, and portability. Our software app directory looks like this

    `database/`         - Database objects, queries, and all things postgres 
    `flom/`             - Main settings and urls 
    `library_monitor/`  - Front end styles and templates 
    `static/`           - Main scripts and styles 
    `templates/`        - Main template files 
    `config.ini`        - Required metadata for database connection 
    `manage.py`         - Managing file from Django 
    
Please refer to this [Django tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) or simply the 
[Django 2.2 documentation](https://docs.djangoproject.com/en/2.2/) for information about using our framework. Django provides a robust templating framework for HTML (that means please use it).

## Git Branching Model

When making a new feature or a bug fix, please make a new branch from **Dev** (short for develop). On your command line, run 

`git checkout dev` \
`git branch [new branch name]` \
`git checkout [new branch name]` 

Branch names should be concise and self-explanatory. Please make your branch names lowercase and use hyphens (-) for spaces. You don't need to prepend your branch name with "dev" or include other details such as your name. For example, a feature branch for updating the about page UI might be called `about-styles` or `about-page-ui`. 

When you have changes to your local code base in your new branch, commit push them with 

`git commit -m [Commit message]` \
`git push` 

Commit messages should be concise and self-explanatory, just like branch names. 

Once your have completed your feature or fixed you bug, please perform a **Pull Request** into dev, even if you are an admin. Pull requests provide a more readable commit log, highlighting major features and changes. On the Github repository website, click new pull request and select `"dev" <- "your branch name"`. This allows an admin to approve your changes before they are live on the develop branch. 
