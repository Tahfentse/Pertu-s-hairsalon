from django.http import request
from django.shortcuts import render
from django.template.context_processors import request

from salonAapp.models import Customer


# Create your views here.
def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        existing_customer = Customer.objects.filter(c_email=email).exists()

        if existing_customer:
            return render(request, 'home.html')
        else:
            Customer.c_name = name
            Customer.c_surname = surname
            Customer.c_email = email
            Customer.c_number = contact
            Customer.c_message = message

            Customer.save()

            return render(request, 'succesfull.html')



    else:
        return render(request, '404.html')
