from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden

#default view for app
def index(request):
    my_list = range(10)

    return render(request, 'index.html', {
        'var': ' World!',
        'list': my_list
    })
