from django.contrib import admin
from . import models

# Register your models here.
from .models import Contact, Agents

admin.site.register(Contact)
admin.site.register(Agents)
