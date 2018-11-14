from django.shortcuts import render
from django.http import HttpResponse

events = [
    {
        'title': 'Event1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    },

    {
        'title': 'Event2',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
    {
        'title': 'Event3',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
    {
        'title': 'Event4',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
    {
        'title': 'Event5',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
    {
        'title': 'Event6',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'}

]

sponser = [
    {
        'title': 'Sponser1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser2',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser3',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser4',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser5',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser6',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser7',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponser8',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
]

args = {
    'events': events,
    'sponsers': sponser
}


def home(request):
    return render(request, 'gandharva/index.html', args)
