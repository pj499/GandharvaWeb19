from django.shortcuts import render
from Sponsors.models import SponsorMaster
from EventApp.models import Department

carouselImages = [
    {
        'src': 'gandharva/img/1.jpg'
    },
    {
        'src': 'gandharva/img/2.jpg'
    },
    {
        'src': 'gandharva/img/3.jpg'
    },
    {
        'src': 'gandharva/img/5.jpg'
    },
    {
        'src': 'gandharva/img/6.jpg'
    },
    {
        'src': 'gandharva/img/7.jpg'
    },
    {
        'src': 'gandharva/img/8.jpg'
    },
    {
        'src': 'gandharva/img/9.jpg'
    },
    {
        'src': 'gandharva/img/10.jpg'
    },
    {
        'src': 'gandharva/img/11.jpg'
    }
]


sponsor_list = SponsorMaster.objects.all()
sponsor = [{'title': i.sponsor_name, 'logo': i.sponsor_logo} for i in sponsor_list]

dep_list = Department.objects.all()

events = [
    {'title': dep.name+' Events', 'description': dep.description, 'img': dep.img, 'linkTo': dep.link_to}
    for dep in dep_list
]


gandharvaDate = '01/01/2019' #mm/dd/yyyy

args = {
    'events': events,
    'sponsors': sponsor,
    'carouselImage': carouselImages,
    'gandharvaDate' : gandharvaDate
}


def home(request):
    return render(request, 'gandharva/index.html', args)
