from django.contrib import admin
from . models import Blog
from django_mongoengine import mongo_admin  as admin

admin.site.register(Blog)