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
    dept = "Events"
    events_list = EventMaster.objects.all()
    events = [
        {
            'title': eve.event_name,
            'description': eve.objective,
            'linkTo': 'details'
        }
        for eve in events_list
    ]

    args1 = {
        'pageTitle': dept,
        'events': events,
    }
    return render(request, 'events/event1.html', args1)


def details(request):
    arg = {
        'event': EventMaster.objects.get(event_id=1),
        'rules': EventMaster.objects.get(event_id=1).rules.split('. '),
    }
    return render(request, 'events/category1Event1.html', arg)
