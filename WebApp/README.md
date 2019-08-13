## Understanding what our WebApp is...
### What is an App?
The term "application" describes a Python package that provides some set of features.           
Applications include some combination of models, views, templates, template tags, static files, URLs, middleware, etc.       
Django forces creators to break his/her code into these "apps".
#### *manage.py*
This is a container for all of our project's applications. 
Think of the arguments passed to manage.py as subcommands. It is a tool for executing many Django-specific tasks. It is also an extension point where developers can create custom commands that are specific to his/her app.
### Our "Apps"...
- *about*: For the *About page* on our website
- *floor3*: For the *Floor 3 page* on our website
- *floor4*: For the *Floor 4 page* on our website
- *stats*: For the *Stats page* on our website
### Now we will explore the general layout of each of our "Apps"...
#### *admin.py*
This file is where we put all of our configuration regarding the Django builtin admin.
In other words, it is used to display our models in and customize the Django admin pannel
#### *apps.py*
This file is used in Django's internal app registry and is mainly used to store metadata. For the most part, we do not modify this.
#### *__init__.py*
This file is Python's convention for determining modules. When one tries to run ```import library``` or ```from library import``` Python will search all folders in the Python path. If a folder has an ```__init__.py``` file, Python will also search inside of that folder, otherwise, it is ignored.
#### *migrations folder*
Migrations are how Django builds your database. Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. The migration files for each app live in this migrations directory.
#### *models.py*
This file is where we store all of our models related to the app. Models are how Django understands our databse and how we want our data stored.
#### *tests.py*
This file is for adding unit and integration tests. A test is code one writes to make sure his/her code is running how he/she expected.
#### *views.py*
A view is simply a Python function that takes a web request and returns a web response. The views.py file is where we define all of our views related to this app, both Class-Based and Function-Based. 
#### *urls.py*
This file is used to store app specific mappings of URLs to views.    
For every URL that starts with ```admin/```, Django will find a corresponding view. 
#### *static & templates folders*
These folders are simply used to store static files or template files in each of our applications. They are stored into a single location that can easily be served.
