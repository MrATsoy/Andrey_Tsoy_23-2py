from django.http import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse("Hello! It's my first project")


def now_date(request):
    current_time = datetime.now()
    return HttpResponse(f'Current date and time: {current_time}')


def goodbye(request):
    return HttpResponse('Goodbye user!')