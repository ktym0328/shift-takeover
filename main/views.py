from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Tickets


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def detail(request, ticket_id):
    return HttpResponse("you're looking at ticket %s." % ticket_id)
