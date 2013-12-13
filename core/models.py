from django.db import models
from django.core.validators import RegexValidator

bsv_validator = RegexValidator(regex='[\s?\w*\s?|]+')

# Create your models here.
class Student(models.Model):
    client_student_id = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.client_student_id)



class StudentAttribute(models.Model):
    student = models.ForeignKey(Student, related_name="attributes")
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)



class Tutor(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)



class Question(models.Model):
    tutor = models.ForeignKey(Tutor)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.description)



class QuestionStep(models.Model):
    question = models.ForeignKey(Question)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.question)


class QuestionSkill(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=4000)
    question_step = models.ForeignKey(QuestionStep)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)    


class HpitTransaction(models.Model):
    anon_student_id = models.CharField(max_length=30)
    session_id = models.CharField(max_length=30)
    tran_time = models.TimeField()
    time_zone = models.CharField(max_length=30)
    stu_response_type = models.CharField(max_length=30)
    stu_response_subtype = models.CharField(max_length=30)
    tutor_response_type = models.CharField(max_length=30)
    tutor_response_subtype = models.CharField(max_length=30)
    level = models.CharField(max_length=100)
    problem_name = models.CharField(max_length=100)
    problem_view = models.IntegerField()
    problem_start_time = models.TimeField()
    step_name = models.CharField(max_length=300)
    attempt_at_step = models.IntegerField()
    outcome = models.CharField(max_length=30)
    selection = models.TextField(validators=[bsv_validator])
    action = models.TextField(validators=[bsv_validator])
    stu_input = models.TextField(validators=[bsv_validator])
    feedback = models.TextField()
    feedback_class = models.CharField(max_length=30)
    help_level = models.IntegerField()
    total_avail_hints = models.IntegerField()
    # condition_name and condition_type can be multi-valued, but need to be parallel
    condition_name = models.TextField(validators=[bsv_validator])
    condition_type = models.TextField(validators=[bsv_validator])
    kc_model = models.CharField(max_length=50)
    kc_category = models.CharField(max_length=30)
    stu_school = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=100)
