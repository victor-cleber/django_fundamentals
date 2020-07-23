Django 2.0 - Fundamentals
It is a exercise in how to implement the MTV Django pattern.

### Baby steps

[1] Create a project in your Git Hub 
[2] Clone your project 
[3] Enable virtual env 
```sh
$ python -m venv venv
```
[4] Activate virtual env (Linux)
```sh
$ source venv/bin/activate 
```
[5] Activate virtual env (Windows) 
```sh
$ venv\Scripts\activate
```
[6] Install Django 
```sh
$ pip install django 
```
[7] Create a project 
```sh
$ django-admin startproject control_spending 
```
[8] Remove app folder control_spending/control_spending 
[9 Create an app project inside actual folder by running 
```sh
$ django-admin startproject control_spending . 
```
[10] Create a new app
```sh
$ python manage.py startapp bills
``` 
[11] Configure a new app in settings.py - Add 'bills', in INSTALLED_APPS 
[12] Run migrate to create a database
```sh
$ python manage.py migrate 
``` 
[13] Running a web application
```sh
$ python manage.py runserver
```  
[14] Create a super user to manage the app
```sh
$ python manage.py createsuperuser
```   
[15] Verify the deployment by navigating to your server address in your preferred browser.
```sh
127.0.0.1:8000
```   
