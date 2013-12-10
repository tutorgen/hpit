from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden

from core.models import Student
from bson.objectid import ObjectId

#default view for app
def index(request):
    my_list = range(10)

    return render(request, 'index.html', {
        'var': ' World!',
        'list': my_list
    })


#/student/
#- POST {arbitrary data} => guid
def create_student(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    new_student = Student()

    if 'client_student_id' in request.POST:
        new_student.client_student_id = request.POST['client_student_id']

    if 'attributes' in request.POST:
        for attr_name, attr_value in request.POST['attributes']:
            new_student.attributes[attr_name] = attr_value

    new_student.save()

    return HttpResponse(new_student.to_json(), content_type="application/json")
    
#/student/(?P<id>\d+)/
# - GET list of all arbitrary data about a student
def student(request, id):
    if request.method != "GET":
        return HttpResponseBadRequest()

    this_student = Student.objects(pk=ObjectId(id))

    return HttpResponse(this_student.to_json(), content_type="application/json")


#/student/(?P<id>\d+)/attribute/
# - POST {key:values}
# - PUT {key:values}
# - GET {key:values}
def student_attribute(request, id):
    if request.method == "DELETE":
        return HttpResponseBadReqeust()

    return HttpResponseNotFound()

#/student/(?P<id>\d+)/attribute/(?P<name>[\w-?]+)/'
# - GET value for specific key :name on student
def student_attribute_name(request, id, name):
    if request.method != "GET":
        return HttpResponseBadRequest()

    return HttpResponseNotFound()
        
#/student/(?P<id>\d+)/question/(?P<question_id>\d+)/
# - GET next hint for the student
def student_question_hint(request, id, question_id):
    if request.method != "GET":
        return HttpResponseBadRequest()

    return HttpResponseNotFound()
    
#/student/(?P<id>\d+)/question/(?P<question_id>\d+)/
# - GET next question student should answer
def student_question_next(request, id, question_id):
    if request.method != "GET":
        return HttpResponseBadRequest()

    return HttpResponseNotFound()
