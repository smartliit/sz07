from django.http import HttpResponse

def index(request):
    return HttpResponse('index page')


def goods(request):
    return HttpResponse('goods page')
