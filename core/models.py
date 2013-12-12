from django.db import models

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
