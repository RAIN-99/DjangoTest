from django.urls import path
from . import views

urlpatterns = [
    path("data/",views.DATA.as_view()),
]