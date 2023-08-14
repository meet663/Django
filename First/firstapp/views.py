from django.shortcuts import render, HttpResponse
from datetime import datetime
from firstapp.models import contact
from django.contrib import messages


# Create your views here.
def index(request):
    messages.success(request, "This is test meassage")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact1 = contact(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact1.save()
        messages.success(request, "Your message has been sent")
    return render(request, "contact.html")
