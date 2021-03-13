from django.contrib import admin
from . models import User
from django_mongoengine import mongo_admin  as admin

admin.site.register(User)