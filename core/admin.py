from django.contrib import admin
from core.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('client_student_id', 'created_at', 'updated_at')

class StudentAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'updated_at')

class QuestionSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'updated_at')

class QuestionStepAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentAttribute, StudentAttributeAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStep, admin.ModelAdmin)
admin.site.register(QuestionSkill, QuestionSkillAdmin)
