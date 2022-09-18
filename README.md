# Django Web App course

## Merch Exchange

Learn Django by building web app

## Installation process

- Create virtual env:</br>
`python -m venv {environment name}`
- Install Django:</br>
`pip install django`
- Start Project:</br>
`django-admin startproject {project name}`

## Configure web app

In the {project name} directory, you can run any django command with:</br>
`./manage.py {command}` or `python manage.py {command}`
- Apply all migrations:</br>
`./manage.py migrate`
- Create new app:</br>
`./manage.py startapp {app name}`
- Then add {app name} to INSTALLED_APPS list in {project name}/settings.py
- After creating models, run:</br>
`./manage.py makemigrations`, then:</br>
`./manage.py migrate` to migrate to DB

To create object, you can use the Django shell: `./manage.py shell`
Then, import Model: `from {app name}.models import Obj`
And, finally, create objects:
- `obj = Obj()`
- `obj.name = 'Name'`
- `obj.save()`
or:
- `obj = Obj.objects.create(name='Name')`

To count objects in DB:
`Obj.objects.count()`
And to display them:
`Obj.objects.all()`

After update models.py, if `migrate` command return `table already exists`, run:
`./manage.py migrate --fake {app name}`
> NOTE: I was forced to remove db.sqite3, \_\_pycache\_\_/ and migrations/*.py because I encountered an OperationalError: no such table: listings_band. Then I run: 
1. `./manage.py makemigrations {app name}`
2. `./manage.py migrate --run-syncdb`