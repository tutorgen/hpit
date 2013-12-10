import json
from bson.objectid import ObjectId
from bson.errors import InvalidId
from mongoengine.django.shortcuts import get_document_or_404

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden

from core.models import Student

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
    data = json.loads(request.body)

    #import pdb; pdb.set_trace()

    if 'client_student_id' in data:
        new_student.client_student_id = data['client_student_id']

    if 'attributes' in data:
        for attr_name, attr_value in data['attributes'].items():
            new_student.attributes[attr_name] = attr_value

    new_student.save()

    return HttpResponse(new_student.to_json(), content_type="application/json")
    
#/student/(?P<id>\d+)/
# - GET list of all arbitrary data about a student
def student(request, id):
    if request.method != "GET":
        return HttpResponseBadRequest()

    try:
        id = ObjectId(id)
    except InvalidId as e:
        return HttpResponseBadRequest()

    this_student = get_document_or_404(Student, pk=id)

    return HttpResponse(this_student.to_json(), content_type="application/json")


#/student/(?P<id>\d+)/attribute/
# - POST {key:values}
# - PUT {key:values}
# - GET {key:values}
def student_attribute(request, id):
    if request.method == "DELETE":
        return HttpResponseBadReqeust()

    try:
        id = ObjectId(id)
    except InvalidId as e:
       return HttpResponseBadRequest(content_type="application/json")        

    this_student = get_document_or_404(Student, pk=id)

    if request.method == "POST" or request.method == "PUT":
        data = json.loads(request.body)
        
        if 'attributes' in data:
            for attr_name, attr_value in data['attributes'].items():
                this_student.attributes[attr_name] = attr_value        

        this_student.save()
        return HttpResponse(this_student.to_json(), content_type="application/json")
    elif request.method == "GET":
        return HttpResponse(json.dumps(dict(this_student.attributes)), content_type="application/json")

    
    return HttpResponseBadRequest()

#/student/(?P<id>\d+)/attribute/(?P<name>[\w-?]+)/'
# - GET value for specific key :name on student
# - PUT value for specific key :name on student
# - POST value for specific key :name on student
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
