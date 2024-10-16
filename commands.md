py -m venv venv
source venv/Scripts/activate
pip install django
django-admin startproject core .
py manage.py startapp users