from django.shortcuts import render
from django.http import HttpResponse
from Sponsors.models import SponsorMaster

# sponsor = [
#     {
#         'title': 'RedBull',
#         'logo': 'gandharva/img/sponsors/redbull.png'
#     },
#     {
#         'title': 'Facebook',
#         'logo': 'gandharva/img/sponsors/facebook.png'
#     },
#     {
#         'title': 'Google',
#         'logo': 'gandharva/img/sponsors/google.png'
#     },
#     {
#         'title': 'Github',
#         'logo': 'gandharva/img/sponsors/github.png'
#     },
#     {
#         'title': 'Microsoft',
#         'logo': 'gandharva/img/sponsors/microsoft.png'
#     },
#
# ]


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

events = [
    {
        'title': 'Mech Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/mech.jpg',
        'linkTo': 'event1'
    },

    {
        'title': 'ENTC Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/entc.jpg', 'linkTo': 'event1'
    },
    {
        'title': 'Comp Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/comp.jpg', 'linkTo': 'event1'},
    {
        'title': 'IT Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/it.jpg', 'linkTo': 'event1'},
    {
        'title': 'Civil Events',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'gandharva/img/deptEvent/civil.jpg', 'linkTo': 'event1'},

]

category1_events = [
    {
        'title': 'Blind Coding',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'events/img/mech.jpg',
        'linkTo': 'category1Event1'
    },
    {
        'title': 'Get Hired',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'events/img/entc.jpg',
        'linkTo': 'category1Event1'
    },
    {
        'title': 'Web Design',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'events/img/comp.jpg',
        'linkTo': 'category1Event1'
    },
    {
        'title': 'Reverse Coding',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. ',
        'img': 'events/img/it.jpg',
        'linkTo': 'category1Event1'
    },
]

blind_coding = {
    'objective': 'The objective of this event is to test the proficiency of the participant in C Programming Language. This event aims at beginners and intermediates in C programming only. The event covers the basic principles of C Programming Language.',
    'round1': 'A Multiple choice questions(MCQ) round. Time allotted is 30 minutes. Negative marking will be implemented. Further details will be informed to the team at the time of event.',
    'round2': 'The top teams from the Round 1 will qualify for this round. This round will be a rapid coding round where the team has to complete the codes within the stipulated time. The output file needs to be submitted and will be judged on the basis of the time taken to code it. Further details will be informed to the team at the time of event.',
    'team_Fees': 'Max 2 participants per team & ₹ 50 per team.',

}

blind_coding_rules = [
    'The environment will be either Ubuntu 14.04 OS with gedit/vim/emacs as text editor and gcc as compiler OR Windows 7 with Turbo C / Dev C++ (as per the teams choice).',
    'Participants should be First Year or Second Year Undergraduate students.',
    'Participants need to bring their College ID cards and the receipt of registration during reporting.',
    'Participants are expected to give their correct contact details, so as to inform them about the results.',
    'In case of any disputes, the decision of the organizers and the judges will be final and binding to all.',
    'Team members may be from different colleges / institutions but one participant may not be a part of multiple teams for the same event.']


gandharvaDate = '01/01/2019' #mm/dd/yyyy

sponsor_list = SponsorMaster.objects.all()
sponsor = [{'title': i.sponsor_name, 'logo': i.sponsor_logo} for i in sponsor_list]

args = {
    'events': events,
    'sponsors': sponsor,
    'carouselImage': carouselImages,
    'gandharvaDate' : gandharvaDate
}

args1 = {
    'pageTitle': 'Events Category',
    'category1_events': category1_events,
    'events': events,
}

args2 = {
    'pageTitle': 'Blind Coding',
    'category1_events': category1_events,
    'events': events,
    'rules':blind_coding_rules,
    'blind_coding':blind_coding
}


def home(request):
    return render(request, 'gandharva/index.html', args)


def event1(request):
    return render(request, 'events/event1.html', args1)


def category1Event1(request):
    return render(request, 'events/category1Event1.html', args2)
