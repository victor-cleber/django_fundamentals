# Django 2.0 - Fundamentals
It is a exercise in how to implement the MTV Django pattern.

1  Create a project in your Git Hub
2  Run clone the project 
3  Run python -m venv venv 
4  (Linux) run source venv/bin/activate
5  (Windows) venv\Scripts\activate
6  Install Django >> pip install django
7  Create a project running >> django-admin startproject control_spending
8  Remove app folder control_spending/control_spending
9  Create an app project inside actual folder by running django-admin startproject control_spending . to create all files inside the main folder
10 Create a new app >> python manage.py startapp bills 
11 Configure a new app in settings.py - Add 'bills', in INSTALLED_APPS 
12 Run migrate to create a database >> python manage.py migrate
13 Running a web application >> python manage.py runserver
14 Create a super user to manage the app >> python manage.py createsuperuser
15 Access 127.0.0.1:8000