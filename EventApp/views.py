from django.shortcuts import render
from EventApp.models import Department, EventMaster, Carousel, SponsorMaster
# Create your views here.


def home(request):
    args = {
        'events': Department.objects.all(),
        'sponsors': SponsorMaster.objects.all(),
        'carouselImage': Carousel.objects.all(),
        'gandharvaDate': '01/01/2019'
    }
    return render(request, 'gandharva/index.html', args)


def event(request):
    if request.POST:
        dept = request.POST.get('dept') + ' Events'
    else:
        dept = 'All Events'
    args1 = {
        'pageTitle': dept,
        'events': EventMaster.objects.all(),
    }
    return render(request, 'events/event1.html', args1)


def details(request):
    event_name = request.POST.get('event')
    arg = {
        'events_list': EventMaster.objects.all(),
        'pageTitle': EventMaster.objects.get(event_name__startswith=event_name).event_name,
        'event': EventMaster.objects.get(event_name__startswith=event_name),
        'rules': EventMaster.objects.get(event_name__startswith=event_name).rules.split('. '),
    }
    return render(request, 'events/category1Event1.html', arg)
