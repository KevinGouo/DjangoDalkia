from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),  # or int:id
    path("", views.home, name="home")
]
