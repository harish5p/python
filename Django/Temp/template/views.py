from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    # return HttpResponse("<h1> Welcome </h1>")
    return render(request, 'hello.html', {'name': 'Python'})
