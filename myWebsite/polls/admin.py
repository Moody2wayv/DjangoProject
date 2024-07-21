from django.contrib import admin
from .models import Question, Choice

# Registering models here.
admin.site.register(Question)
admin.site.register(Choice)
