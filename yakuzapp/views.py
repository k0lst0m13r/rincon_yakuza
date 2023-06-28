from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    ctx = {}
    return render(request, 'yakuzapp/index.html', ctx)
