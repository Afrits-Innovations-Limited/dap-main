from django.http.response import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def teams(request):
    return render(request, "teams.html")

def faqs(request):
    return render(request, "faqs.html")

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact.html")

def blogs(request):
    return render(request, "blogs.html")

def single_blog(request, slug):
    return render(request, "blog_single.html")

def newsletter(request):
    if request.is_ajax():
        email = request.POST["email"]
        name = email.split("@")[1]
        msg = {"success": "Okay"}
        return JsonResponse(msg)
