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