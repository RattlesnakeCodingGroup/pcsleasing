from django.contrib import admin
from . import models

# Register your models here.
from .models import Contact

admin.site.register(Contact)