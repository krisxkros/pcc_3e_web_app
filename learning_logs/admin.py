from django.contrib import admin
# The dot in front of models tells Django to look for models.py in the same directory as admin.py.
from .models import Topic

# Register your models here.

# Tells Django to manage our model through the admin site:
admin.site.register(Topic)
