"""Platzigram views"""

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Returns a HelloWorld

    Args:
        request (HttpRequest): http request

    Returns:
        HttpResponse: http response
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f'<h1>Current server time is {now}</h1>')


def sort_integers(request):
    """Return a JSON response with sorted integers.

    Args:
        request (HttpResponse): hi
    """
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request,name,age):
    """Say hi

    Args:
        request (Request): say hi
    """
    if age < 12:
        message = f"Sorry {name}, you are not allowed here"
    else:
        message = f'Hello, {name}: Welcome to Platzigram'
    return HttpResponse(message)
