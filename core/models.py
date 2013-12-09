import mongoengine as me

# Create your models here.
class Student(me.Document):
    email = me.StringField(required=True)
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)