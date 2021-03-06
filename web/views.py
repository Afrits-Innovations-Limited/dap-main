from web.ext import ip_check
from web.models import Contact
from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import json


def home(request):
    
    config_file = settings.BASE_DIR / "config.json"
    read_file = open(config_file)
    config = json.load(read_file)
    context = {
        "display_partners": config['display_partners']
    }
    return render(request, "index.html", context)


def teams(request):
    
    return render(request, "teams.html")

def faqs(request):
    return render(request, "faqs.html")

def about(request):
    
    return render(request, "about-us.html")

def contact(request):
    if request.is_ajax():
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        subject = "Message from DAP Website"
        body = {
            'name': name,
            'email': email,
            'message': message
        }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, "g.ohunayo@afritsolutions.com", ['g.ohunayo@afritsolutions.com'])
            Contact.objects.create(name=name, email=email, message=message)
            msg = {"success": "Thank You."}
        except BadHeaderError:
            msg = {"error": "Invalid header found."}
        return JsonResponse(msg)
    
    else:
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


def privacy(request):
    
    return render(request, "privacy-policy.html")

def terms(request):
    
    return render(request, "terms.html")


def error_404(request, exception):
    return render(request,'404.html')

