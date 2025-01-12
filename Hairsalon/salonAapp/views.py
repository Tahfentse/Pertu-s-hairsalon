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
        contacts = request.POST.get('contact')
        message = request.POST.get('message')
        existing_customer = Customer.objects.filter(c_email=email).exists()

        if existing_customer:
            return render(request, 'home.html')
        else:
            new_customer = Customer(
                c_name=name,
                c_surname=surname,
                c_email=email,
                c_number=contacts,
                c_message=message
            )
            # Save the new instance to the database
            new_customer.save()
            return render(request, 'succesfull.html')
    else:
        return render(request, '404.html')
