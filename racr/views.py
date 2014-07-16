from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse

from rest_framework import views, viewsets
from rest_framework.response import Response
from racr import models

def main(request):
    if not request.user.is_authenticated():
        return render_to_response('main.html')
    return render_to_response('index.html', {
        'orgname': settings.ORGNAME
    })

def not_registered(request):
    return HttpResponse("<h1>You are not registered for this event.</h1>")

class TimetableViewSet(viewsets.ViewSet):
    def list(self, request):
        pastEvents = [
            {
                'name': '200m Sprint',
                'winner': 'Michael Bates',
                'house': 'Monash',
                'record': 'No'
            },
            {
                'name': '400m Sprint',
                'winner': 'Nick Xanthoudakis',
                'house': 'Gilmore',
                'record': 'Yes'
            },
            {
                'name': 'Under 14 Shotput',
                'winner': 'Matthew Erbacher',
                'house': 'Chisholm',
                'record': 'Yes'
            }
        ]
        return Response({'pastEvents': pastEvents})