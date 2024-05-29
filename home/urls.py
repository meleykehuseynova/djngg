from django.urls import path
from .views import products_page,products_about

urlpatterns=[
    path("",products_page),
    path("about/",products_about),
]