from django.urls import path
from . import views

app_name = 'yakuzapp'

urlpatterns = [
    path("", views.index, name="index"),
]