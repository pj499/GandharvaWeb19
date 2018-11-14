from django.http import HttpResponse
from django.shortcuts import render_to_response


def register(request):
    return render_to_response('registrations/register.html')
