from tastypie.resources import ModelResource
from tastypie import fields
from core.models import *
from core.authorization import GuardianAuthorization

class StudentResource(ModelResource):
    attributes = fields.ToManyField('core.api.StudentAttributeResource', 'attributes', full=True)

    class Meta:
        queryset = Student.objects.all()
        resource_name = 'student'
        authorization = GuardianAuthorization()


class StudentAttributeResource(ModelResource):
    student = fields.ForeignKey(StudentResource, 'student')

    class Meta:
        queryset = StudentAttribute.objects.all()
        resource_name = 'student_attribute'
        authorization = GuardianAuthorization()


class TutorResource(ModelResource):
    class Meta:
        queryset = Tutor.objects.all()
        resource_name = 'tutor'
        authorization = GuardianAuthorization()


class QuestionResource(ModelResource):
    tutor = fields.ForeignKey(TutorResource, 'tutor')

    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        authorization = GuardianAuthorization()


class QuestionStepResource(ModelResource):
    question = fields.ForeignKey(QuestionResource, 'question')

    class Meta:
        queryset = QuestionStep.objects.all()
        resource_name = 'question_step'
        authorization = GuardianAuthorization()


class QuestionSkillResource(ModelResource):
    question_step = fields.ForeignKey(QuestionStepResource, 'question_step')

    class Meta:
        queryset = QuestionSkill.objects.all()
        resource_name = 'question_skill'
        authorization = GuardianAuthorization()


class HpitTransactionResource(ModelResource):

    class Meta:
        queryset = HpitTransaction.objects.all()
        resource_name = 'hpit_transaction'
        authorization = GuardianAuthorization()
