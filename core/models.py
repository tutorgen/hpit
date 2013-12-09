import mongoengine as me
from datetime import datetime

# Create your models here.
class Student(me.Document):
	attributes = me.ListField(me.StringField)
	created_at = me.DateTimeField(default=datetime.now)
	updated_at = me.DateTimeField(default=datetime.now)

	@classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()

    
class QuestionStep(me.Document):
	skills = me.ListField(me.StringField)
	created_at = me.DateTimeField(default=datetime.now)
	updated_at = me.DateTimeField(default=datetime.now)

	@classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()


class Question(me.Document):
	steps = me.ListField(me.EmbeddedDocument(QuestionStep))
	created_at = me.DateTimeField(default=datetime.now)
	updated_at = me.DateTimeField(default=datetime.now)

	@classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()


class Tutor(me.Document):
	questions = me.ListField(me.EmbeddedDocument(Question))
	created_at = me.DateTimeField(default=datetime.now)
	updated_at = me.DateTimeField(default=datetime.now)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now()

signals.pre_save.connect(Student.pre_save, sender=Student)
signals.pre_save.connect(QuestionStep.pre_save, sender=QuestionStep)
signals.pre_save.connect(Question.pre_save, sender=Question)
signals.pre_save.connect(Tutor.pre_save, sender=Tutor)