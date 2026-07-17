from django.http import HttpResponse

def index(request):
    return HttpResponse("FIXIT is working!")