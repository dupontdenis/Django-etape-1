from django.shortcuts import render, redirect
from .models import Person

def person_list(request):
    persons = Person.objects.all()
    return render(request, "myapp/person_list.html", {"persons": persons})

def person_create(request):
    if request.method == "POST":
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        Person.objects.create(first_name=first, last_name=last)
        return redirect("person_list")
    return render(request, "myapp/person_create.html")
