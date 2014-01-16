import string
import random
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from core.models import *

random.seed(datetime.now())

ATTRIBUTES = [
    'boredom', 'grit', 'topic_pref', 'sadness', 'emotional_impairment', 
    'hit_points', 'learning_baggage'
]

SKILLS = ["Subtraction", "Addition", "Critical Thinking", "Visualization", "Comprehension"]
STEPS = ["Add to both sides", "Subtract from both sides", "Multiply both sides", "Divide both sides", "Combine terms", "Apply associative property"]

TUTOR_NAMES_F = ["Generic", "General", "Specialized", "Independent", "Focused"]
TUTOR_NAMES_T = ["Modern Art", "World History", "Math", "Geology", "Astronomy", "Warfare"]
TUTOR_NAMES_L = ["Tutor", "Instruction", "Teaching", "Professor"]
TUTOR_NAMES_V = ["of wisdom", "of great insight", "for professional readiness", "ABCs", "the great and knowing"]

GENERAL_DESCRIPTION = "ombie ipsum reversus ab viral inferno, nam rice grikes malum cerebro. De carne lumbering animata corpora quaeritis."

def gen_student():
    print("Generating New Student")
    new_student = Student()
    new_student.client_student_id = ''.join([random.choice(string.hexdigits) for x in range(16)])
    new_student.save()

    return new_student

def gen_student_attribute(student, attribute):
    print("Generating new attribute on student")
    stu_attr = StudentAttribute()
    stu_attr.student = student
    stu_attr.name = random.choice(ATTRIBUTES)
    stu_attr.value = random.choice(range(6))
    stu_attr.save()

    return stu_attr

def gen_tutor():
    print("Generating New Tutor")
    new_tutor = Tutor()
    new_tutor.name = ' '.join([
        random.choice(TUTOR_NAMES_F),
        random.choice(TUTOR_NAMES_T),
        random.choice(TUTOR_NAMES_L),
        random.choice(TUTOR_NAMES_V)
    ])
    new_tutor.save()

    return new_tutor


def gen_question(tutor):
    print("Generating New Question")
    quest = Question()
    quest.tutor = tutor
    quest.description = GENERAL_DESCRIPTION
    quest.save()

    return quest


def gen_question_step(question):
    step = QuestionStep()
    step.question = question
    step.description = random.choice(STEPS)
    step.save()
    return step


def generate_question_skill(step, skill_str):
    skill = QuestionSkill()
    skill.question_step = step
    skill.name = skill_str
    skill.value = random.choice(range(6))
    skill.save()
    return skill

class Command(BaseCommand):
    args = ''
    help = 'This generates fake data for HPIT developers'

    def handle(self, *args, **options):

        for i in range(100):
            tutor = gen_tutor()

            for j in range(random.choice(range(30, 100))):
                question = gen_question(tutor)
                print j

                for k in range(random.choice(range(1, 10))):
                    step = gen_question_step(question)

                    skills = random.sample(SKILLS, random.choice(range(1, 4)))

                    for sk in skills:
                        generate_question_skill(step, sk)

        for i in range(100):
            student = gen_student()

            attributes = random.sample(ATTRIBUTES, random.choice(range(1, 6)))

            for attr in attributes:
                gen_student_attribute(student, attr)

        print("DONE!")
