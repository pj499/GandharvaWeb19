from django.shortcuts import render
from django.http import HttpResponse

events = [
    {
        'title': 'Mech Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/mech.jpg'
    },

    {
        'title': 'ENTC Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/entc.jpg'},
    {
        'title': 'Comp Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/comp.jpg'},
    {
        'title': 'IT Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/it.jpg'},
    {
        'title': 'Civil Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/civil.jpg'},

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
