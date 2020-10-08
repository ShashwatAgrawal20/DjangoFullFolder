from django.urls import path

from . import views

urlpatterns = [
    # Showing the blank path because the user comes from the mysite.urls here by inputing the path named as polls
    path('',views.index, name='index'),
]