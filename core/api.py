from tastypie.resources import ModelResource
from tastypie import fields
from core.models import *

class StudentResource(ModelResource):
    class Meta:
        queryset = Student.objects.all()
        resource_name = 'student'


class StudentAttributeResource(ModelResource):
    student = fields.ForeignKey(StudentResource, 'student')

    class Meta:
        queryset = StudentAttribute.objects.all()
        resource_name = 'student_attribute'


class TutorResource(ModelResource):
    class Meta:
        queryset = Tutor.objects.all()
        resource_name = 'tutor'


class QuestionResource(ModelResource):
    tutor = fields.ForeignKey(TutorResource, 'tutor')

    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'


class QuestionStepResource(ModelResource):
    question = fields.ForeignKey(QuestionResource, 'question')

    class Meta:
        queryset = QuestionStep.objects.all()
        resource_name = 'question_step'


class QuestionSkillResource(ModelResource):
    question_step = fields.ForeignKey(QuestionStepResource, 'question_step')

    class Meta:
        queryset = QuestionStep.objects.all()
        resource_name = 'question_skill'
