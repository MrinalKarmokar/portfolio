import datetime

from django.shortcuts import render

# Create your views here.

today = datetime.datetime.now().date()
current_time = datetime.datetime.now().strftime("%H:%M:%S")

#--------------------------------------------------------------------------
def icon_view(request, *args, **kwargs):
    context = {}
    return render(request, 'pages/icon.html', context)


#--------------------------------------------------------------------------
def index_view(request, *args, **kwargs):
    context = {
        "today" : today,
        "time" : current_time,
    }
    return render(request, 'pages/index.html', context)


#--------------------------------------------------------------------------
def email_verified_view(request, *args, **kwargs):
    context = {}
    return render(request, 'pages/email_verification_done.html', context)


#--------------------------------------------------------------------------
def home_view(request, *args, **kwargs):

    first_name = request.session.get('first_name', default="Guest")

    context = {
        "today" : today,
        "time" : current_time,
        'first_name' : first_name,
    }

    return render(request, 'pages/home.html', context)


#--------------------------------------------------------------------------
def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, 'pages/contact.html', context)