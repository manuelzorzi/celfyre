from django.urls import path

from . import views

app_name = 'motivation'

urlpatterns = [
    path('', views.home, name='home'),
    # add more paths here for other views
]
