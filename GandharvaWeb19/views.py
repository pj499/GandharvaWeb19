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
        'title': 'Sponsor1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor2',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor3',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor4',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor5',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor6',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor7',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'title': 'Sponsor8',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
]

args = {
    'events': events,
    'sponsors': sponsor
}


def home(request):
    return render(request, 'gandharva/index.html', args)
