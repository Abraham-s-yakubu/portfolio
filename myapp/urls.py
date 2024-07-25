from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("resume.html", views.resume, name="resume"),
    path("contact.html", views.contact, name="contact"),
    path("projects.html", views.project, name="project")
]
