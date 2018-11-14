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

sponsor = [
    {
        'title': 'RedBull',
        'logo': 'gandharva/img/sponsors/redbull.png'
    },
    {
        'title': 'Facebook',
        'logo': 'gandharva/img/sponsors/facebook.png'
    },
    {
        'title': 'Google',
        'logo': 'gandharva/img/sponsors/google.png'
    },
    {
        'title': 'Github',
        'logo': 'gandharva/img/sponsors/github.png'
    },
    {
        'title': 'Microsoft',
        'logo': 'gandharva/img/sponsors/microsoft.png'
    },

]

args = {
    'events': events,
    'sponsors': sponsor
}


def home(request):
    return render(request, 'gandharva/index.html', args)
