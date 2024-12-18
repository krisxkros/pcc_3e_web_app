# Django basics

Django is popular **'web framework'**: a set of tools designed for building interactive web applications.

A Django project is organized as a group of individual apps that work together to make the project work as a whole.

> ## Summary
>
> 1. [Create ąnd activate virtual environment](#create-and-activate-new-virtual-environment)
> 2. Update pip and install django
> 3. [Create a project (using terminal)](#creating-a-project-in-django)
>
>```bash
># !!! DO NOT forget the dot (.) in the end !!!
>django-admin startproject `project_name` .
>```
>
> 4. [Create database](#creating-the-database)
>
>```bash
>python manage.py migrate
>```
>
> 5. [Start local server](#viewing-the-project)
>
>```bash
>python manage.py runserver
>```
>
> 6. [Stop local server](#stop-localserver)
>
>```bash
>CTRL-C
>```
>
> 7. [Template Language Syntax](#template-language-syntax)
>
> - Variables: `{{ first_name }}`
> - Tags: `{% for topic in topics %}`
> - Filters: `{{ entry.date_added|date:"d.M.Y, H:i" }}`
> - Comments: `{% comment %}`
>
> 8. [Start the app](#starting-an-app) (in new terminal window, run where 'manage.py' is located)
>
>```bash
>python manage.py startapp 'app_name'
>```
>
> 9. [Define models](#defining-models) in `models.py`
>
> 10. [Activate models](#activating-models) in `settings.py`
>
> - list 'app_name' app before default apps
> - migrate database after that:
>
>```bash
>python manage.py makemigrations `app_name`
>python manage.py migrate
>```
>
> 11. [Create superuser](#the-django-admin-site)
>
>```bash
>python manage.py createsuperuser
>```
>
> 12. [Register models](#registering-models-with-an-admin-site) in `admin.py`
>
> 13. [Django Shell](#the-django-shell)
>
> Creating pages:
>
> 14. [Mapping URLs](#mapping-urls)
>
>- `urls.py` in main folder
>- `urls.py` in app folder
>
> 15. [Writing views](#writing-views)
>
>- `views.py`
>
> 16. [Writing templates](#writing-templates)
>
>- `.html`

## Setting up a project

1. Describe the project’s goals in a specification, or *spec*
2. Once you have a clear set of goals, you can start to identify manageable tasks to achieve those goals.

### Writing a spec

We’ll write a web app called Learning Log that allows users to:

- log the topics they’re interested ii
- make journal entries as they learn about each topic

The Learning Log home page will:

- describe the site
- invite users to either register or log in

Once logged in a user can:

- create new topics
- add new entries
- read and edit existing entries

### Create and activate new virtual environment

Separating one project’s libraries from other projects is beneficial and `will be necessary` when we deploy the project to a server.

```bash
python -m venv 'venv_name'

source 'venv_name'/Scripts/Activate
```

### Creating a Project in Django

With .venv active, enter the following command in a command line:

```bash
# !!! Don’t forget the dot (.) at the end !!!
django-admin startproject `project_name` .
```

**!!Don’t forget the dot (.) at the end!!** of the above command, or you might run into some configuration issues when you deploy the app. If you forget the dot, delete the files and folders that were created (except `project-name`) and run the command again.

This command creates:

- **´project-name` directory** with some files inside. Most important are:
- settings.py: controls how Django interacts with your system and manages your project
- urls.py: tells Django which pages to build in response to browser requests
- wsgi.py: helps Django serve the files it creates (acronym for “web server gateway interface.”)
- **manage.py**
  - a short program that takes in commands and feeds them to the relevant part of Django
  - these commands manage the tasks, such as working with databases and running servers

### Creating the Database

Django stores most of the information for a project in a database.

With .venv active, enter the following command in a command line:

```bash
python manage.py migrate
```

Anytime we modify a database, we say we’re *migrating* the database.

The first time we run this command in a new project using SQLite, Django will:

- create a new database for us to store information it needs to handle administrative and authentication tasks

SQLite is a database that runs off a single file:

- it’s ideal for writing simple apps
- you don’t have to pay much attention to managing the database

### Viewing the project

To view the project in the current state, enter the following command in a command line:

```bash
python manage.py runserver
```

Django starts a the development server, so you can view the project on your system.

You can view the project by entering the following url in a browser:

> <http://127.0.0.1:8000/>

The above URL indicates that the project is listening for requests on port 8000 on your computer, which is called a localhost.

The term localhost refers to a server that only processes requests on your system; it doesn’t allow anyone else to see the pages you’re developing.

#### Stop 'localserver'

When you want to stop the server, press **'CTRL-C'** in the terminal where the runserver command was issued and close the browser window.

#### Troubleshoot: “That port is already in use”

Use different port like 8001, 8002, 8003... with the following command:

```bash
python manage.py runserver 8001
```

## Template Language Syntax

[Documentation](https://docs.djangoproject.com/en/5.1/ref/templates/)

- [Templates topic guide](https://docs.djangoproject.com/en/5.1/topics/templates/)

### Variables

A variable outputs a value from the context, which is a *dict-like object mapping keys to values*.

>`{{ abc }}`

```django
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

```json
{'first_name': 'John', 'last_name': 'Doe'}
```

Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:

```django
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

### Tags

[Reference of built-in tags](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-tags)

Tags provide arbitrary logic in the rendering process.

>`{% abc %}`

```django
{% csrf_token %}

# Most tags accept arguments:
{% cycle 'odd' 'even' %}

# Some tags (for, if) require beginning and ending tags:
{% for topic in topics %}
    <li><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic.text }}</a></li>
{% empty %}
<li>No topics have been added yet.</li>
{% endfor %}
```

A tag can:

- output content
- serve as a control structure e.g. an `“if" statement` or a `“for” loop`
- grab content from a database
- enable access to other template tags

### Filters

[Reference of built-in filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters)

Filters transform the values of variables and tag arguments.

>`{{ django|title }}`

```django
# Some filters take an argument:
{{ entry.date_added|date:"d.M.Y, H:i" }}
```

### Comments

>`{# this won't be rendered #}`

A `{% comment %}` tag provides multi-line comments.

## Starting an app

1. Leave the development server running in the in the terminal window.
2. Open a new terminal window:
    - navigate to the directory that contains 'manage.py
    - activate the virtual environment
    - run the 'startapp' command:

```bash
python manage.py startapp `app_name`
```

Django creates 'folder_name' with new files. Most important are:

- 'models.py': define the data you want to manage in the app
- 'admin.py'
- 'views.py'

### Defining models

>Check `models.py`

[Django `model` docs >>](https://docs.djangoproject.com/en/5.1/topics/db/models/)

[Django `field` docs >>](https://docs.djangoproject.com/en/4.1/ref/models/fields/)

```python
# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    # 'ForeignKey: connect each entry with a particular topic
    # 'on_delete=models.CASCADE': when a topic is deleted, all the entries associated
    # with that topic should be deleted as well. This is known as a 'cascading delete'.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        return self.text
```

It’s a good idea to tell Django how you want it to represent an instance of a model.

If a model has a '**str**()' method, Django calls that method whenever it needs to generate output referring to an instance of that model.

### Activating models

>Check `settings.py`

To use our models, we have to tell Django to include our app in the overall project.

1. Open 'setting.py' and add 'app_name' in 'INSTALLED_APP = []' section.

```python
INSTALLED_APPS = [
    # My apps:
    'learning_logs',
    # Default django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Grouping apps together in a project helps keep track of them as the project grows to include more apps.

**It’s important to place your own apps before the default apps**, in case you need to override any behavior of the default apps with your own custom behavior.

Next, we need to tell Django to modify the database so it can store information related to the model Topic.

2. Enter the following command where the 'manage.py' is located:

```bash
python manage.py makemigrations `app_name`
```

The command makemigrations tells Django to figure out how to modify the database so it can store the data associated with any new models we’ve defined.

3. Apply this migration and have Django modify the database:

```bash
python manage.py migrate
```

Check the last line in this output: .... OK

#### Whenever you want to modify the database, follow these three steps

>1. modify `models.py`
>2. call 'makemigrations' on `app_name`
>3. tell Django to `migrate` the project

You need to run the `python manage.py migrate` command in the following situations:

- After creating a new model
- After making changes to an existing model
- After installing a new Django app
- After applying model changes from a third-party app
- After running `python manage.py makemigrations`
- When deploying your Django application

### The Django admin site

Django’s admin site is only meant to be used by the site’s administrators.

#### Setting up a superuser

To create a superuser in Django, enter the following  command and respond to the prompts:

```bash
python manage.py createsuperuser
```

Django stores passwords as hashes.

### Registering models with an admin site

> Check `admin.py`

Django includes some models in the admin site automatically, such as *User* and *Group*.

Other models needs to be added manually.

*Troubleshoot*: If you’re having trouble viewing your project at any point in the development process, **closing any open terminals** and **reissuing the 'runserver' command** is a good first troubleshooting step.

```python
from django.contrib import admin

# The dot in front of models tells Django to look for models.py in the same directory as admin.py.
from .models import Topic, Entry

# Register your models here.

# Tells Django to manage our model through the admin site:
admin.site.register(Topic)
admin.site.register(Entry)
```

### The Django shell

**Django shell**: programmatically examine all the data entered (in `db.sqlite3`) through an interactive terminal session.

>You can GUI examine and edit the same data with `DB Browser (SQLite)`
>
>Querying is case sensitive!

[Query reference >>](https://docs.djangoproject.com/en/4.1/topics/db/queries/)

Start Django shell:

```bash
python manage.py shell
```

Import module from modules.py you want to test:

```python
from learning_logs.models import Topic
# queryset: [get all instances of the model Topic]
Topic.objects.all()
```

You can loop over a querryset:

```python
topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)
```

Retrieve that object and examine any attribute the object has:

```python
t = Topic.objects.get(id=3)
t.text
t.date.added
```

Look at the entries related to a certain topic:

```python
t.entry_set.all()
```

## Making pages: the Home Page

Making webpages with Django consists of three stages (in any order):

>- mapping URLs
>- writing views
>- writing templates

### Mapping URLs

A URL pattern describes the way the URL is laid out.

It also tells Django what to look for when matching a browser request with a site URL, so it knows which page to return.

1. `urls.py` in the main folder (ll_project)

Defines URLs for the project as a whole and includes sets of URLs from all apps in the project.

We need to include the URLs for learning_logs app:

```python
...
from django.urls import path, include

urlpatterns = [
    ...
    path("", include("learning_logs.urls")),
]
```

2. `urls.py` in the app folder (learning_logs)

Maps the URLs exclusively for learning log app.

Crate new urls.py file inside `learning_logs` folder

> Check `urls.py` in `learning_logs` folder

```python
"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
  # Home page
    path('', views.index, name='index')
]
```

### Writing views

 Check `views.py` in `learning_logs` folder

Each URL then maps to a particular view. The view function retrieves and processes the data needed for that page.

A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browser. It often does this by using a template that defines what the page will look like.

```python
def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")
```

### Writing templates

The view function often renders the page using a template, which contains the overall structure of the page.

The template defines what the page should look like. A template allows you to access any data provided by the view.

>Check `index.html`

Create index.html in (folder structure for templates is important):

- `learning_logs` folder /`templates` folder /`learning_logs` folder /`index.html`

## Building additional pages

Before creating additional pages, create a base template that all templates in the project can inherit from.

### Template inheritance

**Base template** contains the repeated elements and then have each page inherit from the base. Base template alements are common to all pages.

This approach makes it much easier to change the overall look and feel of the project.

#### The parent template

>Check `base.html`

```html
<a href="{% url 'learning_logs:index' %}">Learning Log</a>
```

To generate a link, we use a `template tag`: ({% %}). 

`{% url 'learning_logs:index' %}`: generates a URL matching the URL pattern defined in learning_logs/urls.py with the name 'index'. 

- `learning_logs` is the namespace (= `app_name` in the learning_logs/urls.py file)
- `index` is a uniquely named URL pattern in that namespace

#### The child template

>Check `index.html`

Thr child template must have an `{% extends "parent path" %}` tag on the first line to tell Django which parent template to inherit from.

```django
{% extends "learning_logs/base.html" %}
```

Everything NOT inherited from the parent template goes inside the `content block`.

```django
{% block content %}
...
{% endblock content %}
```

In a large project, it’s common to have:
- one parent template called `base.html` for the entire site
- parent templates for each major section of the site
- all the section templates inherit from base.html
- each page in the site inherits from a section template

This way you can easily modify the look and feel of the site as a whole, any section in the site, or any individual page.
