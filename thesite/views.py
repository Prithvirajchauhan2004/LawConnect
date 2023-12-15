from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, 'thesite/index.html')

def legal_advisors(request):

    return render(request, 'thesite/advisors_list.html')