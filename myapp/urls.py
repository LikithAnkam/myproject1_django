from django.urls import path
from .views import about,home,contact,login,register

urlpatterns=[
    path("about/",about),
    path("",home), 
    path("contact/",contact),
    path("login/",login),
    path("register/",register)
]
