from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def resume(request):
    return render(request, "resume.html")


def contact(request):
    return render(request, "contact.html")


def project(request):
    return render(request, "projects.html")
