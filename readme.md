# First CRUD App In Django

The first thing we do is create a virtual environment.
If we don't have it install on our pc, we need to install it.
Make sure you are in the prject directory in the terminal.
Use the terminal and write this command:
`python -m pip install --user virtualenv `

To create it write in the terminal this:
`python -m virtualenv env`

To activate write this:
`env\Scripts\activate`

After we activate the env, we need to pip install few things:
`pip install django`
`django-admin startproject myproj . ` - Pay attention to the `.`, it is necessary.
`django-admin startapp base` - Create application
`py manage.py runserver` - Run server

After we create the app, we need to connect it to the project:
Inside `myproj` folder, go to `settings.py`, and go to the 
`INSTALLED_APPS` list. Add at the end your app (`base`).

Next we go to `urls.py` file in the same folder, and write in the list:
`path('', include('base.urls')),`. Don't forget to import include as well, nect to `path`.

The next thing we Create a Model class that will define the object type - the Table fileds.
* See reference inside the `models.py` in the `base` folder.

Afer we create out tables we need to create a `urls.py` file inside our app folder(`base`).
Inside it we create the urls for our end-points that we will create in the next steps.
Don't forget use this import statement:
`from . import  views`.

Now, we need to create our tables that we've defined. To do so we need to run two commands in the cmd:
`python manage.py makemigrations`
`py manage.py migrate`.
Now we can see that our table are in the sqlite file.

The last thing we need to do, is to create the CRUD in the `views.py` file.

First, we import this:
`from rest_framework.decorators import api_view`
`from .models import Student, Phones`.

Now we create an index page:
Just a simple page for now, to have a landing page(We can use the default page we get with django).

Then, we create the end-points for our urls,
nut we need to determine first which methods are allowd.
for example:
`@api_view(['GET', 'POST'])`