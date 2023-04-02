from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, "classifier/index.html")

texts = ["Hot dog",
         "Wiener dog",
         "Cord Dog"]

def section(request, num):
    if 1<=num<=3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404('No such section')
# Create your views here.
