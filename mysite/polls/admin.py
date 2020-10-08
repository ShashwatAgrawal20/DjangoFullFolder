from django.contrib import admin

from .models import Question
# Registering the app by doing the step below
admin.site.register(Question)