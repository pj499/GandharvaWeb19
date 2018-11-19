from django.shortcuts import render
from EventApp.models import Department,EventMaster

# Create your views here.


dep_list = Department.objects.all()

events = [
    {'title': dep.name+' Events', 'description': dep.description, 'img': dep.img, 'linkTo': dep.link_to}
    for dep in dep_list
]


events_list = EventMaster.objects.all()
category1_events = [
    {
        'title': eve.event_name,
        'description': eve.objective,
        'img': 'events/img/mech.jpg',
        'linkTo': 'category1Event1'
    }
    for eve in events_list
]

args1 = {
    'pageTitle': 'Events Category',
    'category1_events': category1_events,
    'events': events,
}

args2 = {
    'pageTitle': 'Blind Coding',
    'category1_events': category1_events,
    'events': events,
    'rules': EventMaster.objects.get(event_name='Blind Coding').rules.split('. '),
    'blind_coding': EventMaster.objects.get(event_name='Blind Coding')
}


def event(request):
    return render(request, 'events/event1.html', args1)


def category1Event1(request):
    return render(request, 'events/category1Event1.html', args2)
