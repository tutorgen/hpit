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


class HpitTransaction(models.Model):
    anon_student_id = models.CharField()
    session_id = models.CharField() #unsure
#Order
#Column
#1
#Anon Student Id
#An anonymized student identifier.
#2
#Session Id
#A dataset-unique string that identifies the user's session with the tutor.
#3
#Time
#Local time. Must be given in one of the following standard time formats [2]
#4
#Time Zone
#Local time zone ID as provided by the zoneinfo (or tz) database. Select a time zone name from the "TZ" column in this List of zoneinfo time zones.
#5
#Student Response Type
#A semantic description of the event. DataShop-expected values are ATTEMPT or HINT_REQUEST. See the corresponding "Tutor Response Type" below.
#6
#Student Response Subtype
#A further classification of student response type.
#7
#Tutor Response Type
#A semantic description of the tutor's response. DataShop-expected values are RESULT or HINT_MSG. See the corresponding "Student Response Type" above.
#8
#Tutor Response Subtype
#A further classification of tutor response type.
#9
#Level()
#A Dataset Level. An example of the correct use of this column heading is Level(Unit), where "Unit" is the dataset level title and the value in the column is the level name (e.g., "Understanding Fractions"). The Level column should always be of the format Level(level_title). The level title must be ≤ 100 characters and consist of letters, numbers, dashes, underscores, and spaces. If a dataset level title is not included, it will become "Default". Multiple Level columns are OK. For additional description, see the level element in the Guide. In tutor-message format XML, level "title" is referred to as "type".
#10
#Problem Name
#The name of the problem or activity.
#11
#Problem View
#The number of times the student encountered the problem so far. This counter increases with each instance of the same problem. Provide either this column or Problem Start Time, but not both. If both are provided, Problem Start Time is used to determine Problem View. A longer description of problem view, including how it is determined if it's not present in the imported data, is available here.
#12
#Problem Start Time
#The time the problem is shown to the student. Must be given in one of the standard time formats [2]. Provide either this column or Problem View, but not both. If both are provided, Problem Start Time is used to determine Problem View. A longer description of problem start time, including how it is determined if it's not present in the imported data, is available here.
#13
#Step Name
#The name of a discrete problem-solving step. Include a step name for a transaction if the transaction also has a Tutor Response Type and an Outcome. Otherwise, Attempt At Step will not be calculated.
#14
#Attempt At Step
#DataShop ignores the values in this column when processing the import file. "Attempt at Step" is computed from the rest of the transaction data, but only if Step Name is provided.
#15
#Outcome
#The tutor's evaluation of the action, if applicable. DataShop prefers the values CORRECT, INCORRECT, or HINT.
#16
#Selection
#A description of the interface element that the student selected or interacted with. Multiple Selection columns are OK. Also see Selection in the Guide.
#17
#Action
#A description of the manipulation applied to the selection. Multiple Action columns are OK.
#18
#Input
#The input the student submitted. Multiple Input columns are OK. Also see Input in the Guide.
#19
#Feedback Text
#The body of a hint, success, or error message shown to the student.
#20
#Feedback Classification
#A further classification of the outcome. See action_evaluation / classification in the Guide. Note that if Feedback Classification has a value, Feedback Text must have a value as well.
#21
#Help Level
#Applicable only to hints, this is the current hint level/depth. If given, value must be a number.
#22
#Total Num Hints
#Total number of hints available to the student for this step. If given, value must be a number.
#23
#Condition Name
#A study/experimental condition. Must always be paired with Condition Type, even if a condition does not have a condition type. Multiple Condition Name columns are OK. See condition in the Guide.
#24
#Condition Type
#A condition classification. Must always be paired with Condition Name, even if a condition does not have a condition type. Multiple Condition Type columns are OK. If Condition Type is specified, Condition Name must have a value as well.
#25
#KC()
#A knowledge component. An example of the correct use of this column heading could be KC(Area), where 'Area' is the KC model name for that knowledge component. The KC column should always be of the format KC(kc_model_name). The model name must be ≤ 50 characters and consist of letters, numbers, dashes, underscores, and spaces. If a KC model name is not included, the name will default to "Default". Multiple KC columns are OK.
#26
#KC Category()
#A knowledge component category. An example of the correct use of this column heading could be KC Category(Area), where 'Area' is the KC model name for that knowledge component. The KC Category column should always be of the format KC Category(kc_model_name). The model name must be ≤ 30 characters and consist of letters, numbers, dashes, underscores, and spaces. If a KC model name is not included, the name will default to "Default". If including KC Category, be sure to pair it with a corresponding KC column by using the same KC model name. (Condition Name and Type must be paired together in the same way.) If you specify a a KC Category value, a KC value must be given as well. Multiple KC Category columns are OK.
#27
#School
#The school in which the data were collected, if applicable.
#28
#Class
#The class in which the data were collected, if applicable.
