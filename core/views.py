from django.shortcuts import render

# Create your views here.
#/student/
def create_student(request):
	pass
    
#/student/(?P<id>\d+)/
def student(request, id):
	pass

#/student/(?P<id>\d+)/attribute/
def student_attribute(request, id):
	pass

#/student/(?P<id>\d+)/attribute/(?P<name>[\w-?]+)/'
def student_attribute_name(request, id, name):
	pass
    
#/student/(?P<id>\d+)/question/(?P<question_id>\d+)/
def student_question_hint(request, id, question_id):
	pass
    
#/student/(?P<id>\d+)/question/(?P<question_id>\d+)/
def student_question_next(request, id, question_id):
	pass