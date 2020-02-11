from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>response text goes in here</h1'>)
